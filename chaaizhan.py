# -*- coding: UTF-8 -*-
# @Time:  18:02
# @Author: 浪飒
# @File: chaaizhan.py
# @Software: PyCharm
import json
import time
import click
import requests
import xlwt


def Welcome():
    print('''    
                批量查爱站百度权重工具 author:浪飒
   ________  _____       __________  _________ 
  / ____/ / / /   |     / ____/ __ \/ ____/   |
 / /   / /_/ / /| |    / /_  / / / / /_  / /| |
/ /___/ __  / ___ |   / __/ / /_/ / __/ / ___ |
\____/_/ /_/_/  |_|  /_/    \____/_/   /_/  |_|                                  

Options:
  -f TEXT     请输入所查域名的txt
  
  txt文件内容单个域名换行(不允许出现http://或者https://)：
  例如：
  www.langsasec.cn
  blog.langsasec.cn
  www.baidu.com
  
  --help      Show this message and exit.
        ''')


# 由于爱站每次请求最多50个域名，为防止请求过多选择50以下和50以上两种处理方式
def read_txt(file_name):
    data = []
    file = open(file_name, 'r')  # 打开文件
    file_data = file.readlines()  # 读取所有行
    for row in file_data:
        tmp_list = row.split(' ')  # 按‘，'切分每行的数据

        # 去除带端口的情况,先去除每行数据冒号后的端口在添加|
        tmp_list[-1] = tmp_list[-1].split(":", 1)[0]
        tmp_list[-1] = tmp_list[-1] + '|'
        print(tmp_list)
        tmp_list[-1] = tmp_list[-1].replace('\n', '|')  # 去掉换行符
        tmp_list[-1] = tmp_list[-1].replace('||', '|')  # 将之前加的|去掉
        data.append(tmp_list)  # 将每行数据插入data中
    if len(data) < 50 or len(data) == 50:
        # 数据不大于50条
        domains = ''
        for i in data:
            domains = domains + i[0]
        return domains
    if len(data) > 50:
        # 数据大于50条
        domains = []

        def list_split(items, n):
            return [items[i:i + n] for i in range(0, len(items), n)]

        domain_list = list_split(data, 50)
        for i in domain_list:
            domain = ''
            for j in i:
                domain = domain + j[0]
            domains.append(domain)
        return domains


def chaaizhan50(f):
    # 数据小于50
    domains = read_txt(f)
    req = f"https://apistore.aizhan.com/baidurank/siteinfos/521566b9bbdb4ec67b1d3f94a62a5e56?domains={domains}"
    res = requests.get(req).content.decode("utf-8")
    dict_data = json.loads(res)  # json转成python字典
    results = dict_data.get('data')['success']
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet(f'{f}_爱站查询结果', cell_overwrite_ok=True)
    col = ('域名', 'PC权重', '移动权重')
    for i in range(0, 3):
        sheet.write(0, i, col[i])
    for i in range(len(results)):
        data = results[i]
        data = [data['domain'], data['pc_br'], data['m_br']]
        for j in range(0, 3):
            sheet.write(i + 1, j, data[j])
    path = f'{str(time.time().__hash__())}_爱站查询查询结果.xls'
    book.save(path)
    print(f"表格已保存为{path}")


def chaaizhan51(f):
    # 数据大于50
    domains = read_txt(f)
    print(domains)
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet(f'{f}_爱站查询结果', cell_overwrite_ok=True)
    col = ('域名', 'PC权重', '移动权重')
    for i in range(0, 3):
        sheet.write(0, i, col[i])
    flag = -1  # 每次循环数组时，写入表格的 50*flag,即每五十组数据写一次
    for domains1 in domains:
        flag = flag + 1
        req = f"https://apistore.aizhan.com/baidurank/siteinfos/521566b9bbdb4ec67b1d3f94a62a5e56?domains={domains1}"
        res = requests.get(req).content.decode("utf-8")
        dict_data = json.loads(res)  # json转成python字典
        results = dict_data.get('data')['success']
        for i in range(len(results)):
            data = results[i]
            data = [data['domain'], data['pc_br'], data['m_br']]
            for j in range(0, 3):
                sheet.write(flag * 50 + i + 1, j, data[j])
    path = f'{str(time.time().__hash__())}_爱站查询查询结果.xls'
    book.save(path)
    print(f"表格已保存为{path}")


@click.command()
@click.option("-f", help="请输入所查域名的txt", prompt="请输入所查域名的txt")
def chaaizhan(f):
    domains = read_txt(f)
    if type(domains) is list:
        chaaizhan51(f)
    else:
        chaaizhan50(f)


if __name__ == '__main__':
    Welcome()
    chaaizhan()

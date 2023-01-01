# chaaizhan
## 介绍

一款命令行批量爱站百度权重查询工具，可快速将查询结果导出到表格中。

## 说明

代码中处理了可能存在http和端口的情况，因此格式可以无需非常严格，如果出问题请及时提出。

## 使用

```shell
				批量查爱站百度权重工具 author:浪飒
   ________  _____       ___    _________   __  _____    _   __
  / ____/ / / /   |     /   |  /  _/__  /  / / / /   |  / | / /
 / /   / /_/ / /| |    / /| |  / /   / /  / /_/ / /| | /  |/ /
/ /___/ __  / ___ |   / ___ |_/ /   / /__/ __  / ___ |/ /|  /
\____/_/ /_/_/  |_|  /_/  |_/___/  /____/_/ /_/_/  |_/_/ |_/


Options:
  -f TEXT     请输入所查域名的txt

  txt文件内容单个域名换行
  例如：
  www.langsasec.cn
  blog.langsasec.cn
  www.baidu.com

  --help      Show this message and exit.

表格已保存为779197503998387307_爱站查询查询结果.xls
```

```sh
python chaaizhan.py -f domain.txt

```

![image-20230102035805561](https://i0.hdslb.com/bfs/album/8732439be86ee85f7dee77d4d9e50343159bdeeb.png)

![image-20230102035830330](https://i0.hdslb.com/bfs/album/e059f939a56fef3b2b292ad098ed78871c4dfe29.png)

![image-20230102040059609](https://i0.hdslb.com/bfs/album/b80e0a3e7a52adbc48cbd529439f2d9a649f1fbd.png)


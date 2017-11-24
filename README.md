# YiyipinWebsite
(venvSOA) [root@izwz9hbv3lrr68d8bo5dvpz M_Arts]# 
git clone git://github.com/RomanceSky/YiyipinWebsite.git

意艺品
http://blog.csdn.net/wcc526/article/details/12239649

ljj123ljj
<h1>一、使用Djang框架自带的SQLite数据库</h1>

<h1>二、使用MySQL数据库</h1>
<p>
因为自己使用的是Centos，所以在Centos中应该使用MariaDB数据库
</p>
(venvSOA) [root@izwz9hbv3lrr68d8bo5dvpz M_Arts]# mysql -u root -p1234
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 35
Server version: 5.5.56-MariaDB MariaDB Server

Copyright (c) 2000, 2017, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> 
同时注意：登录时 mysql -u root -p1234中-p和密码之间是没有空格的

MariaDB [(none)]> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
+--------------------+
3 rows in set (0.00 sec)
https://www.w3cschool.cn/mariadb/mariadb_installation.html

http://www.uedsc.com/python-programs-connect-mariadb.html
http://blog.csdn.net/yf999573/article/details/53081196

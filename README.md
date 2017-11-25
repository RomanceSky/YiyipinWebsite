# YiyipinWebsite
(venvSOA) [root@izwz9hbv3lrr68d8bo5dvpz M_Arts]# 
git clone git://github.com/RomanceSky/YiyipinWebsite.git
git克隆指定分支的代码:
git clone -b 分支名仓库地址


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



Administrator@XB-20170707EUDB MINGW64 ~/Downloads/Boot (master)
$ git init
Initialized empty Git repository in C:/Users/Administrator/Downloads/Boot/.git/

Administrator@XB-20170707EUDB MINGW64 ~/Downloads/Boot (master)
$ git push origin jun
error: src refspec jun does not match any.
error: failed to push some refs to 'origin'

Administrator@XB-20170707EUDB MINGW64 ~/Downloads/Boot (master)
$ git config --global user.name "RomanceSky"

Administrator@XB-20170707EUDB MINGW64 ~/Downloads/Boot (master)
$ git config --global user.email "1171039932@qq.com"

Administrator@XB-20170707EUDB MINGW64 ~/Downloads/Boot (master)
$ git remote add origin https://github.com/RomanceSky/YiyipinWebsite.git

Administrator@XB-20170707EUDB MINGW64 ~/Downloads/Boot (master)
$ git push -u origin master
error: src refspec master does not match any.
error: failed to push some refs to 'https://github.com/RomanceSky/YiyipinWebsite.git'

Administrator@XB-20170707EUDB MINGW64 ~/Downloads/Boot (master)
$ git commit
On branch master

Initial commit

Untracked files:
        bootstrap-3.3.7/

nothing added to commit but untracked files present

Administrator@XB-20170707EUDB MINGW64 ~/Downloads/Boot (master)
$ git branch -a

Administrator@XB-20170707EUDB MINGW64 ~/Downloads/Boot (master)
$ git pull origin master
remote: Counting objects: 39, done.
remote: Compressing objects: 100% (37/37), done.
remote: Total 39 (delta 11), reused 3 (delta 0), pack-reused 0
Unpacking objects: 100% (39/39), done.
From https://github.com/RomanceSky/YiyipinWebsite
 * branch            master     -> FETCH_HEAD
 * [new branch]      master     -> origin/master

Administrator@XB-20170707EUDB MINGW64 ~/Downloads/Boot (master)
$ git push -u origin master
Everything up-to-date
Branch master set up to track remote branch master from origin.

Administrator@XB-20170707EUDB MINGW64 ~/Downloads/Boot (master)
$


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

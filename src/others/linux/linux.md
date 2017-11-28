## 1.linux

```
'''

ps -ef | grep java # 查询：grep 管道：| 包含：java
ls --help | more # 分页：more 查询：ls 帮助信息：help
netstat -an |grep 3306 # 查询：grep 网络端口：netstat 3306  占用情况：an
df -h # 磁盘信息：disk 大小：-h
free -m # 内存：-m
用top查看所有？CPU mem Swap 进程

所有进程查看： ps -ef
kill -9 2868 强制杀死进程

du -h 目录：directory 大小：-h
vi /etc/sysconfig/netwprk

user add test -d /home/t1
passwd test

chmod 755 a.txt
chmod u=rwx,g=rx,o=rx a.txt
user group exe

chown u:public a.txt



echo "angelababy,zhen de hen xihuan ni" > qingshu.txt  把左边的输出放到右边的文件里去


磁盘空间信息查看
df -h  查看磁盘空间状态信息
du -sh * 查看当前目录下所有子目录和文件的汇总大小

nvidia显卡的话可以用nvidia-smi命令来查

lspci  | grep -i vga

重要的参数主要是温度、内存使用、GPU占有率
57C


关于系统没有apt-get下的MySQL安装：
1、MySQLdb的版本比你安装的mysql版本高，升级一下mysql数据库
2、或者安装一个低版本的MySQLdb：
pip uninstall mysql-python
pip install mysql-python==1.2.5

安装的版本

Mysql使用kill命令解决死锁问题(杀死某条正在执行的sql语句)

show processlist;

# 总核数 = 物理CPU个数 X 每颗物理CPU的核数
# 总逻辑CPU数 = 物理CPU个数 X 每颗物理CPU的核数 X 超线程数

# 查看物理CPU个数
cat /proc/cpuinfo | grep "physical id" | sort| uniq| wc -l


'''

```

## 1.linux

```
'''
# 进程/端口查询
ps -ef | grep java # 查询：grep 管道：| 包含：java
所有进程查看： ps -ef
kill -9 2868 强制杀死进程
netstat -an |grep 3306 # 查询：grep 网络端口：netstat 3306  占用情况：an

# 服务器信息查询
磁盘空间信息查看
df -h  查看磁盘空间状态信息
du -sh * 查看当前目录下所有子目录和文件的汇总大小
df -h # 磁盘信息：disk 大小：-h
du -h 目录：directory 大小：-h
free -m # 内存：-m
用top查看所有？CPU mem Swap 进程

总核数 = 物理CPU个数 X 每颗物理CPU的核数
总逻辑CPU数 = 物理CPU个数 X 每颗物理CPU的核数 X 超线程数
查看物理CPU个数
cat /proc/cpuinfo | grep "physical id" | sort| uniq| wc -l

# 用户添加
user add test -d /home/t1
passwd test
vi /etc/sudoers
adduser yufeng
passwd  yufeng
yufeng  ALL=(ALL)    ALL
yufeng  cadyf

.bashrc
远程访问Jupyter Notebook


# 文件（普通查询。权限查询）
1、查看文件的最后20行：tail -n 20 filename
2、查看某关键词前后几行内容：cat filename | grep AAA -A4(后4行) -B4(前4行)
3、
ls --help | more # 分页：more 查询：ls 帮助信息：help
chmod 755 a.txt
chmod u=rwx,g=rx,o=rx a.txt（还没用过+u +g +o）
user group exe
chown u:public a.txt
echo "angelababy,zhen de hen xihuan ni" > qingshu.txt  把左边的输出放到右边的文件里去

多文件压缩
zip -r .-x "" ""

# GPU信息查看
nvidia显卡的话可以用nvidia-smi命令来查
lspci  | grep -i vga
重要的参数主要是温度、内存使用、GPU占有率
57C

# 数据库
也不知道为什么，就常卡死，解决方法：
Mysql使用kill命令解决死锁问题(杀死某条正在执行的sql语句)
show processlist;

关于系统没有apt-get下的MySQL安装：
1、MySQLdb的版本比你安装的mysql版本高，升级一下mysql数据库
2、或者安装一个低版本的MySQLdb：
pip uninstall mysql-python
pip install mysql-python==1.2.5

数据库索引原理以及类别以及具体使用场景（BUG）
原理。。。
1、普通索引
2、唯一索引
3、主键索引
4、主键索引

这里应该C++ 会比较研究红黑树吧


# 链接
硬链接：
ln f1 f2
软链接=符号链接
ln -s f1 f3
当删除f1，f2仍旧有值，f3将失效


# 网络管理
1、ifconfig
2、netstat
netstat -anp 可是查看正在监听网络的程序。。。
3、hostname
4、ping
5、traceroute
6、ifconfig
vi /etc/sysconfig/netwprk


#

'''

```

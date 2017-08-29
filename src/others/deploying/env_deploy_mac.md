Mac os系统下安装YARN

## 一. 安装yarn伪分布式集群
### 1. 系统环境配置
```
(1) 安装brew: /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
(2) 更新homebrew源
    1. cd /usr/local/Homebrew
    2. git remote set-url origin http://mirrors.ustc.edu.cn/homebrew.git
    3. cd ~
    4. mkdir tmp
    5. cd tmp
    6. git clone http://mirrors.ustc.edu.cn/homebrew.git
    7. sudo rm -rf /usr/local/.git
    8. sudo rm -rf /usr/local/Library
    9. sudo cp -R homebrew/.git /usr/local/
    10. sudo cp -R homebrew/Library /usr/local/
    11. brew update
(3) 设置免登陆
    cd ~/.ssh  
    rm ./id_rsa*  
    ssh-keygen -t rsa  (一路回车即可)  
    cat ./id_rsa.pub >> ./authorized_keys 
```

### 2. 安装java环境
```
(1) 下载jdk: http://download.oracle.com/otn-pub/java/jdk/7u79-b15/jdk-7u79-macosx-x64.dmg
(2) 安装jdk:
    1. hdiutil mount jdk-7u79-macosx-x64.dmg
    2. sudo cp -R /Volumes/JDK\ 7\ Update\ 79 /Applications
    3. 进入到应用程序 安装JDK
(2) 设置环境变量JAVA_HOME: 
    1. vim ~/.bash_profile 
    2. 添加一行
       export JAVA_HOME=`/usr/libexec/java_home`
    3. source ~/.bash_profile  
```

### 3. 安装hadoop2
```
(1) 从http://ftp.mirror.tw/pub/apache/hadoop/common/hadoop-2.7.3/hadoop-2.7.3.tar.gz
    下载最新的稳定版本的hadoop，例如hadoop-2.7.3/hadoop-2.7.3.tar.gz  
(2) 安装hadoop:  
    1. tar -zxf hadoop-2.7.3.tar.gz -C /usr/local  
    2. cd /usr/local  
    3. mv hadoop-2.7.3 hadoop  
```

### 4. 配置hadoop
```
1). cd /usr/local/hadoop/etc/hadoop
    进入hadoop配置目录，如果没有hadoop-env.sh或yarn-env.sh需要从后缀名为hadoop-env.sh.template复制一份 
2). hadoop-env.sh中配置JAVA_HOME  
3). yarn-env.sh中配置JAVA_HOME  
    参考 ~/.bash_profile
```
```
4). 修改core-site.xml  
<configuration>  
        <property>  
             <name>hadoop.tmp.dir</name>  
             <value>file:/usr/local/hadoop/tmp</value>  
             <description>Abase for other temporary directories.</description>  
        </property>  
        <property>  
             <name>fs.defaultFS</name>  
             <value>hdfs://localhost:9000</value>  
        </property>  
</configuration>  
```
```
4). hdfs-site.xml  
<configuration>  
        <property>  
             <name>dfs.replication</name>  
             <value>1</value>  
        </property>  
        <property>  
             <name>dfs.namenode.name.dir</name>  
             <value>file:/usr/local/hadoop/tmp/dfs/name</value>  
        </property>  
        <property>  
             <name>dfs.datanode.data.dir</name>  
             <value>file:/usr/local/hadoop/tmp/dfs/data</value>  
        </property>  
</configuration>  
```
```
5). mapred-site.xml  
<configuration>  
    <property>  
        <name>mapreduce.framework.name</name>  
        <value>yarn</value>  
    </property>  
</configuration>  
```
```
6). yarn-site.xml  
<configuration>  
    <property>  
        <name>yarn.nodemanager.aux-services</name>  
        <value>mapreduce_shuffle</value>  
    </property>
</configuration>  
```

### 6. 启动hadoop
```
(1) namenode格式化  
    ./bin/hdfs namenode -format  
(2) 修改~/.bash_profile添加以下两行，并执行source ~/.bash_profile  
    export HADOOP_HOME=/usr/local/hadoop   
    export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native  
(3) ./libexec/hadoop-config.sh 找到JAVA_HOME，在前面添加  
    export JAVA_HOME=...  
(4) 开启 NameNode 和 DataNode 守护进程  
    ./sbin/start-dfs.sh  
(5) jps命令查看是否成功启动  
    若成功启动则会列出如下进程: “NameNode”、”DataNode” 和 “SecondaryNameNode”（如果 SecondaryNameNode 没有启动，请运行 sbin/stop-dfs.sh 关闭进程，然后再次尝试启动尝试）。如果没有 NameNode 或 DataNode ，那就是配置不成功，请仔细检查之前步骤，或通过查看启动日志排查原因。  
(6) 启动成功后可以通过 http://localhost:50070/查看nameNode和dataNode相关信息  
(7) 关闭hadoop  
    ./sbin/stop-dfs.sh  
    第二次之后启动 hadoop，无需进行 NameNode 的初始化，只需要运行 ./sbin/start-dfs.sh 即可  
```

### 7. 启动YARN
```
(1) 启动yarn  
    ./sbin/start-yarn.sh   
    ./sbin/mr-jobhistory-daemon.sh start historyserver  #开启历史服务器，才能在Web中查看任务运行情况  
(2) jps查看  
    开启后通过 jps 查看，可以看到多了 NodeManager 和 ResourceManager 两个后台进程  
(3) 启动成功后可以通过页面http://localhost:8088/cluster查看集群任务的运行情况  
(4) 关闭yarn  
    ./sbin/stop-yarn.sh   
    ./sbin/mr-jobhistory-daemon.sh stop historyserver  
```

## 二. 安装Spark
```
1. 下载Spark  
   wget "http://d3kbcqa49mib13.cloudfront.net/spark-2.0.0-bin-hadoop2.7.tgz"  
2. 解压到/usr/local  
   tar -xvzf spark-2.0.0-bin-hadoop2.7.tgz -C /usr/local  
   cd /usr/local  
   mv spark-2.0.0-bin-hadoop2.7 spark  
3. 设置环境变化PATH  
   vim ~/.bash_profile  
   设置环境变量PATH添加hadoop和spark的bin路径
   export PATH=$PATH:/usr/local/hadoop/bin:/usr/local/spark/bin  
   source ~/.bash_profile  
```
```
4). 配置Spark   
cd /usr/local/spark/conf   
cp spark-env.sh.template spark-env.sh   
vim spark-env.sh  
配置内容如下  
export JAVA_HOME=`/usr/libexec/java_home`
export HADOOP_HOME=/usr/local/hadoop     
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop  
SPARK_MASTER_IP=master  
SPARK_LOCAL_DIRS=/usr/local/spark  
SPARK_DRIVER_MEMORY=2G  
```
```
5). 启动spark  
sh /usr/local/sbin/start-all.sh  
启动成功后可以使用  
pyspark或spark-submit  
同时也可以访问以下链接查看spark任务  
http://master:8080
```

## 三. tools
### 1. 机器配置
有2种方式运行Spark，一种是使用Yarn另外一种就是Spark的本地模式。为了方面，以后我们都采用Yarn来运行Spark任务，不会再单独启动Spark

```
//bash_profile配置  
export JAVA_HOME=`/usr/libexec/java_home`
export HADOOP_HOME=/usr/local/hadoop     
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native  
export HADOOP_OPTS=-Djava.library.path=$HADOOP_HOME/lib  
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop  
export PATH=$PATH:/usr/local/bin:/usr/local/scons/bin:/usr/local/hadoop/bin:/usr/local/spark/bin  
export LD_LIBRARY_PATH=/usr/local/hadoop/lib/native:$LD_LIBRARY_PATH  
```

### 2. 启动yarn
```
cd /usr/local/hadoop  
./sbin/start-dfs.sh  
./sbin/start-yarn.sh  
./sbin/mr-jobhistory-daemon.sh start historyserver  
jps

//jps查看进程应该有以下几个
NodeManager  
JobHistoryServer  
SecondaryNameNode  
NameNode  
Jps  
ResourceManager  
DataNode  
```

### 3. 停止yarn
```
cd /usr/local/hadoop  
./sbin/stop-dfs.sh  
./sbin/stop-yarn.sh  
./sbin/mr-jobhistory-daemon.sh stop historyserver  
jps
```

### 4. web界面查看
```
查看nameNode和dataNode: http://localhost:50070/  
查看yarn集群: http://localhost:8088/cluster  
```

### 5. 问题汇总
#### 1
1. Hadoop 2.x.x - warning: You have loaded library /home/hadoop/2.2.0/lib/native/libhadoop.so.1.0.0 which might have disabled stack guard.  
```
解决方案  
1. vi ~/.bash_profile  
2. 添加以下2行  
   export HADOOP_COMMON_LIB_NATIVE_DIR=${HADOOP_HOME}/lib/native  
   export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib  
```
2. localhost: ssh: connect to host localhost port 22: Connection refused
```
打开系统偏好设置 —— 共享，选中远程登录
```


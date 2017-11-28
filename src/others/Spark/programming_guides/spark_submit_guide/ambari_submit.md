## 1.增加远程访问

`mapreduce.app-submission.cross-platform`

## 2.修改的是mapred-site.xml

```
'''
$PWD/mr-framework/hadoop/share/hadoop/mapreduce/*:$PWD/mr-framework/hadoop/share/hadoop/mapreduce/lib/*:$PWD/mr-framework/hadoop/share/hadoop/common/*:$PWD/mr-framework/hadoop/share/hadoop/common/lib/*:$PWD/mr-framework/hadoop/share/hadoop/yarn/*:$PWD/mr-framework/hadoop/share/hadoop/yarn/lib/*:$PWD/mr-framework/hadoop/share/hadoop/hdfs/*:$PWD/mr-framework/hadoop/share/hadoop/hdfs/lib/*:$PWD/mr-framework/hadoop/share/hadoop/tools/lib/*:/usr/hdp/2.5.3.0-37/hadoop/lib/hadoop-lzo-0.6.0.2.5.3.0-37.jar:/etc/hadoop/conf/secure
'''
改为：
'''
$PWD/mr-framework/hadoop/share/hadoop/mapreduce/*:$PWD/mr-framework/hadoop/share/hadoop/mapreduce/lib/*:$PWD/mr-framework/hadoop/share/hadoop/common/*:$PWD/mr-framework/hadoop/share/hadoop/common/lib/*:$PWD/mr-framework/hadoop/share/hadoop/yarn/*:$PWD/mr-framework/hadoop/share/hadoop/yarn/lib/*:$PWD/mr-framework/hadoop/share/hadoop/hdfs/*:$PWD/mr-framework/hadoop/share/hadoop/hdfs/lib/*:$PWD/mr-framework/hadoop/share/hadoop/tools/lib/*:/usr/hdp/2.5.3.0-37/hadoop/lib/hadoop-lzo-0.6.0.2.5.3.0-37.jar:/etc/hadoop/conf/secure
'''
```

## 3.其他的修改

### 3.1 idea和eclipse不同，个别的包可能需要手工下载并安装到本地仓库：
```
'''
>>>mvn install:install-file -DgroupId=org.spark-project.hive -DartifactId=hive-jdbc -Dversion=1.2.1.spark2 -Dpackaging=jar -Dfile=/root/Downloads/hive-jdbc-1.2.1.spark2.jar
'''
```
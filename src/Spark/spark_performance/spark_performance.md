## 理清楚概念
### 1.内存：系统总内存数（*n）

`work内存大小*work数` = SPARK_WORKER_INSTANCES * SPARK_WORKER_MEMORY

### 2.CPU：系统总的task数目（*n）

`Work数*work所占的core数` = SPARK_WORKER_INSTANCES * SPARK_WORKER_CORES

### 3.示例

```
'''
1、SPARK_WORKER_INSTANCES=3 SPARK_WORKER_CORES=1 SPARK_WORKER_MEMORY=4G
内存大小：3*4G=12G
Cpu核数：1*3=3
总task数：3*8=24

2、SPARK_WORKER_INSTANCES=4 SPARK_WORKER_CORES=3 SPARK_WORKER_MEMORY=6G
mem(24G)
cpu(12core)
'''
```


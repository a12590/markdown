#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from pyspark import SparkContext
from spark_util import hdfs_util
sc = SparkContext(appName="Spark_0_code")

def main():
    """
    1. first put data_0.dat to hdfs path /user/hadoop/examples/data_0.dat
    """
    raw_data_file = '/user/hadoop/examples/data_0.dat'
    text_file = sc.textFile(raw_data_file)
    new_text_file = text_file.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
    result_data_path = '/user/hadoop/examples/data_0_res'
    if hdfs_util.exists(result_data_path) and hdfs_util.rmdir(result_data_path) is False:
        print "[ERROR] remove hdfs dir:[%s] error" % result_data_path
        sys.exit(2)
    new_text_file.saveAsTextFile(result_data_path)
    # read file
    print hdfs_util.cat(result_data_path + '/part-00000')
    print hdfs_util.cat(result_data_path + '/part-00001')

if __name__ == "__main__":
    try:
        main()
    except Exception,e:
        print "Spark main function exception:[%s]" % str(e)
        sys.exit(2)

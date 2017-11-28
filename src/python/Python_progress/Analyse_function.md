# Analyse_function

## Contents

-  方法一：直接使用Tuple、dict初始的转化方式，期间用到相应的split、set、filter()、sort()的方式

    1）、最简单的统计最多
    spark和MapReduce中使用Map和Reduce的思想，其中< key,count>，然后做统计，最后也是sort的方式得到最多，前几位；
    类似的，使用list，每一项是一个Tuple（key,count）,key(0-24h),count = hours.count(h),将list类型的hours['1','1','8','2']进行按值count，然后使用的是sort的方式得到最大值；
    还加上第二种实现方式：二维数组
    这也是二维数组？ {key：dict()}，其中dict：{key:value}
    访问方式：A[]->{{key:value}},.has_key(key)
          value->A[][key]

    dict:items()->这里的value也是dict：所以得到v之后，for k,v in A.items():v.items()

    dict可以通一维数组方式访问；
    一维数组可以通过lambda方式得到二维数组，sort()中key+reverse；key可以是lambda式子？


    （2）、对象的思想使用python中的B.sort(lambda(A:A[0]))->是B[0]之后，再sort

-   使用pandas、SparkSQL中的DataFrame方式处理

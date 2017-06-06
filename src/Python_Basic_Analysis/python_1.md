# PythonDataAnalysis

## Contents

- Series

1、List和Array、Series（一维数组）的区别：List中的元素可以是不同的数据类型，而Array和Series中则只允许存储相同的数据类型

2、Series类型的对象.values（对应的值：科学计数法）

3、创建 Series 时 index 可以指定特定 meaningful labels 作为 index:
  pd.Series(data=[632, 1638, 569, 115],index=['Firmicutes', 'Proteobacteria', 'Actinobacteria', 'Bacteroidetes']) （其中数据和index位置相对应）

4、可以根据 index 获取 Series 的 value：类似list[0]/Series[0]和Series['Firmicutes']

5、[name.endswith('bacteria') for name in bacteria.index]
  .endswith()返回boolean值，for 定义 in XXX

6、可以指定 Series 的 values 数组 和 index 所表示的含义
  bacteria.name = "细菌数量" bacteria.index.name = '细菌种类'

7、可以对 Series 数据结构的 value 应用 numpy 的 math 函数，结果仍然为 Series
  np.log(bacteria)

8、可以对 Series 的 value 进行过滤
  bacteria[bacteria.values > 100]

9、Series 类似与 ndarray， 可以进行分片等操作
  bacteria[:3]（输出具体的列数据）

10、Series 可以看出一个存储 key-value 的数据结构，我们可以从一个 python 的 dict 创建一个 Series，且创建的 Series 会按照键值排序
  bacteria_dict = {'Firmicutes': 632, 'Proteobacteria': 1638, 'Actinobacteria': 569, 'Bacteroidetes': 115} pd.Series(bacteria_dict)

11、某列某行
  df.columns.ix[0]

- DataFrame

1、创建的 DataFrame 默认通过 column 排序，可以通过指定 index 显示的顺序：
  原来这货是这个意思：data[['value','phylum','patient']]或者data[data.columns]

2、可以通过 data.column 或 data['column'] 获取指定列的数据

3、可以通过 DataFrame 的 ix 属性获取每一行的数据，且支持分片操作：
  这就深刻了，.ix[0] .ix[2:5]

4、可通过一个 dict of ditcs 创建一个复杂结构的 DataFrame
  长见识le：{'patient': 1, 'phylum': 'Firmicutes', 'counts': 632}作为value值，得到的是一个N*N的表

5、可以通过赋值的方式新增或修改一列数据。 注意新增一列只能通过 data['new_column'] 的方式，而不能通过 data.new_column
  data['year'] = 2017，但是会所有行都新增同样的值

- import

1、header=None 表示 csv 文件第一行不是 header 而是数据；

2、可以通过 skiprows 指定读取 csv 文件时跳过哪些行。

3、通过 chunk 进行数据的迭代，用于对大文件的懒加载迭代，而不是将整个文件读入内存。

4、.to_csv(name,sep='\t') to_pickle(name) .read_pickle(name)

Excel
1、需要安装 xlrd 和 openpyxl（anconda默认安装）

2、.ExcelFile（import） .parse（得到sheetname） .columns（指定读入的列）

3、# 按照 Count 值降序排列（如何实现？）sort_index(axis=1) 的 axis 指定了按照列/行进行排序(默认升序排列)
  .Count.sort_values(ascending=False)

Missing data
1、去除确实的数据，注意 foo 的元素并没有改变
  foo.dropna() 这货提醒了我，说明它仅仅进入foo的某个状态

2、去除重复数据
  .drop_duplicates()

3、填充，看看这一种填充方式：data 的内容不会修改，可采用赋值的方式进行修改，而且还是不修改！！
  data.fillna({'patient': -1, 'counts': 0})


1、.value_counts().hist(bins=500)得到直方图

2、strptime 字符串转换为时间类型，同理使用：dateutil 用于自动检测时间格式并将其转换 from dateutil.parser import parse

3、如果要对所有的行执行一个统一的操作：.apply(lambda date_parse: datetime.strptime(date_parse, '%m/%d/%y %H:%M'))

4、# pandas 提供了一个便捷的函数用于 Series 数据的格式化为 datetime 类型
  瞬间上面的没啥意义了



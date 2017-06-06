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

- DataFrame

1、创建的 DataFrame 默认通过 column 排序，可以通过指定 index 显示的顺序：
  原来这货是这个意思：data[['value','phylum','patient']]或者data[data.columns]

2、可以通过 data.column 或 data['column'] 获取指定列的数据

3、


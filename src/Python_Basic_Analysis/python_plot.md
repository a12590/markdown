# PythonDataAnalysis

## Contents


- matplotlib.pyplot as plt

1、plt.plot(np.random.normal(size=100), np.random.normal(size=100), 'go')
  go（green dot） bo（blue dot）


- Plotting in Pandas
1、Pandas 的 DataFrame 和 Series 直接支持 matplotlib 绘制。
  简单例子：pd.Series(np.random.normal(size=10)).plot(grid=True)

2、补充对于pandas的函数：dataframe.cumsum ，用于计算 dataframe 的累积和,axis属性指定累积和的轴
  .cumsum(0).plot()（这里在统一窗口中绘制） subplots参数分开绘制  .plot(subplots=True)

3、secondary_y （DataFrame的key值）用于指定在右边的标记
  在plot函数中.plot(secondary_y='normal')

4、plt.subplots(nrows=1, ncols=3, figsize=(12, 4))
  上回说了：fig, axes，其中axes是一个数组，遍历对1*3窗口进行操作

5、title值设置，既然plot函数中的1*3窗口axes[0]\axes[1]\axes[2]，那么设置title时，
  for i,var in enumerate(['normal','gamma','poisson']):有了0 1 2 以及对应的title值
  设置：variables[var].cumsum(0).plot(ax=axes[i], title=var)


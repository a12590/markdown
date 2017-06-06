# Kaggle-House-Prices

## Contents

- Exploratory_data_analysis

1、Ipython（绘图时加上%matplotlib inline）

2、对要预测的目标数据y：SalePrice有一个宏观的把握，这里是输出summary，也可以用boxplot，histogram等形式观察
    #Set up the matplotlib figure
	plt.figure(figsize=(12,5))
    # 同subplot [1,2,1],表示在本区域里显示1行2列个图像，最后的1表示本图像显示在第一个位置。
	plt.subplot(121)
	sns.distplot(df['SalePrice'],kde=False)
	plt.xlabel('Sale price')
	plt.axis([0,800000,0,180])
	plt.subplot(122)
	sns.distplot(np.log(df['SalePrice']),kde=False)
	plt.xlabel('Log (sale price)')# x轴标签
	plt.axis([10,14,0,180])

3、通过Correlation matrix观察哪些变量会和预测目标关系比较大，哪些变量之间会有较强的关联
    data.corr() #相关系数矩阵，即给出了任意两之间的相关系数
    data.corr()[u'A'] #只显示“A”与其他的相关系数
    data[u'A'].corr(data[u'B']) #计算“A”与“B”的相关系数

    corr = df.select_dtypes(include = ['float64', 'int64']).iloc[:,1:].corr()
    #fig = plt.figure()
	sns.set(font_scale=1)
	sns.heatmap(corr, vmax=1, square=True)

	# 得到热力图，分析发现关联程度不同，变量之间的关联图，可以打印出与目标‘SalePrice’最紧密关联的10个变量的关联度
	cols=corrmat.nlarGEst(k, SalePrice )[ SalePrice ].index
	cm=np.corrcoef(df_train[cols].values.T)
	sns.set(font_sCAle=1.25)
	hm=sns.heatmap(cm,cbar=True,annot=True,square=True,fmt= .2f ,annot_kws={ size :10},yticklabels=cols.values,xticklabels=cols.values)
	plt.show

	# 看不懂，换种方式：承接corr，
	corr_list = corr['SalePrice'].sort_values(axis=0,ascending=False).iloc[1:]
	corr_list

	# 再考虑用图表的方式展示结果数据
	plt.figure(figsize=(18,8))
	for i in range(6):
		ii = '23'+str(i+1)
		# 在2*3窗口中，操作第i个窗口
		plt.subplot(ii)
		# 得到 columns值，
		feature = corr_list.index.values[i]
		# 散点图
		plt.scatter(df[feature], df['SalePrice'], facecolors='none',edgecolors='k',s = 75)
		# reg 说明是一条回归线（不知道这样理解是否正确）
		sns.regplot(x = feature, y = 'SalePrice', data = df,scatter=False, color = 'Blue')
		#子图
		ax=plt.gca()
		ax.set_ylim([0,800000])

	#也可以换种图形类型，
	plt.figure(figsize = (12, 6))
	sns.boxplot(x = 'Neighborhood', y = 'SalePrice',  data = df)
	xt = plt.xticks(rotation=45)

	意义：通过这些数值，我们再一一观察变量含义，判断一下是否可以把其中某些变量删除。

4、接下来看missing value（feature_selection）
	#每个变量的NaN记录个数求和算出来
	total=df_train.isnull.sum.sort_values(ascending=False)
	#再把所占的比例计算一下
	percent=(df_train.isnull.sum/df_train.isnull.count).sort_values(ascending=False)

	#对于占比例太大的变量，例如超过了15%，就看看它的含义，如果不是很重要，这种数据是可以删掉的。
	total_missing = train.isnull().sum()
	to_delete = total_missing[total_missing>(train.shape[0]/3.)]

	#dealing with missing data
	for table in [train,test]:
    table.drop(list(to_delete.index),axis=1,inplace=True)

	#方法二：
	missing_data=pd.concat([total,percent],axis=1,keys=[ Total , Percent ])
	missing_data.head
	df_train=df_train.drop((missing_data[missing_data[ Total ]>1]).index,1)
	df_train=df_train.drop(df_train.loc[df_train[ Electrical ].isnull].index)

5、下面是看outliers
	data=pd.concat([df_train[ SalePrice ],df_train[var]],axis=1)
	data.plot.scatter(x=var,y= SalePrice ,ylim=);
	# 发现数据（几个点的数据）偏离较远，删除
	df_train.sort_values(by= GrLivArea ,ascending=False)[:2]
	df_train=df_train.drop(df_train[df_train[ Id ]==1299].index)
	df_train=df_train.drop(df_train[df_train[ Id ]==524].index)

6、补充知识点：
	DataFrame取一列索引的值
　　①一重索引取值
　　　　df.index.tolist()

　　②多重索引取值（df.index.get_level_values('列名')）
　　　　dfQuery.index.get_level_values('gpcode')

7、很重要的一步是把不符合正态分布的变量给转化成正态分布的（使用方法：np.log）
	#histogram and normal probability plot

	sns.distplot(df_train[ SalePrice ],fit=norm);
	fig=plt.figure
	res=stats.probplot(df_train[ SalePrice ],plot=plt)
	这个图里可以看到‘SalePrice’的分布是正偏度，在正偏度的情况下，用log取对数后可以做到转换：

	#aPPlying log transformation

	df_train[ SalePrice ]=np.log(df_train[ SalePrice ])
	同样，我们可以把其他不符合正态分布的变量进行转化，
	例如GrLivArea和目标值SalePrice在转化之前的关系图是类似锥形的：

	#scatter plot
	plt.scatter(df_train[ GrLivArea ],df_train[ SalePrice ]);
	在对GrLivArea转换后，
	#data transformation
	df_train[ GrLivArea ]=np.log(df_train[ GrLivArea ])


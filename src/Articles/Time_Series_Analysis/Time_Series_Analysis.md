# Time_Series_AirPassenger

## Contents

- import

import pandas as pd
import numpy as np
import matplotlib.pylab as plt
%matplotlib inline
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6

- Time

	1、read_csv 日期不是时间序列（转换）
	比如说我的csv中有一列是时间：1949-01-01，当我直接read_csv(fileName)时，得到的数据，
	它的时间这一列被当做 object（或者string）
	
	1）单列转换
	dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
	df = pd.read_csv(infile, parse_dates=['datetime'], date_parser=dateparse)
	这里注意：parse_dates=['datetime']，输入的类型是list，即有[]
	
	2）多列转换
	dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
	df = pd.read_csv(infile, parse_dates={'datetime': ['date', 'time']}, date_parser=dateparse)
	
	dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m')
	# dateparse('1962-01')
	data = pd.read_csv('AirPassengers.csv', parse_dates=['Month'], index_col='Month',date_parser=dateparse)
	print data.head()
	这里index_col=‘Month’是为了把这一列作为索引，然后print(data.index)就能看到DatetimeIndex等字样
	所以#convert to time series: ts = data['#Passengers']，这里不仅仅只有列#Passengers的值，还有Month索引值
	
	2、ts（何为时间序列：索引值为时间，y值为具体值）
	直接：plt.plot(ts)
	使用这样的函数即可
	def test_stationarity(timeseries):
    
		#Determing rolling statistics
		rolmean = pd.rolling_mean(timeseries, window=12)
		rolstd = pd.rolling_std(timeseries, window=12)

		#Plot rolling statistics:
		orig = plt.plot(timeseries, color='blue',label='Original')
		mean = plt.plot(rolmean, color='red', label='Rolling Mean')
		std = plt.plot(rolstd, color='black', label = 'Rolling Std')
		plt.legend(loc='best')
		plt.title('Rolling Mean & Standard Deviation')
		plt.show(block=False)
		
		#Perform Dickey-Fuller test:
		print 'Results of Dickey-Fuller Test:'
		dftest = adfuller(timeseries, autolag='AIC')
		dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
		for key,value in dftest[4].items():
			dfoutput['Critical Value (%s)'%key] = value
		print dfoutput
	
	3、Smoothing化 .rolling_mean
	moving_avg = pd.rolling_mean(ts_log,12)
	
	4、AR模型实例
	
	
	
	
	

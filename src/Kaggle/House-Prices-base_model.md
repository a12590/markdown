# Kaggle-House-Prices

## Contents

- model ensemble（预测房价回归预测）
1、根据Exploratory_data_analysis得到的结果信息，统一对数据进行处理

	# 单独处理：

	# 1、偏离点处理
	df_train=df_train.drop(df_train[df_train[ Id ]==524].index)

	# 2、对于占比例太大的变量，例如超过了15%，就看看它的含义，如果不是很重要，这种数据是可以删掉的。
	to_delete = total_missing[total_missing>(train.shape[0]/3.)]

	# 3、很重要的一步是把不符合正态分布的变量给转化成正态分布的（使用方法：np.log）
	train["SalePrice"] = np.log1p(train["SalePrice"])


	# 统一处理：

	# 1、偏离点处理
	def data_preprocess(train,test)
		outlier_idx = []
		train.drop(train.index[outlier_idx],inplace=True)

	# 2、Miss not important
	to_delete = ['Alley','FireplaceQu','PoolQC','Fence','MiscFeature']
    all_data = all_data.drop(to_delete,axis=1)

	# 3、log transform skewed numeric features（这种方法我还是觉得蛮奇怪的）
	numeric_feats = all_data.dtypes[all_data.dtypes != "object"].index
    skewed_feats = train[numeric_feats].apply(lambda x: skew(x.dropna())) #compute skewness
    skewed_feats = skewed_feats[skewed_feats > 0.75]
    skewed_feats = skewed_feats.index
    all_data[skewed_feats] = np.log1p(all_data[skewed_feats])
    all_data = pd.get_dummies(all_data)
    all_data = all_data.fillna(all_data.mean())

2、调用不同的model算法得到预测值比较

	# 抽出统一的函数

	# 结果保存文件
	# param1：prediction（y预测值）
	# param2：score（仅作为名字以供比较）
	# output：{'Id': test['Id'].values, 'SalePrice': prediction}

	create_submission(prediction,score):
	now = datetime.datetime.now()
    sub_file = 'submission_'+str(score)+'_'+str(now.strftime("%Y-%m-%d-%H-%M"))+'.csv'
    print ('Creating submission: ', sub_file)
    pd.DataFrame({'Id': test['Id'].values, 'SalePrice': prediction}).to_csv(sub_file, index=False)

	# 模型

	#sklearn为我们提供专门调试参数的函数grid_search,建立分类器clf时，调用GridSearchCV()函数，
	#
	#将上述参数列表的变量传入函数。并且可传入交叉验证cv参数，
	#设置为5折交叉验证。对训练集训练完成后调用best_params_变量，打印出训练的最佳参数组。
	#构建模型，model = GridSearchCV(estimator=。。。, param_grid=param_grid, n_jobs=1, cv=10, scoring=RMSE)
	#model.fit训练模型，之后model.best_params_，-model.best_score_打印
	#pred = model.predict(Xtest)

	#在scikit-learn中，RF的分类类是RandomForestClassifier，回归类是RandomForestRegressor。
	#当然RF的变种Extra Trees也有， 分类类ExtraTreesClassifier，回归类ExtraTreesRegressor。
	#scikit-learn 梯度提升树(GBDT)


	# model_random_forecast /RF：RandomForestRegressor
	rfr = RandomForestRegressor(n_jobs=1, random_state=0) ======> estimator=rfr
	param_grid = {}#'n_estimators': [500], 'max_features': [10,15,20,25], 'max_depth':[3,5,7,9,11]}

	# model_xgb_regression /xgboost XGB：XGBRegressor
	xgbreg = xgb.XGBRegressor(seed=0) ======> estimator=xgbreg
    param_grid = {
	#        'n_estimators': [500],
	#        'learning_rate': [ 0.05],
	#        'max_depth': [ 7, 9, 11],
	#        'subsample': [ 0.8],
	#        'colsample_bytree': [0.75,0.8,0.85],
    }

	# model_extra_trees_regression /Extra：ExtraTreesRegressor
	etr = ExtraTreesRegressor(n_jobs=1, random_state=0)  ======> estimator=etr
    param_grid = {}#'n_estimators': [500], 'max_features': [10,15,20]}

	# model_gradient_boosting_tree /GBDT：GradientBoostingRegressor
	gbr = GradientBoostingRegressor(random_state=0)  ======> estimator=gbr
    param_grid = {
	 #       'n_estimators': [500],
	 #       'max_features': [10,15],
	 #	     'max_depth': [6,8,10],
	 #       'learning_rate': [0.05,0.1,0.15],
	 #       'subsample': [0.8]
    }

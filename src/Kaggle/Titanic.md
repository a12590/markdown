##  Kaggle的Titanic数据分析##

## Contents

**特征分析与选择**
**特征工程1**
一般方法：
1、 读取训练集和测试集为 DataFrame；
2、 训练集数据
（head查看）
（info可以看到有缺失值的列）
（describe，mean字段等查看具体数据数值）
3、 数据清洗
（drop去除 PassengerId、Name、Ticket 字段的值+head查看结果）
4、 训练数据存在空数据
（同理 .isnull().head()）

**** 分析 Embarked 特征对 Survived 的影响 ****

1、数据缺失值处理：
将 Embarked 缺失的数据填充为最多的值 S（`print train_data['Embarked'].max() => S`）（`.fillna('S')`）
2、`.factorplot` 分析得到的是Embarked 和Survived 之间的关系（默认是折现图）。
（kind参数转化为 bar 柱形图 col 多维度关系图。size, aspect 指定绘制图像的大小）

**补充：matplotlib 绘图库的简单用法**
```
// plt.figure() 生成空窗：不能通过空Figure绘图，必须用add_subplot创建一个或多个subplot才行。
plt.figure().add_subplot(2,2,1)

// 以上语句生成AxeSubplot对象，直接调用可以绘图
ax.plot( randn(1000).cumsum() )

//　绘制xticks的简单线型图
// 刻度的位置和跟刻度一致，替换为文字，文字的属性在后面关键字中显示）
ax.set_xticks、ax.set_xticklabels
// 再用set_xlabel为x轴设置一个名称，并用set_title设置一个标题
ax.set_title 、ax.set_xlabel

// subplot对象
fig,axes = plt.subplots(2,3)可以直接生成fig axes（可以一下子产生2x3个子窗口，并且以numpy数组的方式保存在axes，通过对axes进行索引来访问每个子窗口）
axes.hist( randn(500), bins = 50,color = 'k',alpha = 0.5 )（这样可以绘制直方图）
plt. subplots_adjust( wspace = 0, hspace = 0 ) （调整图像边框，使得各个图之间的间距为0 ）

=====================================

// 在默认情况下，linspace函数可以生成元素为50的等间隔数列
x=np.linspace(0,10,1000)
// 显示图示
plt.legend()
// 画点图
plt.scatter(X1,X2, marker = 'o')
// 画三维图
x,y,z = m['ydra'],m['zyd'],m['rs12612420']
ax=plt.subplot(111,projection='3d')
//创建一个三维的绘图工程
ax.scatter(x[:],y[:],z[:],c='r')
//将数据点分成三部分画，在颜色上有区分度
plt.scatter(y,z, marker = 'o')

// 散点柱状图
//在带状图中，散点图通常会重叠。这使得很难看到数据的完全分布
sns.stripplot(x="day", y="total_bill", data=tips)
sns.set(style="whitegrid", color_codes=True)
np.random.seed(sum(map(ord, "categorical")))
```

```
// x,y hue(指定分析的红黑蓝多类的那一列) order（x轴列具体命名）
柱状(带黑条)
sns.barplot(x="sex", y="survived", hue="class", data=titanic);
柱状(不带黑条)
sns.countplot(x="deck", data=titanic, palette="Greens_d");
```

**** 分析 Fare 特征对 Survived 的影响**

```
1、查看和简单处理
（head describe）
空值填充
（.fillna(test_df["Fare"].median(),inplace=True)）
数据处理转换
（.astype(int)）

2、数据划分：分别得到Fare变量对应的幸存和没有幸存的记录，
（这种引用很像R语言中的which()函数）

fare_not_survived =
titanic_df["Fare"][titanic_df["Survived"] == 0]

fare_survived     =
titanic_df["Fare"][titanic_df["Survived"] == 1]

3.作图：
1、mean std

2、hist作为函数，也可以作为 kind="hist" 画频率直方图（y:Frequency）

3、titanic_df['Fare'].plot(kind='hist', figsize=(10,3),bins=100, xlim=(0,50))

注：直接调用plot()也是一种简单画图方法，与matplotlib.pyplot中面向对象画图一样

```
 **** 分析 Age 特征对 Survived 的影响 ****

```
1、查看和简单处理

（isnull.head）

对于缺失数据：age，将其填充为高斯分布（mean，std满足训练集分布）的随机值。

np.random.randint()：均值-方差，均值+方差，空值

赋值给
titanic_df["Age"][np.isnan(titanic_df["Age"])])

或者赋值给
titanic_df["Age"][titanic_df["Age"].isnull()]）

数据处理转换（.astype(int)）

.hist(bins=70, ax=axis1)作图得到结果

.dropna()是直接不经过填充，直接去除数据的方式
```

**补充：作图：seaborn的FaceGrid()方法**

```
// peaks for survived/not survived passengers by their age， aspect设置绘图的大小

facet =
sns.FacetGrid(train_data, hue="Survived",aspect=4)

// 拟合和绘制一元或二元概率密度分布
facet.map(sns.kdeplot,'Age',shade= True)
facet.set(xlim=(0, train_data['Age'].max()))
facet.add_legend()

// average survived passengers by age（每个年龄的存活率：）

fig, axis1 = plt.subplots(1,1,figsize=(18,4))

average_age =
train_data[["Age", "Survived"]].groupby(['Age'], as_index=False).mean()

sns.barplot(x='Age', y='Survived', data=average_age)

---seaborn简介和实例

palette 调色板 hue 选择分类列
1  set_style()  set()
set_style()是用来设置主题的，Seaborn有五个预设好的主题： darkgrid , whitegrid , dark , white ,和 ticks  默认： darkgrid
2  distplot()  kdeplot()
distplot()为hist加强版，kdeplot()为密度曲线图
3  箱型图 boxplot()
4  联合分布jointplot()
5  热点图heatmap()
6  pairplot()
7  FacetGrid()
```

 **** 分析 Cabin 特征对 Survived 的影响 ****

```
1、查看和简单处理

titanic_df.shape titanic_df.Cabin.count()

测试发现 Cabin 字段存在过多的 NaN 缺失数据，所以考虑将 Cabin 字段删除：.drop('', axis=1, inplace=True)

查看缺失与否方法二：train_data.ix[train_data['SibSp'].isnull()].shape

```

**组合变量（产生和操作）**
```

titanic_df.SibSp[titanic_df.SibSp!=0].count()
可以发现，两者只有极少数不是0值
故Parch 和 SibSp 特征组合成 Family 特征
titanic_df['Family'] =
titanic_df["Parch"] + titanic_df["SibSp"]
```

作图：

```
sns.countplot(x='Survived', hue='Family', data=train_data, ax=axis2, order=[1,0])

重要：分析时查看1，0结果的分布情况。相同，则说明没太大关联，反之，则有
```

** 整合变量Sex：按照 Age 和 Sex 组合分类为 Person 类别 **

```
1、组合
对于Age 和 Sex的两列得到child and sex（两种）的一列Person（共三种类别）（return 'child' if age < 16 else sex））

2、绘图展示average of survived for each Person(male, female, or child

fig, (axis1, axis2) = plt.subplots(1,2, figsize=(10,5))（figsize（10:5的比例））

方法：mean函数，对Person和survived两列按照Person聚类，sns.barplot将聚类后均值输出，order指明列名

```

**====数据探索结束======**

**模型构建**

**** Feature Scaling 对 Age 、 Fare 数据进行 Feature Scaling 处理。 ****

```
方法：
from sklearn import preprocessing
.StandardScaler() .fit .transform
```

**** 数据的特征选择及向量化 ****

```
// 对数据集进行向量化等处理
// 提取训练集特征和结果
// 将train和test的变量化为统一：
X_train = train_data.drop(['Survived', 'Name'],axis=1)
Y_train = train_data['Survived']
X_test  = test_data.drop(['PassengerId', 'Name'],axis=1)

// 将特征进行向量化处理

方法：
from sklearn.feature_extraction import DictVectorizer
dict_vec = DictVectorizer(sparse=False)
X_train = dict_vec.fit_transform(X_train.to_dict(orient='record'))
```

**** sklearn Random Forests 和 xgboost ****

```
//  对于 Logistic Regression 回归，分析各特征对 survived 为 1 的打分值

//　用逻辑回归去拟合X_train和Y_train，然后用logreg.predict()函数去预测X_test的数据，最后用拟合的结果去给模型打分！

logreg = LogisticRegression()
logreg.fit(X_train, Y_train)
Y_pred = logreg.predict(X_test)

logreg.score(X_train, Y_train)

// 使用逻辑回归获得每个特征的相关系数
coeff_df = DataFrame(train_data.columns.delete(0))
coeff_df.columns = ['Features']
coeff_df["Coefficient Estimate"] = pd.Series(logreg.coef_[0])
```

```
// 随机森林
// n_estimators： The number of trees in the forest.
random_forest = RandomForestClassifier(n_estimators=200)
// 随机森林分类
random_forest.fit(X_train, Y_train)
// 预测分类的类别
Y_predict_random_forest = random_forest.predict(X_test)
// 预测分类的类别的概率
Y_predict_proba = random_forest.predict_proba(X_test)
```

```
// XGBClassifier

from xgboost import XGBClassifier
xgbc = XGBClassifier(n_estimators=500)

// 使用5折交叉验证的方法在训练集上分别对 random_forest 和 XGBClassifier的分类性能进行评估，获取平均分类准确度的得分

方法：
from sklearn.cross_validation import cross_val_score
cross_val_score(random_forest, X_train, Y_train, cv=5).mean()
cross_val_score(xgbc, X_train, Y_train, cv=5).mean()

// XGBClassifier 分类

xgbc.fit(X_train, Y_train)
Y_predict_random_xgbc = xgbc.predict(X_test)
```

```
//总的，对应以上的算法 生成csv，提交文件 **
//先构造一个数据框DataFrame，再将其写成一个csv文件。
submission = pd.DataFrame({
        "PassengerId": test_df["PassengerId"],
        "Survived": （这里写的是预测得到结果）
    })
submission.to_csv('titanic.csv', index=False)
```

```
//各个分类器的对比使用：（GradientBoostingClassifier，LogisticRegression，AdaBoostClassifier，RandomForestClassifier，XGBClassifier，VotingClassifier）

先通过cross_validation.ShuffleSplit生成一个CV迭代策略生成器cv，然后将cv以参数的形式传递到cross_val_score中。
对数据集进行from sklearn.model_selection import ShuffleSplit
出对比效果：使用交叉验证 cross_val_score

使用示例：
// GradientBoostingClassifier
gbc = GradientBoostingClassifier(n_estimators=100)
cv = ShuffleSplit(n_splits=10, test_size=0.3, random_state=50)

// 对各个模型进行交叉验证
gbc.fit(X_train, Y_train)
scores = cross_val_score(gbc, X_train, Y_train, scoring='f1',cv=cv)
print 'GradientBoostingClassifier:', scores.mean()
```

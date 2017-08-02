# Spark_movie

## 1. program_structure

* dataset->data_model 

* engine -> A movie recommendation engine
```
> 定义函数get_counts_and_averages，Given a tuple (movieID, ratings_iterable)，returns (movieID, (ratings_count, ratings_avg))
`count` len
`averages` float(sum(x for x in A[1]))/count

> 定义函数__count_and_average_ratings，Updates the movies ratings counts from the current data self.ratings_RDD
`map`-> tuple (movieID, ratings_iterable):ratings_RDD.map(lambda x: (x[1], x[2])).groupByKey()
`map`-> map(lambda x: (x[0], x[1][0]))

```

* webapp_flask_app



## 2.spark MLlib recommendation / ALS、MatrixFactorizationModel 

*  __train_model
```
加载model
> MatrixFactorizationModel.load(sc, "als_model.data")
训练模型
> Train the model
rank = 8
seed = 5L
iterations = 10
regularization_parameter = 0.1
> ALS.train(ratings_RDD, rank, seed,iterations, lambda_=regularization_parameter)
  model.save(sc,"als_model.data")
```

*  __predict_ratings
```
预测,Gets predictions for a given (userID, movieID) formatted RDD,
Returns: an RDD with format (movieTitle, movieRating, numRatings)
> model.predictAll(user_and_movie_RDD).map(lambda x: (x.product, x.rating))
.join(movies_titles_RDD).join(movies_rating_counts_RDD)
.map(lambda r: (r[1][0][1], r[1][0][0], r[1][1]))

> Recommends up to movies_count top unrated movies to user_id
# Get pairs of (userID, movieID) for user_id unrated movies//
movies_RDD.filter(lambda rating: not rating[1]==user_id).map(lambda x: (user_id, x[0]))
__predict_ratings(user_unrated_movies_RDD).filter(lambda r: r[2]>=25).takeOrdered(movies_count, key=lambda x: -x[1])

```

## 3.__init__

```
# Load ratings data for later use
> ratings_file_path = os.path.join(dataset_path, 'ratings.csv')
sc.textFile(ratings_file_path).map(lambda line:json.loads(line))
.map(lambda tokens: (int(tokens["user_id"]),int(tokens["movie_id"]),float(tokens["rate_score"]))).cache()

```

## 4.webapp_flask_app
```
> recommend
.list.array.dict .append
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.debug("User %s rating requested for movie %s", user_id, movie_id)
返回：json.dumps(ratings)
> users
from flask.ext.paginate import Pagination
1、分页
def get_page_items():
    page = int(request.args.get('page', 1)) 
    per_page = request.args.get('per_page')
    if not per_page:
        per_page = current_app.config.get('PER_PAGE', 10)
    else:
        per_page = int(per_page)

    offset = (page - 1) * per_page
    return page, per_page, offset

pagination = Pagination(page=page,per_page=per_page,total=total
,css_framework='bootstrap3',record_name="users_info")
2、config思想
3、
from flask.ext.wtf import Form
from wtforms import IntegerField,StringField, SubmitField,RadioField
from wtforms.validators import Required, Length, Email, Regexp
from wtforms import ValidationError
表格验证，这个可以直接拿来用
4、blueprint
```

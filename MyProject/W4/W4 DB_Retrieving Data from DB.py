from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

target_movie = db.movies.find_one({'title':'어벤져스: 엔드게임'})
target_star = target_movie['star']

sameStars = list(db.movies.find({'star': target_star}))
for movie in sameStars:
    print(movie['title'])


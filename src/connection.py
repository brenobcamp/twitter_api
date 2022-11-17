import pymongo as pyM


client = pyM.MongoClient()

db = client.testing_tweepy
tweets_collection = db.tweets

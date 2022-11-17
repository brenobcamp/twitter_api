import tweepy
from src.secrets import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
from pprint import pprint
from typing import List, Dict, Any
from src.connection import tweets_collection

def _get_timeline() -> List[Dict[str, Any]]:
    """
        Getting most recents tweets of your timeline
    """
    auth = tweepy.Client(
        consumer_key=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET
    )


    public_tweets = auth.get_home_timeline()
    return [tweets for tweets in public_tweets]

def get_tweets_from_mongo() -> List[Dict[str, Any]]:
    
    tweets = tweets_collection.find({})

    return list(tweets)

def save_tweets() -> None:
    timeline = _get_timeline()
    timeline_data = timeline[-1]
    tweets_collection.insert_one(timeline_data)

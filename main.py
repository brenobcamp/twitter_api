import uvicorn
from fastapi import FastAPI
from src.services import get_tweets_from_mongo, save_tweets
from typing import List
from src.responses import Timeline


app = FastAPI()


@app.get('/get', response_model=List[Timeline])
def get_tweets():
    return get_tweets_from_mongo()


if __name__ == '__main__':
    timeline = get_tweets_from_mongo()
    if not timeline:
        save_tweets()

    uvicorn.run(app, host='0.0.0.0', port=8000)


from fastapi import FastAPI
from scrape import ESPN

app = FastAPI()

@app.get('/')
def welcome():
    return 'current calls: /espn'

@app.get('/espn')
def espn_top_news():
    data = ESPN().get_top_news()
    return {'data':data}

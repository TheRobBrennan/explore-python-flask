from flask import Flask
import requests

app = Flask(__name__)

API_URL = 'https://financialmodelingprep.com/api/v3/stock/real-time-price/{ticker}'
API_KEY = 'demo'


def fetch_price(ticker):
    data = requests.get(API_URL.format(ticker=ticker.upper()),
                        params={'apikey': API_KEY}).json()
    return data["price"]

# http://localhost:5000/stock/AAPL


@app.route('/stocks/<ticker>')
def stock(ticker):
    price = fetch_price(ticker)
    return "The price of {ticker} is {price}".format(ticker=ticker, price=price)


@app.route('/')
def home_page():
    return 'This is the home page. Please try going to /stocks/AAPL'

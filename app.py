# Example Python backend structure
import requests
from flask import Flask, jsonify
import yfinance as yf  # Yahoo Finance API
import alpha_vantage    # Alpha Vantage API


app = Flask(__name__)

@app.route('/api/stock/<symbol>')
def get_stock_price(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period="1d")
    return jsonify({
        'price': data['Close'].iloc[-1],
        'change': data['Close'].iloc[-1] - data['Open'].iloc[0]
    })
from flask import (
    Flask,
    jsonify,
    g,
    redirect,
    render_template,
    request,
    session,
    flash,
    url_for, Response
)
import ta
import numpy
import talib
from numpy import genfromtxt
import websocket,json
import json
from binance.enums import *
import talib
from binance.client import Client
import config,csv
app = Flask(__name__)
app.config.update(
    TESTING=True,
    SECRET_KEY=b'_5#y2L"F4Q8z\n\xec]/'
)

class Wallet:
    key=''
    secret=''
    def set_credentials(self,api_key,api_secret):
        self.key=api_key
        self.secret=api_secret

    def get_credentials(self):
        return self.key,self.secret


w=Wallet()


@app.route('/')
def index():
    title="Main"


    return render_template('index.html',title=title)


@app.route('/binance')
def binance():


    key,secret=w.get_credentials()
    if (key==""):
        return redirect('/')
    print(key)
    print(secret)
    client = Client(key,secret)

    title="Main"
    account=client.get_account()
    balances=account['balances']
    print(balances)
    balance_tuple_list=[]
    for balance in balances:
        if(balance['free']!='0.00000000' and balance['free']!='0.00' ):
            val=(balance['asset'],balance['free'])
            balance_tuple_list.append(val)

    sorted_balance = sorted(balance_tuple_list, key=lambda tup: tup[1],reverse=True)

    exchange_info=client.get_exchange_info()
    #print('/n')
    #print('/n')
    #print(json.dumps(exchange_info,indent=1))
    symbols=exchange_info['symbols']


    return render_template('main.html',title=title,symbols=symbols,balancetpl=sorted_balance )

@app.route('/buy',methods=['POST'])
def buy():
    key, secret = w.get_credentials()
    client = Client(key, secret)
    print (request.form['symbol'])
    try:
        order = client.create_order(
        symbol=request.form['symbol'],
        side=SIDE_BUY,
        type=ORDER_TYPE_MARKET,
        quantity=request.form['quantity'])
        flash("Succesfully Bought!")



    except Exception as e:
        val=str(e)
        flash(val[21:])



    return redirect('/binance')

@app.route('/sell',methods=['POST'])
def sell():
    key, secret = w.get_credentials()
    client = Client(key, secret)
    print(request.form['symbol'])
    try:
        order = client.create_order(
            symbol=request.form['symbol'],
            side=SIDE_SELL,
            type=ORDER_TYPE_MARKET,
            quantity=request.form['quantity'])
        flash("Succesfully Sold!")

    except Exception as e:
        val = str(e)
        flash(val[21:])

    return redirect('/binance')

@app.route('/setting')
def settings():
    return "setting"

@app.route('/connect',methods=['POST'])
def connect():
    w.set_credentials(request.form['key'],request.form['secret'])

    return redirect("/binance")


@app.route('/history')
def history():
    key, secret = w.get_credentials()
    client = Client(key, secret)
    candlestick=client.get_historical_klines("BTCUSDT",Client.KLINE_INTERVAL_5MINUTE,"1 June, 2021","12 June, 2021")

    pc=[]
    for c in candlestick:
        c_stick={
            "time":c[0],
            "open":c[1],
            "high":c[2],
            "low":c[3],
            "close":c[4]

            }
        pc.append(c_stick)


    return jsonify(pc)

@app.route('/rsi')
def rsi():
    #print(ta.ws.run_forever())

    return "SS"











if __name__ == '__main__':
    app.run()

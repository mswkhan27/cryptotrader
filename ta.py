import numpy
import talib
from numpy import genfromtxt
import websocket,json

#my_data=genfromtxt("15minutes.csv",delimiter=",")
#close=my_data[:,4]
#print(close)

#rsi=talib.RSI(close)
#print(rsi)
#close=numpy.random.random(100)
#print(close)
#moving_avg=talib.SMA(close,10)
#rsi=talib.SMA(close)
#print(rsi)

cc = 'btcusd'

socket = 'wss://stream.binance.com:9443/ws/btcusdt@kline_5m'
va = []


def on_message(ws, message):
    json_msg = json.loads(message)
    data = json_msg['k']
    close = data['c']
    va.append(float(close))

    arr = numpy.array(va)
    rsi = talib.RSI(arr)

    # a = numpy.append(a, data['c'])
    rsi = rsi[numpy.logical_not(numpy.isnan(rsi))]
    print ( str(rsi[-1]))


def on_close(ws):
    print("closed")


ws = websocket.WebSocketApp(socket, on_message=on_message, on_close=on_close)



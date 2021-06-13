from binance.client import Client
import config,csv
import json

client=Client(config.API_KEY,config.API_SECRET)
prices=client.get_all_tickers()
exchange_info = client.get_exchange_info()
print('/n')
print('/n')

symbols=exchange_info
print(json.dumps(symbols, indent=1))

#for price in prices:
#    print(price['price'])


#candles=client.get_klines(symbol="BTCUSDT",interval=Client.KLINE_INTERVAL_15MINUTE)
#klines = client.get_historical_klines("BNBBTC", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2021","12 June, 2021")

#csvfile= open('daily.csv', 'w', newline='')
#candlestick_writer = csv.writer(csvfile, delimiter=',')

#for candlestick in klines:
#    print(candlestick)
#    candlestick_writer.writerow(candlestick)

#csvfile.close()



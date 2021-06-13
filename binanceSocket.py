import time

from binance import ThreadedWebsocketManager

api_key = '6K1I003QwWknFtEn2qiRGe7LjLoPMqCwy7KG8pkWEVy3FBT4KEoEDjeBUlIj4LmX'
api_secret = 'somEcPQIbzcdw0h3fyWsOnUWh0dVTMdHIn7vU16hZHFjFeACVYlDrF1I6fewLdac'

def main():

    symbol = 'BTCUSDT'

    twm = ThreadedWebsocketManager(api_key=api_key, api_secret=api_secret)
    # start is required to initialise its internal loop
    twm.start()

    def handle_socket_message(msg):
        print(f"message type: {msg['e']}")
        print(msg)

    twm.start_kline_socket(callback=handle_socket_message, symbol=symbol)



    twm.join()



print (main())
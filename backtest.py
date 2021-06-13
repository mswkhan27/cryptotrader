import backtrader as bt
cerebro=bt.Cerebro()


data=bt.feeds.GenericCSVData(dataname='daily.csv',dtformat=1)
cerebro.adddata(data)
cerebro.run()
cerebro.plot()

Demo Link: https://www.youtube.com/watch?v=H2sy69L2B_g

## Introduction

Cryptocurrency is probably the hottest trend in the world right now but still not many people
really understand the concept behind the currencies and how the trading works. The
confusion can be costly since you need an understanding about how the trading works and
what time is suitable for any certain action. Right now, there are platforms like Binance,
OKEX and Coinbase where the user can decide to buy or sell depending upon the current
position and price along with some other indicators for the currency. As most of the
consumers don’t really understand the nitty gritty details to make a decision, we tried to
develop a trader which uses RSI indicator to help users in making their decisions easily.

## Implementation

Initially, we built a website with real time trading functionality where users can easily
purchase and sell cryptocurrencies.

## Structure

While building the website, we used flask as the backend to cater the users and their
accounts. For frontend, we used HTML, CSS, Bootstrap and JS to build functional and
pleasing UI for our website.

## Binance API

In order to incorporate real time trading, we used Binance API to implement the functionality
along with getting wallet details for the trader. Initially, API key and API Secret are required
for the exchange information and accessing the wallet. After that, we integrated a Web Socket
in order to get closing prices for the currencies in different timeframes, all of which intervals
are mentioned on Binance. Later, we added the buy and sell option for the currencies using
the API where users can view the current balance of cryptocurrencies they hold along.

## RSI Indicator

Finally, we included the RSI indicator in order to help users understand the right time to buy
or sell the currency depending upon its overbought and oversold conditions. The RSI
indicator is really helpful since it shows the currency’s actual value against its true value
hence allowing the trader to make a decision. By using this, the trader can enter and leave the
market at an appropriate time which can be really beneficial. We took the RSI Indicator from a publicly available API of https://taapi.io/

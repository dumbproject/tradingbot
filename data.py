# code stolen from NeuralNine on youtube
# https://www.youtube.com/watch?v=FEDBsbTFG1o

# get necessary tools necessary tools for:
# the current date, graph, and market info
import datetime as dt
import matplotlib.pyplot as plt
import pandas_datareader as web


#                these are our variables:
# 
##################################################################
########## IMPORTANT: THESE ARE THE ADJUSTABLE VARIABLES #########
##################################################################
# set the two moving averages to whatever you choose             #
ma_1 = 10                                                        #
ma_2 = 30                                                        #
# set the dates for when to collect past data                    #
# (x amount of days ago, until the current date)                 #
start = dt.datetime.now() - dt.timedelta(days=365 * 1)           #
end = dt.datetime.now()                                          #
# market data for a stock/crypto, on a market, from start to end #
data = web.DataReader('DOGE-USD', 'yahoo', start, end)           #
##################################################################
##################################################################
# adding data for the two moving averages
data[f'SMA_{ma_1}'] = data['Adj Close'].rolling(window=ma_1).mean()
data[f'SMA_{ma_2}'] = data['Adj Close'].rolling(window=ma_2).mean()
data = data.iloc[ma_2:]
# buy and sell triggers
buy_stock = False
sell_stock = False
# every time a buy or sell is made,
# the price is added to these arrays
buy_signals = []
sell_signals = []
# this is the amount we start with,
# which changes along with our current balance
wallet = 100
# the price of the last transaction
last_buy = 0
last_sell = 0
# data collected for backtesting:
# the amount of dollars and crypto in the transaction,
# and the price of the dollar or crypto at that time
dollaramount = []
cryptoamount = []
dollarprice = []
cryptoprice = []



# tell the console we're starting with { this } amount
print('\n', 'STARTING AMOUNT: $', wallet, '\n')



# for every datapoint within the time range of the dates we specified earlier:
for x in range(len(data)):
    # if the shorter moving average is greater than the longer moving average,
    # and we SHOULD buy stock,
    # buy
    if data[f'SMA_{ma_1}'].iloc[x] > data[f'SMA_{ma_2}'].iloc[x] and buy_stock != True:
    # if data[f'SMA_{ma_1}'].iloc[x] > data[f'SMA_{ma_2}'].iloc[x] and buy_stock == True:
        # change triggers accordingly
        buy_stock = True
        sell_stock = False

        # add price to data
        buy_signals.append(data['Adj Close'].iloc[x])
        sell_signals.append(float('nan'))


        wallet = wallet / data['Adj Close'].iloc[x]
        # print('buy transaction: ', wallet, ' = ', wallet, ' / ', data['Adj Close'].iloc[x])
        last_buy = data['Adj Close'].iloc[x]
        # print('last buy:  ', last_buy)

        cryptoamount.append(wallet)
        cryptoprice.append(data['Adj Close'].iloc[x])
    # if the shorter moving average is greater than the longer moving average,
    # and we SHOULD sell stock,
    # sell
    elif data[f'SMA_{ma_1}'].iloc[x] < data[f'SMA_{ma_2}'].iloc[x] and sell_stock != True and last_buy < data['Adj Close'].iloc[x]:
        # change triggers accordingly
        buy_stock = False
        sell_stock = True

        # add price to data
        sell_signals.append(data['Adj Close'].iloc[x])
        buy_signals.append(float('nan'))

        wallet = wallet * data['Adj Close'].iloc[x]
        # print('sell transaction: ', wallet, ' = ', wallet, ' * ', data['Adj Close'].iloc[x])
        last_sell = data['Adj Close'].iloc[x]
        # print('last sell: ', last_sell)

        dollaramount.append(wallet)
        dollarprice.append(data['Adj Close'].iloc[x])
    # if neither of these things are true, do nothing
    # (fill collected data with a NotANumber value)
    else:
        buy_signals.append(float('nan'))
        sell_signals.append(float('nan'))


# add data to buy and sell signals, 
# print data
data['Buy Signals'] = buy_signals
data['Sell Signals'] = sell_signals
print(data, '\n')
# print('\n')



# print the collected data of crypto purchased and estimated return in dollars
for x in range(len(cryptoamount)):
    print('CRYPTO PURCHASED: ', '{:,}'.format(round(cryptoamount[x], 4)), ' AT PRICE OF ', round(cryptoprice[x], 4))
print('\n')
for y in range(len(dollaramount)):
    print('RETURN AMOUNT: $$$', '{:,}'.format(round(dollaramount[y], 2)), ' AT PRICE OF ', round(dollarprice[y], 4))
print('\n')



# plot data on a graph
plt.style.use("dark_background")
plt.plot(data['Adj Close'], label="Share Price", alpha=0.5)
plt.plot(data[f'SMA_{ma_1}'], label=f"SMA_{ma_1}", color="orange", linestyle="--")
plt.plot(data[f'SMA_{ma_2}'], label=f"SMA_{ma_2}", color="pink", linestyle="--")
plt.scatter(data.index, data['Buy Signals'], label="Buy Signal", marker="^", color="#00ff00", lw=3)
plt.scatter(data.index, data['Sell Signals'], label="Sell Signal", marker="v", color="#ff0000", lw=3)
plt.legend(loc="upper left")
plt.show()

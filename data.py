import datetime as dt
import matplotlib.pyplot as plt
import pandas_datareader as web

plt.style.use("dark_background")

ma_1 = 10
ma_2 = 30

start = dt.datetime.now() - dt.timedelta(days=365 * 1)
end = dt.datetime.now()

data = web.DataReader('DOGE-USD', 'yahoo', start, end)
data[f'SMA_{ma_1}'] = data['Adj Close'].rolling(window=ma_1).mean()
data[f'SMA_{ma_2}'] = data['Adj Close'].rolling(window=ma_2).mean()

data = data.iloc[ma_2:]

# plt.plot(data['Adj Close'], label="Share Price", color="lightgray")
# plt.plot(data[f'SMA_{ma_1}'], label=f"SMA_{ma_1}", color="orange")
# plt.plot(data[f'SMA_{ma_2}'], label=f"SMA_{ma_2}", color="purple")
# plt.legend(loc="upper left")
# plt.show()

buy_signals = []
sell_signals = []
trigger = 0



starting = 100
# currentprice = []
dollaramount = []
cryptoamount = []
print("\n", "STARTING AMOUNT: ", starting)


for x in range(len(data)):
    if data[f'SMA_{ma_1}'].iloc[x] > data[f'SMA_{ma_2}'].iloc[x] and trigger != 1:
        buy_signals.append(data['Adj Close'].iloc[x])
        sell_signals.append(float('nan'))
        trigger = 1
        starting = starting / data['Adj Close'].iloc[x]
        cryptoamount.append(starting)
        # currentprice.append(data['Adj Close'].iloc[x])
    elif data[f'SMA_{ma_1}'].iloc[x] < data[f'SMA_{ma_2}'].iloc[x] and trigger != -1:
        sell_signals.append(data['Adj Close'].iloc[x])
        buy_signals.append(float('nan'))
        trigger = -1
        starting = starting * data['Adj Close'].iloc[x]
        dollaramount.append(starting)
    else:
        buy_signals.append(float('nan'))
        sell_signals.append(float('nan'))

data['Buy Signals'] = buy_signals
data['Sell Signals'] = sell_signals

print(data, '\n')
for x in cryptoamount:
    print('CRYPTO PURCHASED: ', x)
print('\n')
for y in dollaramount:
    print('RETURN AMOUNT $$: ', y)
print('\n')

plt.plot(data['Adj Close'], label="Share Price", alpha=0.5)
plt.plot(data[f'SMA_{ma_1}'], label=f"SMA_{ma_1}", color="orange", linestyle="--")
plt.plot(data[f'SMA_{ma_2}'], label=f"SMA_{ma_2}", color="pink", linestyle="--")
plt.scatter(data.index, data['Buy Signals'], label="Buy Signal", marker="^", color="#00ff00", lw=3)
plt.scatter(data.index, data['Sell Signals'], label="Sell Signal", marker="v", color="#ff0000", lw=3)
plt.legend(loc="upper left")
plt.show()

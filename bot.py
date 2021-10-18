import cbpro

data = open('passphrase', 'r').read().splitlines()

public = data[0]
passphrase = data[1]
secret = data[2]

auth_client = cbpro.AuthenticatedClient(public, secret, passphrase)

# print(auth_client)
print(auth_client.get_accounts())

# print(auth_client.buy(price="10.0", size="0.1", order_type="limit", product_id="ETH-USD"))
# print(auth_client.buy(size="10", order_type="market", product_id="ETH-USD"))

# print(auth_client.sell(price="10.0", size="0.1", order_type="limit", product_id="ETH-USD"))
# print(auth_client.sell(size="10", order_type="market", product_id="ETH-USD"))

# auth_client.place_limit_order(product_id="BTC-USD", side="buy", price="10.00", size="2")

# print(auth_client.cancel_all(product_id="BTC-USD"))
# print(auth_client.get_orders())




# import time

# sell_price = 30000
# sell_amount = 0.3

# buy_price = 25000
# buy_amount = 0.2

# while True:
#     price = float(auth_client.get_product_ticker(product_id="BTC-USD")['price'])
#     if price <= buy_price:
#         print(f"Buying BTC-USD because price of {price:,} fell below buying price limit of {buy_price}")
#         # print("Buying BTC")
#         auth_client.buy(size=buy_amount, order_type="market", product_id="BTC-USD")
#     elif price >= sell_price:
#         print(f"Selling BTC-USD because price of {price:,} rose above selling price limit of {sell_price}")
#         # print("Selling BTC")
#         auth_client.sell(size=sell_amount, order_type="market", product_id="BTC-USD")
#     else:
#         print(f"Not doing anything! Price is {price:,}!")
#         # print("Nothing...")
#     time.sleep(10)








# public_client = cbpro.PublicClient()

# eth_trades = public_client.get_product_trades('ETH-USD')
# print(next(eth_trades))
# print(next(eth_trades))
# print(next(eth_trades))
# print(next(eth_trades))
# print(next(eth_trades))

# # result = public_client.get_products()
# # result = public_client.get_currencies()
# # for row in result:
# #     print(row['id'])

# # result = public_client.get_time()
# # print(result)

# result = public_client.get_product_24hr_stats()

# result = public_client.get_product_order_book('BTC-USD')
# print(result)


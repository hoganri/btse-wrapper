import requests, json

# BTSE API Wrapper
# Start building or migrate your trading
# algorithms to the BTSE platform
#
# Tipjar: bc1q3taedwlg6955eda6e40k7uaxrvfmtrx9apjsw3
# Referral URL: https://www.btse.com/en/home?ref=7MnXDG

# ****************************************** #
#
# AUTHENTICATED APIS
#
# ****************************************** #

# Creating a Request
# All authenticated REST requests must contain the following headers
auth = {
    "API-KEY" : "API KEY GOES HERE",
    "API-PASSPHRASE" : "API PASSPHRASE GOES HERE"
}

# Get accounts
# Get balance on your trading account
def getAccount(auth):
    url = "https://api.btse.com/v1/restapi/account/"
    response = requests.get(url, headers=auth).json()
    return response

# Create order
# Place an order on BTSE platform
def createOrder(auth, amount, price, side, trade_type, product_id, time_in_force, tag):
    data = {
        'amount' : amount,
        'price' : price,
        'side' : side,
        'type' : trade_type,
        'product_id' : product_id,
        'time_in_force' : time_in_force,
        'tag' : tag
    }
    url = "https://api.btse.com/v1/restapi/order"
    request = requests.post(url, data=data, headers=auth).json()
    return request
    
# Get pending orders
# Get the list of open orders
def getOrders(auth, product_id):
    data = {
        'product_id' : product_id
    }
    url = "https://api.btse.com/v1/restapi/pending"
    response = requests.get(url, data=data, headers=auth).json()
    return response
    
# Cancel order
# Cancel an order
def cancelOrder(auth, order_id, product_id):
    data = {
        'order_id' : order_id,
        'product_id' : product_id
    }
    url = "https://api.btse.com/v1/restapi/deleteOrder"
    response = requests.post(url, data=data, headers=auth).json()
    return response
    
# Cancel all orders
# Cancels all pending orders from all markets
def cancelAll(auth, product_id):
    data = {
        'product_id' : product_id
    }
    url = "https://api.btse.com/v1/restapi/deleteOrders"
    response = requests.post(url, data=data, headers=auth)
    return response
    

# Get fills
# Get a list of fills
def getFills(auth, order_id, product_id, before, after, limit):
    data = {
        'order_id' : order_id,
        'product_id' : product_id,
        'before' : before,
        'after' : after,
        'limit' : limit
    }
    url = "https://api.btse.com/v1/restapi/fills"
    response = requests.post(url, data=data, headers=auth).json()
    return response

# ****************************************** #
#
# PUBLIC APIS
#
# ****************************************** #
  
# Get markets
# Get list of offered markets available on BTSE
def getMarkets():
    url = "https://api.btse.com/v1/restapi/markets"
    response = requests.get(url).json()
    return response
 
# Get trades
# Get list of transacted trades on a market   
def getTrades(market_id):
    url = "https://api.btse.com/v1/restapi/trades/"+market_id
    response = requests.get(url).json()
    return response
    
# Get ticker
# Get list of transacted trades on a market
def getTicker(market_id):
    url = "https://api.btse.com/v1/restapi/ticker/"+market_id
    response = requests.get(url).json()
    return response
    
# Get market statistics
# Get list of transacted trades on a market
def getStatistics(market_id):
    url = "https://api.btse.com/v1/restapi/stats/"+market_id
    response = requests.get(url).json()
    return response
    
# Get server time
# Get server time
def getServerTime():
    url = "https://api.btse.com/v1/restapi/time"
    response = requests.get(url).json()
    return response
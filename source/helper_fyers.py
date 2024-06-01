#DISCLAIMER:
#1) This sample code is for learning purposes only.
#2) Always be very careful when dealing with codes in which you can place orders in your account.
#3) The actual results may or may not be similar to backtested results. The historical results do not guarantee any profits or losses in the future.
#4) You are responsible for any losses/profits that occur in your account in case you plan to take trades in your account.
#5) TFU and Aseem Singhal do not take any responsibility of you running these codes on your account and the corresponding profits and losses that might occur.
#6) The running of the code properly is dependent on a lot of factors such as internet, broker, what changes you have made, etc. So it is always better to keep checking the trades as technology error can come anytime.
#7) This is NOT a tip providing service/code.
#8) This is NOT a software. Its a tool that works as per the inputs given by you.
#9) Slippage is dependent on market conditions.
#10) Option trading and automatic API trading are subject to market risks

from fyers_apiv3 import fyersModel
import datetime
import time
import requests
from datetime import timedelta
from pytz import timezone
import pandas as pd
import pytz

######PIVOT POINTS##########################
####################__INPUT__#####################


def getNiftyExpiryDate():
    nifty_expiry = {
        datetime.datetime(2023, 11, 16).date(): "23N16",
        datetime.datetime(2023, 11, 23).date(): "23N23",
        datetime.datetime(2023, 11, 30).date(): "23NOV",
        datetime.datetime(2023, 12, 7).date(): "23D07",
        datetime.datetime(2023, 12, 14).date(): "23D14",
        datetime.datetime(2023, 12, 21).date(): "23D21",
        datetime.datetime(2023, 12, 28).date(): "23DEC",
        datetime.datetime(2024, 1, 4).date(): "24104",
        datetime.datetime(2024, 1, 11).date(): "24111",
        datetime.datetime(2024, 1, 18).date(): "24118",
        datetime.datetime(2024, 1, 25).date(): "24JAN",
        datetime.datetime(2024, 2, 1).date(): "24201",
        datetime.datetime(2024, 2, 8).date(): "24208",
        datetime.datetime(2024, 2, 15).date(): "24215",
        datetime.datetime(2024, 2, 22).date(): "24222",
        datetime.datetime(2024, 2, 29).date(): "24FEB",
        datetime.datetime(2024, 3, 7).date(): "24307",
        datetime.datetime(2024, 3, 14).date(): "24314",
        datetime.datetime(2024, 3, 21).date(): "24321",
        datetime.datetime(2024, 3, 28).date(): "24MAR",
        datetime.datetime(2024, 4, 4).date(): "24404",
        datetime.datetime(2024, 4, 10).date(): "24410",
        datetime.datetime(2024, 4, 18).date(): "24418",
        datetime.datetime(2024, 4, 25).date(): "24APR",
        datetime.datetime(2024, 5, 2).date(): "24502",
        datetime.datetime(2024, 5, 9).date(): "24509",
        datetime.datetime(2024, 5, 16).date(): "24516",
        datetime.datetime(2024, 5, 23).date(): "24523",
        datetime.datetime(2024, 5, 30).date(): "24MAY",
        datetime.datetime(2024, 6, 6).date(): "24606",
        datetime.datetime(2024, 6, 13).date(): "24613",
        datetime.datetime(2024, 6, 20).date(): "24620",
        datetime.datetime(2024, 6, 27).date(): "24JUN",
    }

    today = datetime.datetime.now().date()

    for date_key, value in nifty_expiry.items():
        if today <= date_key:
            print(value)
            return value

def getBankNiftyExpiryDate():
    banknifty_expiry = {
        datetime.datetime(2023, 11, 15).date(): "23N15",
        datetime.datetime(2023, 11, 22).date(): "23N22",
        datetime.datetime(2023, 11, 30).date(): "23NOV",
        datetime.datetime(2023, 12, 6).date(): "23D06",
        datetime.datetime(2023, 12, 13).date(): "23D13",
        datetime.datetime(2023, 12, 20).date(): "23D20",
        datetime.datetime(2023, 12, 28).date(): "23DEC",
        datetime.datetime(2024, 1, 3).date(): "24103",
        datetime.datetime(2024, 1, 10).date(): "24110",
        datetime.datetime(2024, 1, 17).date(): "24117",
        datetime.datetime(2024, 1, 25).date(): "24JAN",
        datetime.datetime(2024, 1, 31).date(): "24131",
        datetime.datetime(2024, 2, 7).date(): "24207",
        datetime.datetime(2024, 2, 14).date(): "24214",
        datetime.datetime(2024, 2, 21).date(): "24221",
        datetime.datetime(2024, 2, 29).date(): "24FEB",
        datetime.datetime(2024, 3, 6).date(): "24306",
        datetime.datetime(2024, 3, 13).date(): "24313",
        datetime.datetime(2024, 3, 20).date(): "24320",
        datetime.datetime(2024, 3, 27).date(): "24MAR",
        datetime.datetime(2024, 4, 3).date(): "24403",
        datetime.datetime(2024, 4, 10).date(): "24410",
        datetime.datetime(2024, 4, 16).date(): "24416",
        datetime.datetime(2024, 4, 24).date(): "24APR",
        datetime.datetime(2024, 4, 30).date(): "24430",
        datetime.datetime(2024, 5, 8).date(): "24508",
        datetime.datetime(2024, 5, 15).date(): "24515",
        datetime.datetime(2024, 5, 22).date(): "24522",
        datetime.datetime(2024, 5, 29).date(): "24MAY",
        datetime.datetime(2024, 6, 5).date(): "24605",
        datetime.datetime(2024, 6, 12).date(): "24612",
        datetime.datetime(2024, 6, 19).date(): "24619",
        datetime.datetime(2024, 6, 26).date(): "24JUN",
    }

    today = datetime.datetime.now().date()

    for date_key, value in banknifty_expiry.items():
        if today <= date_key:
            print(value)
            return value

def getFinNiftyExpiryDate():
    finnifty_expiry = {
        datetime.datetime(2024, 2, 20).date(): "24220",
        datetime.datetime(2024, 2, 27).date(): "24FEB",
        datetime.datetime(2024, 3, 5).date(): "24305",
        datetime.datetime(2024, 3, 12).date(): "24312",
        datetime.datetime(2024, 3, 19).date(): "24319",
        datetime.datetime(2024, 3, 26).date(): "24MAR",
        datetime.datetime(2024, 4, 2).date(): "24402",
        datetime.datetime(2024, 4, 9).date(): "24409",
        datetime.datetime(2024, 4, 16).date(): "24416",
        datetime.datetime(2024, 4, 23).date(): "24423",
        datetime.datetime(2024, 4, 30).date(): "24APR",
        datetime.datetime(2024, 5, 7).date(): "24507",
        datetime.datetime(2024, 5, 14).date(): "24514",
        datetime.datetime(2024, 5, 21).date(): "24521",
        datetime.datetime(2024, 5, 28).date(): "24MAY",
        datetime.datetime(2024, 6, 4).date(): "24604",
        datetime.datetime(2024, 6, 11).date(): "24611",
        datetime.datetime(2024, 6, 18).date(): "24618",
        datetime.datetime(2024, 6, 25).date(): "24JUN",
    }

    today = datetime.datetime.now().date()

    for date_key, value in finnifty_expiry.items():
        if today <= date_key:
            print(value)
            return value

def getExpiryFormat(year, month, day, monthly):
    if monthly == 0:
        day1 = day
        if month == "JAN":
            month1 = 1
        elif month == "FEB":
            month1 = 2
        elif month == "MAR":
            month1 = 3
        elif month == "APR":
            month1 = 4
        elif month == "MAY":
            month1 = 5
        elif month == "JUN":
            month1 = 6
        elif month == "JUL":
            month1 = 7
        elif month == "AUG":
            month1 = 8
        elif month == "SEP":
            month1 = 9
        elif month == "OCT":
            month1 = "O"
        elif month == "NOV":
            month1 = "N"
        elif month == "DEC":
            month1 = "D"
    elif monthly == 1:
        day1 = ""
        month1 = month

    return str(year)+str(month1)+str(day1)

def getIndexSpot(stock):
    if stock == "BANKNIFTY":
        name = "NSE:NIFTYBANK-INDEX"
    elif stock == "NIFTY":
        name = "NSE:NIFTY50-INDEX"
    elif stock == "FINNIFTY":
        name = "NSE:FINNIFTY-INDEX"

    return name

def getOptionFormat(stock, intExpiry, strike, ce_pe):
    return "NSE:" + str(stock) + str(intExpiry)+str(strike)+str(ce_pe)

def getLTP(instrument):
    url = "http://localhost:4001/ltp?instrument=" + instrument
    try:
        resp = requests.get(url)
    except Exception as e:
        print(e)
    data = resp.json()
    return data

def manualLTP(symbol, fyers):
    data = {'symbols' : symbol}
    temp = fyers.quotes(data=data)
    #print(temp['d'][0]['v']['lp'])
    return float(temp['d'][0]['v']['lp'])

def placeOrder(inst ,t_type,qty,order_type,price,variety,fyers,papertrading=0):
    exch = inst[:3]
    symb = inst[4:]
    dt = datetime.datetime.now()
    #papertrading = 0 #if this is 1, then actual trades will get placed
    print(dt.hour,":",dt.minute,":",dt.second ," => ",t_type," ",symb," ",qty," ",order_type)
    if(order_type=="MARKET"):
        type1 = 2
        price = 0
    elif(order_type=="LIMIT"):
        type1 = 1

    if(t_type=="BUY"):
        side1=1
    elif(t_type=="SELL"):
        side1=-1

    data =  {
        "symbol":inst,
        "qty":qty,
        "type":type1,
        "side":side1,
        "productType":"INTRADAY",   #MARGIN
        "limitPrice":0,
        "stopPrice":0,
        "validity":"DAY",
        "disclosedQty":0,
        "offlineOrder":False,
        "stopLoss":0,
        "takeProfit":0
    }
    try:
        if (papertrading == 1):
            orderid = fyers.place_order(data)
            print(dt.hour,":",dt.minute,":",dt.second ," => ", symb , orderid)
            return orderid
        else:
            return 0


    except Exception as e:
        print(dt.hour,":",dt.minute,":",dt.second ," => ", symb , "Failed : {} ".format(e))

def getHistorical(ticker,interval,duration,fyers):
    range_from = datetime.datetime.today()-timedelta(duration)
    range_to = datetime.datetime.today()

    from_date_string = range_from.strftime("%Y-%m-%d")
    to_date_string = range_to.strftime("%Y-%m-%d")
    data = {
        "symbol":ticker,
        "resolution":1,
        "date_format":"1",
        "range_from":from_date_string,
        "range_to":to_date_string,
        "cont_flag":"1"
    }

    response = fyers.history(data=data)['candles']

    # Create a DataFrame
    columns = ['Timestamp','open','high','low','close','volume']
    df = pd.DataFrame(response, columns=columns)

    # Convert Timestamp to datetime in UTC
    df['Timestamp2'] = pd.to_datetime(df['Timestamp'],unit='s').dt.tz_localize(pytz.utc)

    # Convert Timestamp to IST
    ist = pytz.timezone('Asia/Kolkata')
    df['Timestamp2'] = df['Timestamp2'].dt.tz_convert(ist)
    # Filter rows where 'Timestamp2' is less than 15:30
    filtered_df = df[df['Timestamp2'].dt.time < pd.to_datetime('15:30').time()]

    filtered_df['datetime2'] = filtered_df['Timestamp2'].copy()
    # Set 'Timestamp2' as the index
    filtered_df.set_index('Timestamp2', inplace=True)
    # Update the format of the datetime index and add 5 hours and 30 minutes for IST
    #filtered_df.index = filtered_df.index.floor('min')  # Floor to minutes
    #print(hist_data)

    if interval < 375:
        finaltimeframe = str(interval)  + "min"
    elif interval == 375:
        finaltimeframe = "D"

    # Resample to a specific time frame, for example, 30 minutes
    resampled_df = filtered_df.resample(finaltimeframe).agg({
        'open': 'first',
        'high': 'max',
        'low': 'min',
        'close': 'last',
        'volume': 'sum',
        'datetime2': 'first'
    })

    # If you want to fill any missing values with a specific method, you can use fillna
    #resampled_df = resampled_df.fillna(method='ffill')  # Forward fill

    #print(resampled_df)
    resampled_df = resampled_df.dropna(subset=['open'])
    return resampled_df


def getHistorical_old(ticker,interval,duration,fyers):
    range_from = datetime.datetime.today()-timedelta(duration)
    range_to = datetime.datetime.today()

    from_date_string = range_from.strftime("%Y-%m-%d")
    to_date_string = range_to.strftime("%Y-%m-%d")
    data = {
        "symbol":ticker,
        "resolution":interval,
        "date_format":"1",
        "range_from":from_date_string,
        "range_to":to_date_string,
        "cont_flag":"1"
    }

    response = fyers.history(data=data)['candles']

    # Create a DataFrame
    columns = ['Timestamp','open','high','low','close','volume']
    df = pd.DataFrame(response, columns=columns)

    # Convert Timestamp to datetime in UTC
    df['Timestamp2'] = pd.to_datetime(df['Timestamp'],unit='s').dt.tz_localize(pytz.utc)

    # Convert Timestamp to IST
    ist = pytz.timezone('Asia/Kolkata')
    df['Timestamp2'] = df['Timestamp2'].dt.tz_convert(ist)
    # Filter rows where 'Timestamp2' is less than 15:30
    filtered_df = df[(df['Timestamp2'].dt.time >= pd.to_datetime("09:15:00").time()) & (df['Timestamp2'].dt.time <= pd.to_datetime("15:29:00").time())]

    return (filtered_df)


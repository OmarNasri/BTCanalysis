
import calendar
import time
import requests

def getData(start,end):
    # Change the start and end dates to unix time so that we can get the data from API
    startday = time.strptime(start, "%d/%m/%Y")
    endday = time.strptime(end, "%d/%m/%Y")
    startday = calendar.timegm(startday)
    endday = calendar.timegm(endday) + 1800  # We add 1800 to the endpoint, so that if the data is couple minutes after midnight, it will still be added to the list

    # Get data from API and store it as json
    response = requests.get(f"https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range?vs_currency=eur&from={str(startday)}&to={str(endday)}").json()

    return response
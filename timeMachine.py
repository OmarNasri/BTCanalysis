
import bearishTrend
import listDaily
import requestData
import pandas

def mostProfitable(start,end):
    pricedata = requestData.getData(start,end)["prices"]
    dailyprices = listDaily.getDaily(pricedata)

    #get the consecutive days from date range, that the price of BTC has gone down using the function we built earlier, then save only the int from the functions output
    consecutive = int(''.join(filter(str.isdigit,bearishTrend.downwardTrend(start,end))))

    # the difference of start and end dates in days
    start = pandas.to_datetime(start, format='%d/%m/%Y')
    end = pandas.to_datetime(end, format='%d/%m/%Y')
    diff = int((end-start).days)

    # compare if consecutive days that the bitcoin has lowered equals the date difference, in which case you should not buy BTC
    if diff == consecutive:
        return "Bitcoin has only gone down in value at given range, don't buy BTC at all. "

    # Iterate through the pricelist using two inner loops to find the biggest price difference in days, this will give us the desired buy and sell date
    else:
        first = dailyprices[0]
        first = first[1]
        second = dailyprices[1]
        second = second[1]
        comparable = second-first
        for startday in range (len(dailyprices)):
            temp = dailyprices[startday]
            for endday in range (startday+1,len(dailyprices)):
                temp2 = dailyprices[endday]
                if temp2[1]-temp[1] > comparable:
                    resultstart = temp
                    resultend = temp2
                    comparable = temp2[1]-temp[1]

        #Convert unix time back to regular time for output
        buy = pandas.to_datetime(resultstart[0], unit="ms")
        sell = pandas.to_datetime(resultend[0], unit="ms")

        return f"You should buy: {buy.day}/{buy.month}/{buy.year} and sell: {sell.day}/{sell.month}/{sell.year}"




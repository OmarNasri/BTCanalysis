

import listDaily
import requestData

def downwardTrend(start,end):

    prices = requestData.getData(start,end)["prices"]
    daily = listDaily.getDaily(prices)
    consecutive = 0
    result = 0
    comparable = daily[0]
    comparable = float(comparable[1])

    for i in daily:
        if i[1]<comparable:
            consecutive+=1
        else:
            consecutive = 0
        if consecutive>result:
            result = consecutive
        comparable = i[1]

    return f"Maximum downward trend: {result} days."



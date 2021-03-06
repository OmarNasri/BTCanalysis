

import pandas
import listDaily
import requestData


def highest(start,end):
    volume = requestData.getData(start,end)["total_volumes"]
    daylist = listDaily.getDaily(volume)
    comparable = daylist[0]
    comparable = comparable[1]

    #Iterate through the total volumelist and find the day with biggest volume

    for i in daylist:
        if i[1]>comparable:
            biggest = i
            comparable = i[1]

    # Convert the date with biggest volume back to normal time for output
    date = pandas.to_datetime(biggest[0], unit="ms")
    volume = biggest[1]
    #Get the price of bitcoin in eur from the date that had highest trading volume and multiply it with total volume
    price = requestData.getData(f"{date.day}/{date.month}/{date.year}",f"{date.day}/{date.month}/{date.year}")["prices"]
    price = price[0]
    return f"Date with the highest trading volume is {date.day}/{date.month}/{date.year} and the volume in eur: {price[1]*volume}"


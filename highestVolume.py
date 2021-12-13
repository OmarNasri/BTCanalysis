<<<<<<< HEAD
import pandas
import listDaily
import requestData


def highest(start,end):
    volume = requestData.getData(start,end)["total_volumes"]
    daylist = listDaily.getDaily(volume)
    comparable = daylist[0]
    comparable = comparable[1]

    for i in daylist:
        if i[1]>comparable:
            biggest = i
            comparable = i[1]
    date = pandas.to_datetime(biggest[0], unit="ms")
    price = requestData.getData(f"{date.day}/{date.month}/{date.year}",f"{date.day}/{date.month}/{date.year}")["prices"]
    price = price[0]
    return f"Date with the highest trading volume is {date.day}/{date.month}/{date.year} and the price of bitcoin from this date is : {price[1]}"

=======
import pandas
import listDaily
import requestData


def highest(start,end):
    volume = requestData.getData(start,end)["total_volumes"]
    daylist = listDaily.getDaily(volume)
    comparable = daylist[0]
    comparable = comparable[1]

    for i in daylist:
        if i[1]>comparable:
            biggest = i
            comparable = i[1]
    date = pandas.to_datetime(biggest[0], unit="ms")
    price = requestData.getData(f"{date.day}/{date.month}/{date.year}",f"{date.day}/{date.month}/{date.year}")["prices"]
    price = price[0]
    return f"Date with the highest trading volume is {date.day}/{date.month}/{date.year} and the price of bitcoin from this date is : {price[1]}"

>>>>>>> refs/remotes/origin/main

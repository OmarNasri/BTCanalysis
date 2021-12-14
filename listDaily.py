
import pandas

def getDaily(list):
    #iterate the list and return only the days price at 00:00 utc
    result = []
    for i in list:
        temp = pandas.to_datetime(int(i[0]),unit="ms")
        if temp.hour == 00:
            result.append(i)

    return result
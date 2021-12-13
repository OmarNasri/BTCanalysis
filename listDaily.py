
import pandas

def getDaily(list):
    result = []
    for i in list:
        temp = pandas.to_datetime(int(i[0]),unit="ms")
        if temp.hour == 00:
            result.append(i)

    return result
import datetime 


def getFirstDayOfMonth(strDate):
    todayDate = datetime.datetime.strptime(strDate, '%Y-%m-%d')
    strDate
    if (todayDate - todayDate.replace(day=1)).days > 25:
        x= todayDate + datetime.timedelta(30)
        x.replace(day=1)
        print (x)
    else:
        print(todayDate.replace(day=1))

def getLastDayOfMonth(strDate):
    test_date = datetime.datetime.strptime(strDate, '%Y-%m-%d')
    nxt_mnth = test_date.replace(day=28) + datetime.timedelta(days=4)
    
    # subtracting the days from next month date to
    # get last date of current Month
    res = nxt_mnth - datetime.timedelta(days=nxt_mnth.day)
    
    # printing result
    print("Last date of month : " + str(res))

getFirstDayOfMonth("2020-02-07")
getLastDayOfMonth("2020-02-07")

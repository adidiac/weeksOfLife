from datetime import date, datetime, timedelta
from time import daylight, sleep

def getNumberOfWeeksTillNow(year,month,day):

    d1=date(year,month,day)
    d2=date.today()

    monday1 = (d1 - timedelta(days=d1.weekday()))
    monday2 = (d2 - timedelta(days=d2.weekday()))
    return (monday2 - monday1).days / 7
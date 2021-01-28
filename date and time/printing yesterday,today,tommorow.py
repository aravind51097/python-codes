import datetime
from datetime import timedelta
today=datetime.date.today()
day_1=timedelta(days=1)
yesterday=(today-day_1)
tommorow=(today+day_1)


print('yesterday is ',yesterday)
print('today is  ',today)
print('tommorow is  ',tommorow)

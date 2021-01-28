from datetime import timedelta
import datetime
today=datetime.datetime.now()
sec=timedelta(seconds=5)
print('present time is',today)
print('after 5 secs is  ',today+sec)

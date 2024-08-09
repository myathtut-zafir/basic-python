import datetime
from datetime import datetime
from datetime import date
# myTime=datetime.time(2,20,1)
# print(myTime)
# print(myTime.minute)
# print(myTime.hour)

# today=datetime.date.today()
# print(today)
# print(today.ctime())
dt=datetime(2021,10,3)
print(dt)
dt=dt.replace(year=2022)
print(dt)
date1=date(2022,11,3)
date2=date(2023,11,3)
result=date1 - date2
print(result.total_seconds())

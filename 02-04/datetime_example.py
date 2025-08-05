import datetime

birth_day = datetime.datetime(2020, 11, 22)
print(birth_day)
# 2020-11-22 00:00:00

birth_day = datetime.datetime(2020, 11, 22, 13, 6, 15)
print(birth_day)
# 2020-11-22 13:06:15

now = datetime.datetime.now()
print(now)
# 2025-08-06 02:29:19.622432
print(now.year)
# 2025
print(now.month)
# 8
print(now.day)
# 6
print(now.hour)
# 2
print(now.minute)
# 31
print(now.second)
# 44
print(now.microsecond)
# 866510

print(now.date())
# 2025-08-06
print(now.time())
# 02:33:18.777817

now_date = now.strftime("%Y/%m/%d")
print(now_date)
# 2025/08/06

now_time = now.strftime("%H시 %M분 %S초")
print(now_time)
# 02시 35분 46초


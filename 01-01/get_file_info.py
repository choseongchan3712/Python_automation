import os
import datetime

#! 1. 만든 날짜
birth_time_stamp = os.path.getctime("Haehong_Logo.png")
print(birth_time_stamp)
# 1753101120.168956

birth_time = datetime.datetime.fromtimestamp(birth_time_stamp)
print(birth_time)
# 2025-07-21 21:32:00.168956

print(f"만든 날짜: {birth_time}")
# 만든 날짜: 2025-07-21 21:32:00.168956

#! 수정한 날짜
mtime_stamp = os.path.getmtime("Haehong_Logo.png")
mtime = datetime.datetime.fromtimestamp(mtime_stamp)
print(mtime)
# 2025-05-29 03:18:33.355697

print(f"수정한 날짜: {mtime}")
# 수정한 날짜: 2025-05-29 03:18:33.355697

#! 마지막으로 사용한 날짜
atime_stamp = os.path.getatime("Haehong_Logo.png")
atime = datetime.datetime.fromtimestamp(atime_stamp)
print(atime)
# 2025-07-27 23:28:32.988964

print(f"액세스한 날짜:{atime}")
# 액세스한 날짜:2025-07-27 23:28:32.988964


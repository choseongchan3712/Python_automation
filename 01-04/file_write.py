import os

# append
with open("업무자동화.txt", "a", encoding="UTF-8") as file:
    pass

# write
with open("데이터사이언스.txt", "w", encoding="UTF-8") as file:
    pass

# os.rename("기존이름", "새 이름") -> 이름 바꾸기
os.rename("업무자동화.txt", "업무 자동화.txt")
os.rename("데이터사이언스.txt", "데이터 사이언스.txt")

os.remove("업무 자동화.txt")
os.remove("데이터 사이언스.txt")
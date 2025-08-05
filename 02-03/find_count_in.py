
# ! find()
message = "수달, 해달, 오리, 강아지, 고양이"
print(message.find("수달"))
# 0 -> 0번째 인덱스
print(message.find("해달"))
# 4 -> 4번째 인덱스
print(message.find("비둘기"))
# -1 -> 없음

# ! count()
message = "수달, 수달, 해달, 비둘기, 비둘기, 비둘기"
print(message.count("수달"))
# 2
print(message.count("해달"))
# 1
print(message.count("비둘기"))
# 3

with open("william.txt", encoding="UTF-8") as file:
    content = file.read()
    print(content.count("윌리엄"))
    # 2

# ! in
print("A" in "ABCD")
# True
print("ABC" in "ABCD")
# True
print("E" in "ABCD")
# False

log = "수달, 해달, 오리, 강아지, 고양이"
keyword = "수달"

if keyword in log:
    print(f"{keyword} 기록이 발견되었습니다.")
else:
    print(f"{keyword} 기록이 발견되지 않았습니다.")
# 수달 기록이 발견되었습니다.

numbers = [2, 3, 5, 7, 11]
print(3 in numbers)
# True
print(10 in numbers)
# False
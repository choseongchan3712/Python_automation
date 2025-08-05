message = "제 이름은 otter입니다."
print(message.replace("otter", "수달"))
# 제 이름은 수달입니다.

message = " 제 이름은 otter입니다. "
print(message)
#  제 이름은 otter입니다. 
print(message.strip())
# 제 이름은 otter입니다.
print(message.replace(" ", ""))
# 제이름은otter입니다.

message = "...제 이름은 otter입니다..."
print(message.strip("."))
# 제 이름은 otter입니다
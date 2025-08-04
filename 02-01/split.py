phone_number = "010-0000-1111"
print(phone_number.split("-"))
# ['010', '0000', '1111']
print("010-0000-1111".split("-"))
['010', '0000', '1111']

address = "서울특별시 종로구 세종로 청와대로 1"
print(address.split())
# ['서울특별시', '종로구', '세종로', '청와대로', '1']
print(address.split()[0])
# 서울특별시

file_name = "사진 이름.jpeg"
name = file_name.split(".")[0]
extension = file_name.split(".")[1]

print(f"파일 이름: {name}")
print(f"확장자: {extension}")
# 파일 이름: 사진 이름
# 확장자: jpeg

# ! 위 코드 간단하게 적는 법:
name, extension = file_name.split(".")
print(f"파일 이름: {name}")
print(f"확장자: {extension}")
# 파일 이름: 사진 이름
# 확장자: jpeg

# 새로운 내용 추가
with open("text1.txt", "a", encoding="UTF-8") as file:
    file.write("\n안녕하세요.")

# 내용 덮어 쓰기
with open("text1.txt", "w", encoding="UTF-8") as file:
    file.write("반갑습니다.")

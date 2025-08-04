with open("text_1.txt", "a+", encoding="UTF-8") as file:
    file.write("안녕하세요\n")
    file.seek(0)
    print(file.read())
    # 안녕하세요

with open("text_2.txt", "w+", encoding="UTF-8") as file:
    file.write("반갑습니다.\n")
    file.seek(0)
    print(file.read())
    # 반갑습니다.

with open("text_2.txt", "r+", encoding="UTF-8") as file:
    file.write("하이")
    file.seek(0)
    print(file.read())
    # 하이습니다.
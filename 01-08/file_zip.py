import zipfile

# ? 압축하기
with zipfile.ZipFile("img1.zip", "w") as zip:
    zip.write("Haehong_Logo.png")
    # ! 용량 변화 없이 압축됨

with zipfile.ZipFile("img2.zip", "w", compression=zipfile.ZIP_DEFLATED) as zip:
    zip.write("Haehong_Logo.png")
    # ! 용량 변화 있이 압축됨

# ? 압축 풀기
with zipfile.ZipFile("img2.zip", "r") as zip:
    zip.extractall("data")

import os
import zipfile

print(os.listdir("."))
# ['Haehong_Logo.png', 'listdir.py']

filenames = os.listdir(".")

with zipfile.ZipFile("Logo.zip", "w") as zip:
    for filename in filenames:
        if "Logo" in filename:
            zip.write(filename)
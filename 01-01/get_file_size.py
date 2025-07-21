import os

print(os.path.getsize('Haehong_Logo.png'))
# 30053

size = os.path.getsize('Haehong_Logo.png')
def byte_to_kb(byte):
    kb = byte / 1000
    return kb


print(f"{byte_to_kb(size)}KB")
# 30.053KB
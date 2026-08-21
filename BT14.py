"""
xây dựng chương trình rút thăm trúng thưởng
1 . thêm mã dự thưởng vào danh sách 
2 . Sắp xếp danh sách các mã
3 . quay và chọn ngẫu nhiên một phần thưởng trong danh sách
"""
#thêm mã dự thưởng
setCode = set()
code = ""
while code != "exit":
    code = input("Nhập mã dự thưởng: ")
    if code in setCode:
        print("Mã dự thưởng {} đã có trong danh sách".format(code))
    else:
        if code != "exit":
            setCode.add(code)
            print("Mã dự thưởng {} đã được thêm vào danh sách".format(code))
            print("Danh sách các mã dự thưởng hiện tại là: ")
            for i in setCode:
                print(i)
#sắp xếp danh sách các mã dự thưởng
sortedList = sorted(setCode)
print("Danh sách các mã dự thưởng sau khi sắp xếp là: ")
for i in sortedList:
    print(i)
#quay và chọn ngẫu nhiên một phần thưởng trong danh sách
from os import remove
import random
import time

print("Đang quay", end="", flush=True)
for _ in range(10):
    time.sleep(0.2)
    print(".", end="", flush=True)
randomCode = random.choice(list(setCode))
print("\nMã dự thưởng được chọn ngẫu nhiên là: ",randomCode)
setCode.remove(randomCode)
print("Danh sách các mã dự thưởng còn lại là: ")
for i in setCode:
    print(i)

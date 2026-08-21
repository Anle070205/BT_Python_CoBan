
import random

mucTraiCay = {"táo", "cam", "mít", "xoài", "dưa", "nho", "lê", "ổi"}
sortedList = sorted(mucTraiCay)
print("các mục trái cây sau khi sắp xếp là: ")
for i in sortedList:
    print(i)
random.shuffle(list(mucTraiCay))
print("các mục trái cây sau khi xáo trộn là: ")
for i in mucTraiCay:
    print(i)
print("loại trái cây ngẫu nhiên được chọn là: ", random.choice(list(mucTraiCay)))
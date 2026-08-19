import math
import random
# nhập 1 list thí sinh , và chọn ngẫu nhiêu 3 người , và chọn 3 người có điểm cao nhất
list_thi_sinh = []
for i in range(5):
    ten = input("Nhập tên thí sinh thứ {}: ".format(i+1))
    diem = float(input("Nhập điểm của {}: ".format(ten)))
    list_thi_sinh.append((ten, diem))
print("--------------------------------")
print("Danh sách thí sinh:")
for i, (ten, diem) in enumerate(list_thi_sinh):
    print("Tên: {}, Điểm: {}".format(ten, diem))
print("--------------------------------")

print("Chọn ngẫu nhiên 3 thí sinh:")
random_thi_sinh = random.sample(list_thi_sinh, 3)
for i, (ten, diem) in enumerate(random_thi_sinh):
    print("Tên: {}, Điểm: {}".format(ten, diem))
print("--------------------------------")

top_3 = sorted(list_thi_sinh, key=lambda x: x[1], reverse=True)[:3]
print("3 thí sinh có điểm cao nhất là: ")
for i in range(3):
    print("Tên: {}, Điểm: {}".format(top_3[i][0], top_3[i][1]))

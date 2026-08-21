"""
xây dựng function để tìm USCLN của 2 số nguyên dương
"""
from Lib import re

#function tìm USCLN của 2 số nguyên dương
def USCLN(a, b):
    while b != 0:
        a, b = b, a % b
    return a
#function tìm BCNN của 2 số nguyên dương
def BCNN(a, b):
    return a * b // USCLN(a, b)
print("Nhập 2 số nguyên dương: ")
a = int(input())
b = int(input())
print("USCLN của {} và {} là: {}".format(a, b, USCLN(a, b)))
print("BCNN của {} và {} là: {}".format(a, b, BCNN(a, b)))
"""
xây dựng function đệ quy tính giai thừa của một số nguyên dương
"""
def giaiThua(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * giaiThua(n - 1)
print("Nhập một số nguyên dương: ")
n = int(input())
print("Giai thừa của {} là: {}".format(n, giaiThua(n)))
"""
xây dựng function nhập danh sách sinh viên , điểm và tính điểm trung bình của lớp
"""
def nhapDanhSachSinhVien():
    danhSach = {}
    while True:
        ten = input("Nhập tên sinh viên : ")
        if ten == "exit":
            break
        lop = input("Nhập lớp của sinh viên {}: ".format(ten))
        diem = float(input("Nhập điểm của sinh viên {}: ".format(ten)))
        danhSach[ten] = (lop, diem)
    print("Danh sách sinh viên hiện tại là: ")
    for ten, (lop, diem) in danhSach.items():
        print("Tên: {}, Lớp: {}, Điểm: {}".format(ten, lop, diem))
    return danhSach
def tinhDiemTrungBinh(danhSach, lop):
    total = sum(diem for t_ten, (t_lop, diem) in danhSach.items() if t_lop == lop)
    count = sum(1 for t_ten, (t_lop, diem) in danhSach.items() if t_lop == lop)
    return total / count if count > 0 else 0
print("Nhập danh sách sinh viên: ")
danhSach = nhapDanhSachSinhVien()
lop = input("Nhập lớp cần tính điểm trung bình: ")
dtb = tinhDiemTrungBinh(danhSach, lop)
print("Điểm trung bình của lớp {} là: {}".format(lop, dtb))
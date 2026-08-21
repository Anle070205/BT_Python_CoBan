# chuyển đổi số nguyên sang số nhị phân, thập phân, thập lục phân
from re import match
from unittest import case
choice = ""
while (choice != "0"):
    print("----------------menu----------------")
    print("1. Chuyển đổi sang nhị phân")
    print("2. Chuyển đổi sang thập phân")
    print("3. Chuyển đổi sang thập lục phân")
    print("0. Thoát")
    print("------------------------------------")
    choice = input("Nhập lựa chọn: ")
    match choice:
        case "1":
            print("Nhập số nguyên: ")
            n = int(input())
            print("Số nhị phân là: ", bin(n)[2:])
        case "2":
            print("Nhập số nguyên: ")
            n = int(input())
            print("Số thập phân là: ", n)
        case "3":
            print("Nhập số nguyên: ")
            n = int(input()) 
            print("Số thập lục phân là: ", hex(n)[2:])
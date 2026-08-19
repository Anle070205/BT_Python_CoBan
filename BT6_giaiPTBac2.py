#nhập dữ liệu
print("giải phương trình bậc 2: ax^2 + bx + c = 0")
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
delta = b**2 - 4*a*c
if delta < 0:
    print("Phương trình vô nghiệm")
else:
    if delta == 0:
        x = -b/(2*a)
        print("Phương trình có nghiệm kép: x1 = x2 = ",x)
    else:
        x1 = (-b + delta**0.5)/(2*a)
        x2 = (-b - delta**0.5)/(2*a)
        print("Phương trình có 2 nghiệm phân biệt: x = {1} và x2 = {2}".format(x1,x2))
        

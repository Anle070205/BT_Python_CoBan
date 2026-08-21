"""
kiểu dữ liệu tuple và set
"""
#tuple
from re import match


quaTao = ("táo xanh", "táo đỏ","táo tàu", "táo Mỹ", "táo Úc", "táo Pháp", "táo Nhật", "táo Hàn", "táo Thái", "táo Việt Nam")
print("các loại trái cây là: ")
for i in quaTao:
    print(i)
list1 = sorted(quaTao)
print("các loại trái cây sau khi sắp xếp: ")
for i in list1:
    print(i)
#set
mucTraiCay = {"táo", "cam", "mít", "xoài", "dưa", "nho", "lê", "ổi"}
print("các mục trái cây :")
for i in mucTraiCay:
    print(i)
choice = ""
while choice != "exit":
    choice = input("chọn mục : ")
    if choice in mucTraiCay:
        print("các loại trái cây có trong mục {} là: ".format([choice]))
        match choice:
            case "táo":
                print(quaTao)
            case "cam":
                quaCam = ("cam sành", "cam vàng", "cam ngọt")
                print(quaCam)
            case "mít":
                quaMit = ("mít Thái", "mít ruột đỏ", "mít ruột vàng")
                print(quaMit)
            case "xoài":
                quaXoai = ("xoài cát Hòa Lộc", "xoài keo", "xoài tượng")
                print(quaXoai)
            case "dưa":
                quaDua = ("dưa hấu", "dưa lưới", "dưa gang")
                print(quaDua)
            case "nho":
                quaNho = ("nho xanh", "nho đỏ", "nho đen")
                print(quaNho)
            case "lê":
                quaLe = ("lê Hàn Quốc", "lê Mỹ", "lê Pháp")
                print(quaLe)
            case "ổi":
                quaOi = ("ổi ruột đỏ", "ổi ruột trắng")
                print(quaOi)
#thêm phần tử vào set
newFruit = ""
while newFruit != "exit":
    newFruit = input("Nhập loại trái cây muốn thêm vào mục trái cây: ")
    if newFruit in mucTraiCay:
        print("loại trái cây {} đã có trong mục trái cây".format(newFruit))
    else: 
            if newFruit != "exit":
                mucTraiCay.add(newFruit)
                print("loại trái cây {} đã được thêm vào mục trái cây".format(newFruit))
                print("các mục trái cây hiện tại là: ")
                for i in mucTraiCay:
                    print(i)
#update thêm nhiều phần tử vào trong set
updateFruit = ""
while updateFruit != "exit":
    updateFruit = input("Nhập các loại trái cây muốn thêm vào mục trái cây (cách nhau bởi dấu phẩy): ")
    if updateFruit != "exit":
        newFruits = updateFruit.split(" , ")
        mucTraiCay.update(newFruits)
        print("các mục trái cây hiện tại là: ")
        for i in mucTraiCay:
            print(i)
#thêm phần tử từ list vào set
fruitList = ["jery", "banana", "jery"]
mucTraiCay.update(fruitList)
print("các mục trái cây hiện tại là: ")
for i in mucTraiCay:
    print(i)
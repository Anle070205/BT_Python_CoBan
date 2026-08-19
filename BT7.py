"""
nhập 3 điểm trên hệ trục Oxy và tính diện tích tam giác tạo bởi 3 điểm đó
1 . xác định 3 điểm có tạo thành tam giác hay không
2. nếu tạo thành tam giác thì tính diện tích và chu vi của tam giác đó
3. nếu không tạo thành tam giác thì in ra thông báo
"""
print("nhập lần lượt 3 điểm A, B, C trên hệ trục Oxy")
A = list(map(float, input("Nhập tọa độ điểm A (x y): ").split()))
B = list(map(float, input("Nhập tọa độ điểm B (x y): ").split()))
C = list(map(float, input("Nhập tọa độ điểm C (x y): ").split()))
ktra = float((B[0]-A[0])*(C[1]-A[1])-(C[0]-A[0])*(B[1]-A[1]))
if ktra == 0:
    print("3 điểm A, B, C không tạo thành tam giác")
else:
    import math
    AB = math.sqrt((B[0]-A[0])**2+(B[1]-A[1])**2)
    AC = math.sqrt((C[0]-A[0])**2+(C[1]-A[1])**2)
    BC = math.sqrt((C[0]-B[0])**2+(C[1]-B[1])**2)
    chu_vi = AB + AC + BC
    p = chu_vi/2
    dien_tich = math.sqrt(p*(p-AB)*(p-AC)*(p-BC))
    print("3 điểm A, B, C tạo thành tam giác")
    print("Diện tích tam giác là: ", round(dien_tich, 2))
    print("Chu vi tam giác là: ", round(chu_vi, 2))
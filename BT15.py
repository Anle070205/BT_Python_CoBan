"""
kiểu dữ liệu dictionary
bài tập dictionary :
Chương trình hiển thị menu sau và lặp lại cho đến khi người dùng chọn thoát.
            1 Xem tất cả danh mục
            2 Xem các loại trái cây trong một danh mục
            3 Thêm một danh mục mới
            4 Thêm một loại trái cây vào danh mục
            5 Xóa một danh mục
            6 Tìm kiếm danh mục
            0 Thoát
"""
trai_cay = {
    "táo": ["táo xanh", "táo đỏ", "táo Mỹ"],
    "cam": ["cam sành", "cam vàng"],
    "xoài": ["xoài cát Hòa Lộc", "xoài keo"],
    "nho": ["nho xanh", "nho đỏ"]
}
choice = ""
while choice != "0":
    print("----------------menu----------------")
    print("1. Xem tất cả danh mục")
    print("2. Xem các loại trái cây trong một danh mục")
    print("3. Thêm một danh mục mới")
    print("4. Thêm một loại trái cây vào danh mục")
    print("5. Xóa một danh mục")
    print("6. Tìm kiếm danh mục")
    print("0. Thoát")
    print("------------------------------------")
    choice = input("Nhập lựa chọn: ")
    match choice:
        #Xem tất cả danh mục
        case "1":
            print("Các danh mục hiện có là: ")
            for danh_muc in trai_cay.keys():
                print(danh_muc)
        #Xem các loại trái cây trong một danh mục
        case "2":
            danh_muc = input("Nhập tên danh mục: ")
            get_loai_trai_cay = trai_cay.get(danh_muc)
            if get_loai_trai_cay is not None:
                print("Các loại trái cây trong danh mục {} là: ".format(danh_muc))
                for loai_trai_cay in get_loai_trai_cay:
                    print(loai_trai_cay)
            else:
                print("Danh mục {} không tồn tại.".format(danh_muc))
        #Thêm một danh mục mới
        case "3":
            trai_cay_moi = input("Nhập tên danh mục mới: ")
            if trai_cay_moi in trai_cay:
                print("Danh mục {} đã tồn tại.".format(trai_cay_moi))
            else:
                trai_cay[trai_cay_moi] = []
                print("Danh mục {} đã được thêm vào.".format(trai_cay_moi))
        #Thêm các loại trái cây vào danh mục
        case "4":
            print("Các danh mục hiện có là: ")
            for danh_muc in trai_cay.keys():
                print(danh_muc)
            danh_muc = input("Nhập tên danh mục muốn thêm : ")
            if danh_muc in trai_cay:
                loai_trai_cay = input("Nhập tên loại trái cây: ")
                trai_cay[danh_muc].append(loai_trai_cay)
                print("Loại trái cây {} đã được thêm vào danh mục {}.".format(loai_trai_cay, danh_muc))
            else:
                print("Danh mục {} không tồn tại.".format(danh_muc))
        #Xóa một danh mục
        case "5":
            danh_muc = input("Nhập tên danh mục muốn xóa: ")
            if danh_muc in trai_cay:
                trai_cay.pop(danh_muc)
                print("Danh mục {} đã được xóa.".format(danh_muc))
            else:
                print("Danh mục {} không tồn tại.".format(danh_muc))
        #Tìm kiếm danh mục
        case "6":
            danh_muc = input("Nhập tên danh mục muốn tìm kiếm: ")
            if danh_muc in trai_cay:
                print("Danh mục {} tồn tại.".format(danh_muc))
                print("Các loại trái cây trong danh mục {} là: ".format(danh_muc))
                for loai_trai_cay in trai_cay[danh_muc]:
                    print(loai_trai_cay)
            else:
                print("Danh mục {} không tồn tại.".format(danh_muc))
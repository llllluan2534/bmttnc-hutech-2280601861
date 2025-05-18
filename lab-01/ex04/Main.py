from QuanLySinhVien import QuanLySinhVien
qlsv = QuanLySinhVien()
while( 1 == 1):
    print("\nChuong trinh quan ly sinh vien")
    print("1. Them sinh vien") 
    print("2. Cap nhat thong tin sinh vien boi ID")
    print("3. Xoa sinh vien boi ID") 
    print("4. Tim kiem sinh vien theo ten")
    print("5. Sap xep sinh vien theo diem trung binh")
    print("6. Sap xep sinh vien theo ten chuyen nganh")
    print("7. Hien thi danh sach sinh vien")
    print("0. Thoat")
    
    key = int(input("Nhap lua chon: "))
    if (key == 1):
        print("\n1. Them sinh vien")
        qlsv.nhapSinhVien()
        print("Them sinh vien thanh cong")
    elif (key == 2):
        if(qlsv.soLuongSinhVien() > 0):
            print("\n2. Cap nhat thong tin sinh vien")
            print("Nhap ID")
            id = int(input())
            qlsv.updateSinhVien(id)
        else:
            print("Khong co sinh vien nao trong danh sach")
    elif (key == 3):
        if(qlsv.soLuongSinhVien() > 0):
            print("\n3. Xoa sinh vien")
            print("Nhap ID")
            id = int(input())
            if(qlsv.deleteByID(id)):
               print("\nSinh vien co ID = ", id, " da bi xoa")
            else:
               print("\nSinh vien co ID = ", id, " khong ton tai")
        else:
            print("Khong co sinh vien nao trong danh sach")
    elif (key == 4):
        if(qlsv.soLuongSinhVien() > 0):
            print("\n4. Tim kiem sinh vien theo ten")
            print("Nhap ten")
            name = input()
            qlsv.searchByName(name)
        else:
            print("Khong co sinh vien nao trong danh sach")
    elif (key == 5):  
        if(qlsv.soLuongSinhVien() > 0):
            print("\n5. Sap xep sinh vien theo diem trung binh (GPA).")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())    
        else:
            print("Khong co sinh vien nao trong danh sach")
    elif (key == 6):
        if(qlsv.soLuongSinhVien() > 0):
            print("\n6. Sap xep sinh vien theo ten.")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())    
        else:
            print("Khong co sinh vien nao trong danh sach")
    elif (key == 7):
        if(qlsv.soLuongSinhVien() > 0):
            print("\n7. Hien thi danh sach sinh vien")
            qlsv.showSinhVien(qlsv.getListSinhVien())    
        else:
            print("Khong co sinh vien nao trong danh sach")
    elif (key == 0):
        print("\nBan da chon thoat chuong trinh")
        break
    else:
        print("Khong co chuc nang nay!")
        print("Hay chon chuc nang khac trong hop menu")
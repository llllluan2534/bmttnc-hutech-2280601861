import keyword
from SinhVien import SinhVien

class QuanLySinhVien:
    list_sinhvien = []
    def generateID(self):
        maxId = 1
        if (self.soLuongSinhVien() > 0):
            maxId = self.list_sinhvien[0]._id 
            for sv in self.list_sinhvien:
                if (sv._id > maxId):
                    maxId = sv._id
            maxId += 1
        return maxId
    def soLuongSinhVien(self):
        return self.list_sinhvien.__len__()
    def nhapSinhVien(self):
        svId = self.generateID()
        name = input("Nhap ten sinh vien: ")  
        sex = input("Nhap gioi tinh sinh vien: ")
        major = input("Nhap nganh hoc sinh vien: ")
        diemTB = float(input("Nhap diem trung binh sinh vien: ")) 
        sv = SinhVien(svId, name, sex, major, diemTB)
        self.XepLoaiHocLuc(sv)
        self.list_sinhvien.append(sv)
    def updateSinhVien(self, id):
        sv:SinhVien = self.findByID(id)
        for sv in self.list_sinhvien:
            if (sv != None):
                name = input("Nhap ten sinh vien: ") 
                sex = input("Nhap gioi tinh sinh vien: ")
                major = input("Nhap nganh hoc sinh vien: ")
                diemTB = float(input("Nhap diem trung binh sinh vien: "))
                sv._name = name
                sv._sex = sex
                sv._major = major   
                sv._diemTB = diemTB
                self.XepLoaiHocLuc(sv)
            else:
                print("Sinh vien co ID = {} khong ton tai".format(id))
    def sortByID(self):
        self.list_sinhvien.sort(key=lambda x: x._id, reverse=False)
    def sortByName(self):
        self.list_sinhvien.sort(key=lambda x: x._name, reverse=False)
    def sortByDiemTB(self):
        self.list_sinhvien.sort(key=lambda x: x._diemTB, reverse=False)
    def findByID(self, ID):
        searchResult = None
        if (self.soLuongSinhVien() > 0):
            for sv in self.list_sinhvien:
                if (sv._id == ID):
                    searchResult = sv
        return searchResult
    def findByName(self, keyword):
        listSV = []
        if (self.soLuongSinhVien() > 0):
            for sv in self.list_sinhvien:
                if(keyword.upper() in sv._name.upper()):
                    listSV.append(sv)
        return listSV
    def deleteByID(self, ID):
        isDelete = False
        sv = self.findByID(ID)
        if (sv != None):
            self.list_sinhvien.remove(sv)
            isDelete = True
        return isDelete
    def XepLoaiHocLuc(self, sv:SinhVien):
        if (sv._diemTB >= 8):
            sv._hocluc = "Gioi"
        elif (sv._diemTB >= 6.5):
            sv._hocluc = "Kha"
        elif (sv._diemTB >= 5):
            sv._hocluc = "Trung binh"
        else:
            sv._hocluc = "Yeu"
    def showSinhVien(self, listSV):
        print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}".format("ID", "Name", "Sex", "Major", "DiemTB", "Hocluc")) 
        if (listSV.__len__() > 0):
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}".format(sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocluc))
        print("\n")
    def getListSinhVien(self):
        return self.list_sinhvien
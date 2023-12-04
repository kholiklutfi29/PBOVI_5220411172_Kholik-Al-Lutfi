class Menu:

    def mainMenu(self):
        print(
            f"""
    Selamat Datang Pada Sistem Perpustakaan
    Aoa Yang ingin anda lakukan?
    1. Input Item Perpustakaan
    2. Cari Item Pada Katalog
    3. Melakukan Aksi Berdasarkan Pengarang
    4. Stop Program
            """
        )
    
    def menu1(self):
        print(
            f"""
    Pilih Item Perpustakaan
        1. Buku
        2. Majalah
        3. DVD
            """
        )
        
    def menu2(self):
        print(
            f"""
    Apa Anda Ingin Melakukan Aksi Lain?
    1. Lihat Lokasi Barang
    2. Info Barang
    3. Kembali
            """
        )
    
    def menu3(self):
        print(
            f"""
    Pilih Item Perpustakaan Yang Akan Dicari
        1. Buku
        2. Majalah
        3. DVD
            """
        )

    def menu4(self):
        print(
            f"""
    Pilih Tindakan
    1. Melihat pengarang yang terdapat di katalog
    2. Mencari apakah terdapat pengarang yang dicari ada pada buku di dalam katalog
            """
        )


class PerpusItem:
    def __init__(self,judul,subyek):
        self.judul = judul
        self.subyek = subyek
        self.lokasi = None
        
    def lokasiPenyimpan(self):
        lokasi = input("Masukkan lokasi menyimpan barang : ")
        self.lokasi = lokasi
    
    def info(self):
        if type(self) == Buku:
            print(
                f"""
                Info Buku
                Judul Buku : {self.judul}
                Subyek Buku : {self.subyek}
                ISBN : {self.isbn}
                Pengarang : {self.pengarang}
                Jumlah Halaman : {self.jmlHal}
                Ukuran : {self.ukuran}
                Lokasi : {self.lokasi}
                """
            )
        elif type(self) == Majalah:
            print(
                f"""
                Info Majalah
                Judul Majalah : {self.judul}
                Subyek Majalah : {self.subyek}
                Volume : {self.volume}
                Issue : {self.issue}
                Lokasi : {self.lokasi}
                """
            )
        elif type(self) == DVD:
            print(
                f"""
                Info DVD
                Judul DVD : {self.judul}
                Subyek DVD : {self.subyek}
                Aktor : {self.aktor}
                Genre : {self.genre}
                Lokasi : {self.lokasi}
                """
            )
                      
        
class Buku(PerpusItem):
    def __init__(self, judul, subyek,isbn, pengarang, jmlHal,ukuran):
        super().__init__(judul, subyek)
        self.lokasi = None
        self.isbn = isbn
        self.pengarang = pengarang
        self.jmlHal = jmlHal
        self.ukuran = ukuran
    
    def lokasiPenyimpan(self):
        return super().lokasiPenyimpan()
      
    def info(self):
        return super().info()
        
    
class Majalah(PerpusItem):
    def __init__(self,judul,subyek,volume,issue):
        super().__init__(judul, subyek)
        self.lokasi = None
        self.volume = volume
        self.issue = issue
    
    def lokasiPenyimpan(self):
        return super().lokasiPenyimpan()
    
    def info(self):
        return super().info()
        
class DVD(PerpusItem):
    def __init__(self, judul,subyek,aktor,genre):
        super().__init__(judul, subyek)
        self.lokasi = None
        self.aktor = aktor
        self.genre = genre
        
    def lokasiPenyimpan(self):
        return super().lokasiPenyimpan()
    
    def info(self):
        return super().info()
       
class Pengarang:
    def __init__(self, nama=None):
        self.nama = nama
        
    def info(self,itemList):
        listPengarang = []
        print("Pengarang : ")
        for item in itemList:
            if isinstance(item,Buku):
                namaPengarang = item.pengarang.nama
                if namaPengarang not in listPengarang:
                    print(item.pengarang.nama, end=" ")
                    listPengarang.append(namaPengarang)
                else:
                    continue
            if itemList == None:
                print("Katalog Buku Kosong!")

    def cari(self,itemList):
        namaPengarang = input("Masukkan Nama Pengarang : ")
        buku_ditemukan = False
        for item in itemList:
            if type(item) == Buku:
                if item.pengarang.nama == namaPengarang:
                    buku_ditemukan = True
                    print("Buku dengan nama pengarang yang anda cari ditemukan!")
                    print(
                f"""
                Info Buku
                Judul Buku : {item.judul}
                Subyek Buku : {item.subyek}
                ISBN : {item.isbn}
                Pengarang : {item.pengarang.nama}
                Jumlah Halaman : {item.jmlHal}
                Ukuran : {item.ukuran}
                Lokasi : {item.lokasi}
                """
            )
            else:
                print("Buku dengan nama pengarang yang anda cari tidak ditemukan!")
        if not buku_ditemukan:
            print("Buku dengan nama pengarang yang Anda cari tidak ditemukan!")
        
class Katalog:
    def cari(self,object):
        judul = input("Masukkan judul yang akan dicari : ")
        for item in object:
            if type(item) == Buku:
                if item.judul == judul:
                    print(f"Buku ditemukan!")
                    print(
                f"""
                Info Buku
                Judul Buku : {item.judul}
                Subyek Buku : {item.subyek}
                ISBN : {item.isbn}
                Pengarang : {item.pengarang.nama}
                Jumlah Halaman : {item.jmlHal}
                Ukuran : {item.ukuran}
                Lokasi : {item.lokasi}
                """
            )
                else:
                    print("Buku tidak ditemukan")
            elif type(item) == Majalah:
                if item.judul == judul:
                    print(f"Majalah ditemukan!")
                    print(
                f"""
                Info Majalah
                Judul Majalah : {item.judul}
                Subyek Majalah : {item.subyek}
                Volume : {item.volume}
                Issue : {item.issue}
                Lokasi : {item.lokasi}
                """
            )
                else:
                    print("Majalah tidak ditemukan")
            elif type(item) == DVD:
                if item.judul == judul:
                    print(f"DVD ditemukan!")
                    print(
                f"""
                Info DVD
                Judul DVD : {item.judul}
                Subyek DVD : {item.subyek}
                Aktor : {item.aktor}
                Genre : {item.genre}
                Lokasi : {item.lokasi}
                """
            )
                else:
                    print("DVD tidak ditemukan")
 
def main():
    katalog = Katalog()
    katalogItem = {
        "Buku" : [],
        "Majalah" : [],
        "DVD" : []
    }
    
    pengarangInstance = Pengarang()

    while True:
        Menu().mainMenu()
        mainInput = int(input("Masukkan Pilihan Anda : "))

        if mainInput == 1:
            Menu().menu1()
            pilihan1 = int(input("Masukkan Pilihan : "))
            if pilihan1 == 1:
                judul = input("Masukkan Judul : ")
                subyek = input("Masukkan Subyek : ")
                isbn = input("Masukkan ISBN : ")
                inputPengarang = input("Masukkan Pengarang : ")
                jmlHal = int(input("Masukkan Jumlah Halaman : "))
                ukuran = input("Masukkan Ukuran : ")
                
                pengarang = Pengarang(nama=inputPengarang)
                buku = Buku(judul,subyek,isbn,pengarang,jmlHal,ukuran)
                buku.lokasiPenyimpan()
                katalogItem["Buku"].append(buku)
                
                Menu().menu2()
                pilihan2 = int(input("Masukkan Pilihan : "))
                
                if pilihan2 == 1:
                    print(f"Lokasi Buku : {buku.lokasi}")
                elif pilihan2 == 2:
                    buku.info()
                elif pilihan2 == 3:
                    continue
                    
            elif pilihan1 == 2:
                judul = input("Masukkan Judul : ")
                subyek = input("Masukkan Subyek : ")
                volume = int(input("Masukkan Volume : "))
                issue = int(input("Masukkan Issue : "))
                
                majalah = Majalah(judul,subyek,volume,issue)
                majalah.lokasiPenyimpan()
                katalogItem["Majalah"].append(majalah)
                
                Menu().menu2()
                pilihan2 = int(input("Masukkan Pilihan : "))
                
                if pilihan2 == 1:
                    print(f"Lokasi Majalah : {majalah.lokasi}")
                elif pilihan2 == 2:
                    majalah.info()
                    
            elif pilihan1 == 3:
                judul = input("Masukkan Judul : ")
                subyek = input("Masukkan Subyek : ")
                aktor = input("Masukkan Aktor : ")
                genre = input("Masukkan Genre : ")
                
                dvd = DVD(judul,subyek,aktor,genre)
                dvd.lokasiPenyimpan()
                katalogItem["DVD"].append(dvd)
                
                Menu().menu2()
                pilihan2 = int(input("Masukkan Pilihan : "))
                
                if pilihan2 == 1:
                    print(f"Lokasi Majalah : {dvd.lokasi}")
                elif pilihan2 == 2:
                    dvd.info()

        elif mainInput == 2:
            Menu().menu3()
            inputJenisItem = int(input("Masukkan Pilihan Anda : "))
            if inputJenisItem == 1:
                katalog.cari(katalogItem["Buku"])
            elif inputJenisItem == 2:
                katalog.cari(katalogItem["Majalah"])
            elif inputJenisItem == 3:
                katalog.cari(katalogItem["DVD"])

        elif mainInput == 3:
            Menu().menu4()
            inputMenuPengarang = int(input("Masukkan Pilihan : "))
            if inputMenuPengarang == 1:
                pengarangInstance.info(katalogItem["Buku"])
            elif inputMenuPengarang == 2:
                pengarangInstance.cari(katalogItem["Buku"])
            else:
                print("Inputan Salah!")
                continue
        
        elif mainInput == 4:
            print("Terima Kasih")
            return
        
    
if __name__ == "__main__":
    main()
    
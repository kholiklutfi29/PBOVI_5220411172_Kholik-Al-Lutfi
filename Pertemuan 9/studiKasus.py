import time
from prettytable import PrettyTable
import os

class Menu:
    def loadingEffect(self, text):
        print(text, end='', flush=True)
        for _ in range(3):
            time.sleep(1)
            print('.', end='', flush=True)
        print(f"\n{text} selesai!")
    
    def mainMenu(self):
        print(
            """
        Ingin berpergian menggunakan kendaraan apa hari ini?
        1. Kereta Api
        2. Mobil
            """
        )

    def menuKeretaLanjutan(self):
        print(
        """
        Pilih Aksi
        1. Tambah Rute
        2. Kurangi Rute
        """
        )
    
    def secondMenu(self):
        print(
            """
        Ingin menggunakan mobil apa?
        1. Mobil Perkotaan
        2. Mobil Balap
        3. Mobil Crossroad
            """
        )
    
    def gerakMobil(self):
        print(
        """
        Insturksi apa yang ingin anda lakukan?:
        1. Maju
        2. Belok
        3. Mundur
        """
        )
    
    def gerakMobilBalap(self):
        print(
        """
        Insturksi apa yang ingin anda lakukan?:
        1. Maju
        2. Belok
        3. Mundur
        4. Aktifkan Race Mode
        """
        )

    def gerakMobilCrossroad(self):
        print(
        """
        Insturksi apa yang ingin anda lakukan?:
        1. Maju
        2. Belok
        3. Mundur
        4. Buka Sunroof
        5. Tutup Sunroof
        """
        )

    def menuKereta(self, object):
        table = PrettyTable()
        table.field_names = ["No","Nama", "Kapasitas", "Jenis Gerbong", "Rute"]
        
        no = 0
        # namaKereta = object dalam dict, kereta = attribut dalam object
        for namaKereta, kereta in object.items():

            # Menggabungkan elemen-elemen dari list rute menjadi satu string
            rute_str = ', '.join(kereta.rute)
            no+=1

            table.add_row([no,kereta.nama, kereta.jumlahKursi, kereta.jenisGerbong, rute_str])

        print(table)

    def menuMobil(self, object):
        table = PrettyTable()
        table.field_names = ["No","Nama", "Jenis ","Kecepatan", "Kapasitas"]
        
        no = 0
        for namaMobil, mobil in object.items():
            no += 1
            table.add_row([no,mobil.nama, mobil.jenisMobil, mobil.kecepatan, mobil.kapasitasPenumpang])

        print(table)

    def menuMobilBalap(self, object):
        table = PrettyTable()
        table.field_names = ["Nama", "Jenis","Kecepatan", "Kapasitas", "Front Wing", "Rear Wing"]

        no = 0

        for namaMobil, mobil in object.items():
            no += 1
            table.add_row([no,mobil.nama, mobil.jenisMobil, mobil.kecepatan, mobil.kapasitasPenumpang, mobil.frontWing, mobil.rearWing])

        print(table)




class KendaraanDarat:
    def __init__(
            self, nama, tahunKeluaran, warna, kecepatan, bahanBakar, jumlahRoda,
            kapasitasPenumpang
    ):
        self.nama = nama
        self.__tahunKeluaran = tahunKeluaran
        self.warna = warna
        self.kecepatan = kecepatan
        self.bahanBakar = bahanBakar
        self.jumlahRoda = jumlahRoda
        self.kapasitasPenumpang = kapasitasPenumpang

    


class Kereta(KendaraanDarat):
    def __init__(self, nama, tahunKeluaran, warna, kecepatan, bahanBakar, kapasitasPenumpang, jenisGerbong, jenisLayananKereta, rute, jumlahRoda = None):
        super().__init__(nama, tahunKeluaran, warna, kecepatan, bahanBakar,kapasitasPenumpang, jumlahRoda)
        self.jenisGerbong = jenisGerbong
        self.jumlahKursi = kapasitasPenumpang
        self.jenisLayananKereta = jenisLayananKereta
        self.rute = rute

    def __tambahRute(self, rute):
        tambahRute = input("Masukkan rute tambahan : ")
        if type(rute) == list:
            rute.append(tambahRute)
            print(f"Rute sekarang : {self.rute}")
        else:
            rute = [rute, tambahRute]
            # rute diubah menjadi list baru yang berisi elemen pertama, yaitu nilai awal dari rute, dan elemen kedua, yaitu tambahRute
        return rute
    
    def __kurangiRute(self, rute):
        kurangiRute = input("Masukkan rute yang akan dikurangi : ")
        if type(rute) == list:
            rute.remove(kurangiRute)
            print(f"Rute sekarang : {self.rute}")
        else:
            rute = [rute]
        return rute
    


class Mobil(KendaraanDarat):
    def __init__(self, nama, tahunKeluaran, warna, kecepatan, bahanBakar, jumlahRoda, kapasitasPenumpang, jenisMobil):
        super().__init__(nama, tahunKeluaran, warna, kecepatan, bahanBakar, jumlahRoda, kapasitasPenumpang)
        self.jenisMobil = jenisMobil
        self.instruksi = []

    def startEngine(self):
        vroom = input("Ingin nyalakan mesin? (y/n) : ").upper()
        if vroom == "Y":
            print("Mesin nyala")
        else:
            print("Gagal menerima instruksi")
    
    def stopEngine(self):
        vroom = input("Ingin matikan mesin? (y/n) : ").upper()
        if vroom == "Y":
            print("Mesin Dimatikan")
        else:
            print("Gagal menerima instruksi")
    
    def maju(self):
        print("Mobil bergerak ke depan")
        return self.instruksi.append("Maju")
    
    def mundur(self):
        print("Mobil bergerak ke belakang")
        return self.instruksi.append("Mundur")
    
    def belok(self):
        print("Mobil bergerak ke samping")
        return self.instruksi.append("Belok")
    
    



class MobilBalap(Mobil):
    def __init__(self, nama, tahunKeluaran, warna, kecepatan, bahanBakar, jumlahRoda, kapasitasPenumpang, jenisMobil, frontWing, rearWing):
        super().__init__(nama, tahunKeluaran, warna, kecepatan, bahanBakar, jumlahRoda, kapasitasPenumpang, jenisMobil)
        self.frontWing = frontWing
        self.rearWing = rearWing
        self.instruksi = []

    def startEngine(self):
        return super().startEngine()
    
    def stopEngine(self):
        return super().stopEngine()
    
    def maju(self):
        return super().maju()
    
    def mundur(self):
        return super().mundur()
    
    def belok(self):
        return super().belok()
    
    def race(self):
        confirm = input("Apakah anda ingin mengaktifkan race mode? (y/n) : ").upper()
        if confirm == "Y":
            print("Mode Race diaktifkan, bersiap untuk kenaikkan kecepatan yang drastis!")
        elif confirm == "N":
            print("Mode aman")
        else:
            print("Gagal memberikan keputusan")
    


class MobilCrossroad(Mobil):
    def __init__(self, nama, tahunKeluaran, warna, kecepatan, bahanBakar, jumlahRoda, kapasitasPenumpang, jenisMobil):
        super().__init__(nama, tahunKeluaran, warna, kecepatan, bahanBakar, jumlahRoda, kapasitasPenumpang, jenisMobil)

    def startEngine(self):
        return super().startEngine()
    
    def stopEngine(self):
        return super().stopEngine()
    
    def maju(self):
        return super().maju()
    
    def mundur(self):
        return super().mundur()
    
    def belok(self):
        return super().belok()
    
    def sunroofTerbuka(self):
        Menu().loadingEffect("Membuka sunroof")
        print(
            """
            Sunroof Terbuka!
            Mohon tutup sunroof ketika hujan, untuk menghindari kerusakan pada bagian dalam mobil
            """
        )
    
    def sunroofTertutup(self):
        Menu().loadingEffect("Menutup sunroof")
        print("Sunroof Tertutup!")


class ProgramEngine:
    
    def Journey(self):

        # init kendaraan
        kereta = self.initKereta()
        mobil = self.initMobil()
        mobilBalap = self.initMobilBalap()
        mobilCrossroad = self.initMobilCrossroad()

        while True:
            Menu().mainMenu()

            firstInput = int(input("Masukkan pilihan anda : "))
            if firstInput == 1:
                Menu().menuKereta(kereta)
                self.pilihKereta(kereta)
            elif firstInput == 2:
                Menu().secondMenu()
                secondInput = int(input("Masukkan Input Anda : "))
                if secondInput == 1:
                    Menu().menuMobil(mobil)
                    self.pilihKendaraan(mobil)
                elif secondInput == 2:
                    Menu().menuMobil(mobilBalap)
                    self.pilihKendaraan(mobilBalap)
                elif secondInput == 3:
                    Menu().menuMobil(mobilCrossroad)
                    self.pilihKendaraan(mobilCrossroad)
            else:
                print("Inputan Salah!")
                Menu().loadingEffect("Menghapus command line")
                os.system("cls")
                continue

    def initKereta(self):
            kereta1 = Kereta(
                "KA 159-Joglosemarkerto","2008","Putih",
                200, "Biosolar",200,"Bisnis","Kereta Antarkota",
                ["Purwokerto", "Bumiayu", "Prupuk", "Slawi", "Tegal"]
            )
            kereta2 = Kereta(
                "KA 163-Joglosemarkerto","2012","Merah",
                200, "Biosolar",300,"Eksekutif","Kereta Antarkota",
                ["Solo", "Kalioso", "Gundih", "Telawa", "Kedungjati","Brumbung", "Semarang Tawang"]
            )
            kereta3 = Kereta(
                "KA 171-Joglosemarkerto","2015","Biru",
                200, "Biosolar",400,"Ekonomi","Kereta Antarkota",
                ["Yogyakarta", "Wates", "Kutoarjo", "Kebumen", "Karanganyar","Gombong","Sumpiuh","Kroya","Maos","Gumilir","Cilacap"]
            )
            dictKereta = {
                "kereta1" : kereta1,
                "kereta2" : kereta2,
                "kereta3" : kereta3
            }
            return dictKereta

    def initMobil(self):
            mobil1 = Mobil("Toyota Camry","2020","Hitam",180,"Bensin","4","5","Sedan")
            mobil2 = Mobil("Honda Civic", "2018", "Merah", 200,"Bensin","4","5","Sedan")
            mobil3 = Mobil("Daihatsu Xenia", "2019", "Maroon", 180,"Bensin","4","7","MPV")
            dictMobil = {
                "mobil1" : mobil1,
                "mobil2" : mobil2,
                "mobil3" : mobil3
            }
            return dictMobil

    def initMobilBalap(self):
            mobilBalap1 = MobilBalap("Mercedes-AMG Petronas Formula One Team - W12", "2021", "Merah", 330, "Bensin", "4", "2", "Supersport", "Stable-GT", "Stable-GT")
            mobilBalap2 = MobilBalap("Nissan GT-R R35", "2022", "Hitam", 300, "Bensin", "4", "4", "Coupe", "Aerodynamic", "Aerodynamic")
            mobilBalap3 = MobilBalap("Porsche 911 RSR","2020","Putih",290,"Bensin","4","1","GT racing car","Aerodynamic","Aerodynamic")
            dictMobilBalap = {
                "mobilBalap1" : mobilBalap1,
                "mobilBalap2" : mobilBalap2,
                "mobilBalap3" : mobilBalap3
            }
            return dictMobilBalap
    
    def initMobilCrossroad(self):
        crossroad1 = MobilCrossroad("Toyota RAV4","2020","Putih",180,"Bensin","4","5","SUV")
        crossroad2 = MobilCrossroad("Honda CR-V","2021","Hitam",193,"Bensin","4","5","SUV")
        crossroad3 = MobilCrossroad("Nissan X-Trail","2019","Putih",184,"Bensin","4","5-7","SUV")
        dictMobilCrossroad = {
            "crossroad1" : crossroad1,
            "crossroad2" : crossroad2,
            "crossroad3" : crossroad3
        }
        return dictMobilCrossroad
    
    def processKereta(self,object):
        firstInput = int(input("Masukkan pilihan anda : "))
        if firstInput == 1:
            object._Kereta__tambahRute(object.rute)
        elif firstInput == 2:
            object._Kereta__kurangiRute(object.rute)
    
    def pilihKereta(self,object):
        inputKereta = int(input("Masukkan pilihan anda (angka) : "))
        if inputKereta == 1:
            print(f"\n{object['kereta1'].nama} telah dipilih!")
            Menu().menuKeretaLanjutan()
            self.processKereta(object['kereta1'])
        elif inputKereta == 2:
            print(f"\n{object['kereta2'].nama} telah dipilih!")
            Menu().menuKeretaLanjutan()
            self.processKereta(object['kereta2'])
        elif inputKereta == 3:
            print(f"\n{object['kereta3'].nama} telah dipilih!")
            Menu().menuKeretaLanjutan()
            self.processKereta(object['kereta3'])

    
    def fractionPilihMobilPerkotaan(self,object,mobilKey):
        print(
            f"""
Mobil Yang dipakai saat ini :

            Mobil : {object[mobilKey].nama}
            Jenis Mobil : {object[mobilKey].jenisMobil}
            Tahun Keluaran: {object[mobilKey]._KendaraanDarat__tahunKeluaran}
            Kecepatan : {object[mobilKey].kecepatan} KM/H
            Kapasitas Penumpang : {object[mobilKey].kapasitasPenumpang}
            """
        )
        # _KendaraanDarat__tahunKeluaran -> karena tahun keluaran terletak pada kelas Kendaraan Darat
        # atribut tersebut bukan merupakan bagian dari kelas Mobil. Berikut adalah koreksi yang sesuai
        object[mobilKey].startEngine()
        print("")
        Menu().gerakMobil()
        while True:
            thirdInput = int(input("Masukkan inputan anda : "))
            if thirdInput == 1:
                object[mobilKey].maju()
                fourthInput = input("Ingin memberi instruksi lagi? (y/n) : ").upper()
                if fourthInput == "Y":
                    continue
                elif fourthInput == "N":
                    object[mobilKey].stopEngine()
                    print(f"instruksi yang dilakukan : {object[mobilKey].instruksi}")
                    return
            elif thirdInput == 2:
                object[mobilKey].belok()
                fourthInput = input("Ingin memberi instruksi lagi? (y/n) : ").upper()
                if fourthInput == "Y":
                    continue
                elif fourthInput == "N":
                    object[mobilKey].stopEngine()
                    print(f"instruksi yang dilakukan : {object[mobilKey].instruksi}")
                    return
            elif thirdInput == 3:
                object[mobilKey].mundur()
                fourthInput = input("Ingin memberi instruksi lagi? (y/n) : ").upper()
                if fourthInput == "Y":
                    continue
                elif fourthInput == "N":
                    object[mobilKey].stopEngine()
                    print(f"instruksi yang dilakukan : {object[mobilKey].instruksi}")
                    return
        
    def fractionPilihMobilBalap(self,object,mobilKey):
        print(
            f"""
Mobil Yang dipakai saat ini :

            Mobil : {object[mobilKey].nama}
            Jenis Mobil : {object[mobilKey].jenisMobil}
            Tahun Keluaran: {object[mobilKey]._KendaraanDarat__tahunKeluaran}
            Kecepatan : {object[mobilKey].kecepatan} KM/H
            Kapasitas Penumpang : {object[mobilKey].kapasitasPenumpang}
            Front Wing : {object[mobilKey].frontWing}
            Rear Wing : {object[mobilKey].rearWing}
            """
        )
        object[mobilKey].startEngine()
        print("")
        Menu().gerakMobilBalap()
        while True:
            thirdInput = int(input("Masukkan inputan anda : "))
            if thirdInput == 1:
                object[mobilKey].maju()
                fourthInput = input("Ingin memberi instruksi lagi? (y/n) : ").upper()
                if fourthInput == "Y":
                    continue
                elif fourthInput == "N":
                    object[mobilKey].stopEngine()
                    print(f"instruksi yang dilakukan : {object[mobilKey].instruksi}")
                    return
            elif thirdInput == 2:
                object[mobilKey].belok()
                fourthInput = input("Ingin memberi instruksi lagi? (y/n) : ").upper()
                if fourthInput == "Y":
                    continue
                elif fourthInput == "N":
                    object[mobilKey].stopEngine()
                    print(f"instruksi yang dilakukan : {object[mobilKey].instruksi}")
                    return
            elif thirdInput == 3:
                object[mobilKey].mundur()
                fourthInput = input("Ingin memberi instruksi lagi? (y/n) : ").upper()
                if fourthInput == "Y":
                    continue
                elif fourthInput == "N":
                    object[mobilKey].stopEngine()
                    print(f"instruksi yang dilakukan : {object[mobilKey].instruksi}")
                    return
            elif thirdInput == 4:
                object['mobilBalap1'].race()
                fourthInput = input("Ingin memberi instruksi lagi? (y/n) : ").upper()
                if fourthInput == "Y":
                    continue
                elif fourthInput == "N":
                    object['mobilBalap1'].stopEngine()
                    print(f"instruksi yang dilakukan : {object['mobilBalap1'].instruksi}")
                    return
    
    def fractionMobilCrossroad(self,object,mobilKey):
        print(
            f"""
Mobil Yang dipakai saat ini :

            Mobil : {object[mobilKey].nama}
            Jenis Mobil : {object[mobilKey].jenisMobil}
            Kecepatan : {object[mobilKey].kecepatan} KM/H
            Kapasitas Penumpang : {object[mobilKey].kapasitasPenumpang}
            Tahun Keluaran: {object[mobilKey]._KendaraanDarat__tahunKeluaran} 
            """
        )
        object[mobilKey].startEngine()
        print("")
        Menu().gerakMobilCrossroad()
        while True:
            thirdInput = int(input("Masukkan inputan anda : "))
            if thirdInput == 1:
                object[mobilKey].maju()
                fourthInput = input("Ingin memberi instruksi lagi? (y/n) : ").upper()
                if fourthInput == "Y":
                    continue
                elif fourthInput == "N":
                    object[mobilKey].stopEngine()
                    print(f"instruksi yang dilakukan : {object[mobilKey].instruksi}")
                    return
            elif thirdInput == 2:
                object[mobilKey].belok()
                fourthInput = input("Ingin memberi instruksi lagi? (y/n) : ").upper()
                if fourthInput == "Y":
                    continue
                elif fourthInput == "N":
                    object[mobilKey].stopEngine()
                    print(f"instruksi yang dilakukan : {object[mobilKey].instruksi}")
                    return
            elif thirdInput == 3:
                object[mobilKey].mundur()
                fourthInput = input("Ingin memberi instruksi lagi? (y/n) : ").upper()
                if fourthInput == "Y":
                    continue
                elif fourthInput == "N":
                    object[mobilKey].stopEngine()
                    print(f"instruksi yang dilakukan : {object[mobilKey].instruksi}")
                    return
            elif thirdInput == 4:
                object[mobilKey].sunroofTerbuka()
                fourthInput = input("Ingin memberikan instruksi lagi? (y/n) : ").upper()
                if fourthInput == "Y":
                    continue
                elif fourthInput == "N":
                    object[mobilKey].stopEngine()
                    print(f"instruksi yang dilakukan : {object[mobilKey].instruksi}")
                    return
            elif thirdInput == 5:
                object[mobilKey].sunroofTertutup()
                fourthInput = input("Ingin memberi instuksi lagi? (y/n) : ").upper()
                if fourthInput == "Y":
                    continue
                elif fourthInput == "N":
                    object[mobilKey].stopEngine()
                    print(f"instruksi yang dilakukan : {object[mobilKey].instruksi}")
                    return
            
    def pilihMobilPerkotaan(self,object):
        inputKendaran = int(input("Masukkan pilihan anda : "))
        if inputKendaran == 1:
            self.fractionPilihMobilPerkotaan(object,'mobil1')
        elif inputKendaran == 2:
            self.fractionPilihMobilPerkotaan(object,'mobil2')
        elif inputKendaran == 3:
            self.fractionPilihMobilPerkotaan(object,'mobil3')
    
    def pilihMobilBalap(self,object):
        inputKendaran = int(input("Masukkan pilihan anda : "))
        if inputKendaran == 1:
            self.fractionPilihMobilBalap(object,'mobilBalap1')
        elif inputKendaran == 2:
            self.fractionPilihMobilBalap(object, 'mobilBalap2')
        elif inputKendaran == 3:
            self.fractionPilihMobilBalap(object, 'mobilBalap3')

    
    def pilihMobilCrossroad(self,object):
        inputKendaran = int(input("Masukkan pilihan anda : "))
        if inputKendaran == 1:
            self.fractionMobilCrossroad(object,'crossroad1')
        elif inputKendaran == 2:
            self.fractionMobilCrossroad(object,'crossroad2')
        elif inputKendaran == 3:
            self.fractionMobilCrossroad(object,'crossroad3')

    def pilihKendaraan(self,dict):
        # dict.values() -> mengambil semua nilai values pada dict
        # iter() -> membuat iterator dari kumpulan nilai tersebut
        # next() -> mengambil elemen pertama dari iterator
        nilaiPertama = next(iter(dict.values()))
        tipeData = type(nilaiPertama)
        if tipeData is Mobil:
            self.pilihMobilPerkotaan(dict)
        elif tipeData is MobilBalap:
            self.pilihMobilBalap(dict)
        elif tipeData is MobilCrossroad:
            self.pilihMobilCrossroad(dict)              

if __name__ == "__main__":
    program = ProgramEngine()
    program.Journey()
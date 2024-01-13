import random
import time
import os
from prettytable import PrettyTable
from mysql.connector import connect,Error,IntegrityError

class Menu:
    def mainMenu(self):
        print(
        """
    Selamat Datang Di Rumah Sakit Sejahtera
    1. Daftar Pasien Baru
    2. Sudah Pernah daftar
    3. Riwayat 
    4. Daftar Patient
    5. Update Data
    6. Delete Data
        """
    )
        
    def secondMenu(self):
        print(
        """
    Jenis Pelayan apa yang akan dipilih? :
    1. Rawat Jalan
    2. Rawat Inap
    3. Unit Perawatan Intensif
        """
    )
    
    def loadingEffect(self, text,text2):
        print(text, end='', flush=True)
        for _ in range(3):
            time.sleep(1)
            print('.', end='', flush=True)
        print(f"\n{text2}")

    def printHistory(self, dict):
        for treatmentType, treatments in dict.items():
            if treatments:
                table = PrettyTable()
                treatment = treatments[0]  # Ambil objek pertama untuk mendapatkan field names, cara mengambil key : treatment.__dict__.keys()
                table.field_names = treatment.field_names

                for treatment in treatments:
                    if type(treatment) is OutpatientCare:
                        table.add_row([treatment.name,treatment.age,treatment._MedicalTreatment__healthInsuranceCard,treatment.discount,treatment.noOC])
                    elif type(treatment) is Hospitalization :
                        table.add_row([treatment.name,treatment.age,treatment._MedicalTreatment__healthInsuranceCard,treatment.date,treatment.room,treatment.noHospitalization])
                    elif type(treatment) is ICU:
                        table.add_row([treatment.name,treatment.age,treatment._MedicalTreatment__healthInsuranceCard,treatment.date,treatment.roomPrice,treatment.noICU])

                table.title = f"Riwayat {treatmentType}"
                print("\n")
                print(table)
            else:
                print(f"\nRiwayat {treatmentType} kosong.")
                
    def printPatient(self,dict):
        table = PrettyTable()
        table.field_names = ["No","Nama","Umur","Jenis Kartu Asuransi"]

        no = 0
        for patientType, patiens in dict.items():
            no += 1
            table.add_row([no,patiens.name,patiens.age,patiens._MedicalTreatment__healthInsuranceCard])
        print(table)
            
class Database:
    def connection(self):
        connection = None
        try:
            connection = connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "5220411172"
            )
            print("Berhasil terkoneksi dengan database")
        except Error as e:
            print(e)
        return connection
    
    def createDatabase(self,conn):
        query = "CREATE DATABASE IF NOT EXISTS db_hospital"
        with conn.cursor() as cur:
            cur.execute(query)
    
    def createTableOC(self,conn):
        query = """
        CREATE TABLE IF NOT EXISTS outpatient_care(
        nama VARCHAR(25) PRIMARY KEY NOT NULL,
        umur VARCHAR(25) NOT NULL,
        jenis_kartu_asuransi VARCHAR(25) NOT NULL,
        discount VARCHAR(25) NOT NULL,
        no_rawat_jalan VARCHAR(25) NOT NULL
        )
        """
        with conn.cursor() as cur:
            cur.execute(query)
            conn.commit()
    
    def createTableHO(self,conn):
        query = """
        CREATE TABLE IF NOT EXISTS hospitalization(
        nama VARCHAR(25) PRIMARY KEY NOT NULL,
        umur VARCHAR(25) NOT NULL,
        jenis_kartu_asuransi VARCHAR(25) NOT NULL,
        tanggal_mulai_rawat VARCHAR(25) NOT NULL,
        ruangan VARCHAR(25) NOT NULL,
        no_rawat_inap VARCHAR(25) NOT NULL
        )
        """
        with conn.cursor() as cur:
            cur.execute(query)
            conn.commit()
    

    def createTableICU(self,conn):
        query = """
        CREATE TABLE IF NOT EXISTS icu(
        nama VARCHAR(25) PRIMARY KEY NOT NULL,
        umur VARCHAR(25) NOT NULL,
        jenis_kartu_asuransi VARCHAR(25) NOT NULL,
        tanggal_mulai_rawat VARCHAR(25) NOT NULL,
        biaya_kamar INT(10) NOT NULL,
        no_icu VARCHAR(25) NOT NULL
        )
        """
        with conn.cursor() as cur:
            cur.execute(query)
            conn.commit()
    
    def createTableDataPatient(self, conn):
        query = """
        CREATE TABLE IF NOT EXISTS data_patient(
        nama VARCHAR(25) PRIMARY KEY NOT NULL,
        umur VARCHAR(25) NOT NULL,
        jenis_kartu_asuransi VARCHAR(25) NOT NULL
        )
        """
        with conn.cursor() as cur:
            cur.execute(query)
            conn.commit()

    def insertData(self, conn, object):
        try:
            with conn.cursor() as cur:
                if type(object) is OutpatientCare:
                    cur.execute(f"""INSERT INTO outpatient_care(nama, umur, jenis_kartu_asuransi, discount, no_rawat_jalan) VALUES (
                                '{object.name}', {object.age}, '{object._MedicalTreatment__healthInsuranceCard}', '{object.discount}',
                                '{object.noOC}'
                    )""")
                    conn.commit()
                elif type(object) is Hospitalization:
                    cur.execute(f"""INSERT INTO hospitalization(nama, umur, jenis_kartu_asuransi, tanggal_mulai_rawat, ruangan, no_rawat_inap) VALUES (
                                '{object.name}', {object.age}, '{object._MedicalTreatment__healthInsuranceCard}', '{object.date}',
                                '{object.room}','{object.noHospitalization}'
                    )""")
                    conn.commit()
                elif type(object) is ICU:
                    cur.execute(f"""INSERT INTO ICU(nama, umur, jenis_kartu_asuransi, tanggal_mulai_rawat, biaya_kamar,no_icu) VALUES (
                                '{object.name}', {object.age}, '{object._MedicalTreatment__healthInsuranceCard}', '{object.date}',
                                {object.roomPrice},'{object.noICU}'
                    )""")
                    conn.commit()
        except:
            print(f"Pasien dengan nama {object.name} sudah ada dalam database")

    
    def insertDataPatient(self, conn, object):
        try:
            with conn.cursor() as cur:
                cur.execute(f"INSERT INTO data_patient(nama, umur, jenis_kartu_asuransi) VALUES('{object.name}', {object.age}, '{object._MedicalTreatment__healthInsuranceCard}')")
                conn.commit()
                print("Data berhasil diinput")
        except:
            print("Data gagal diinput")

    def updateDate(self, conn):
        table = input("Pilih tabel : ")
        oldName = input("Masukkan nama pasien yang ingin diganti dari database : ")
        newName = input("Nama baru : ")
        try:
            with conn.cursor() as cur:
                cur.execute(f"""UPDATE {table} 
                            SET nama = '{newName}'
                            WHERE nama = '{oldName}'
                """)
                conn.commit()
                print("Data berhsil diupdate")
        except Error as e:
            print(e)
    
    def deleteData(self, conn):
        table = input("Pilih tabel : ")
        name = input("Masukkan nama pasien yang ingin dihapus dari database : ")
        try:
            with conn.cursor() as cur:
                cur.execute(f"DELETE FROM {table} WHERE nama = '{name}'")
                conn.commit()
                print("Data berhasil dihapus")
        except:
            print("Data gagal dihapus")

    def printDatabase(self, conn, tabelDB):
        query = f"SELECT * FROM {tabelDB}"
        try:
            with conn.cursor() as cur:
                cur.execute(query)
                Menu().loadingEffect("Tunggu sebentar", "Database ditampilkan")
                result = cur.fetchall()
                self.printHistoryDB(tabelDB, result)
        except:
            print("Tabel Kosong")

    def printHistoryDB(self, tableDB, result):
        table = PrettyTable()

        if tableDB == "outpatient_care":
            table.field_names = ["Nama", "Umur", "Jenis Kartu Asuransi", "Discount", "No. Rawat Jalan"]
            for row in result:
                table.add_row(row)
        elif tableDB == "hospitalization":
            table.field_names = ["Nama", "Umur", "Jenis Kartu Asuransi", "Tanggal Mulai Rawat", "Ruangan", "No. Rawat Inap"]
            for row in result:
                table.add_row(row)
        elif tableDB == "icu":
            table.field_names = ["Nama", "Umur", "Jenis Kartu Asuransi", "Tanggal Mulai Rawat", "Biaya Kamar", "No. ICU"]
            for row in result:
                table.add_row(row)
        elif tableDB == "data_patient":
            table.field_names = ["Nama", "Umur", "Jenis Kartu Asuransi"]
            for row in result:
                table.add_row(row)

        table.title = f"Riwayat {tableDB.upper()}"
        print(table)
        print("\n")
        
        

class MedicalTreatment:
    def __init__(self,name,age,healthInsuranceCard):
        self.name = name
        self.age = age
        self.__healthInsuranceCard = healthInsuranceCard
         
    def __generateCode(self,jenisPerawatan):
        randomNumber = random.randint(100,999)
        treatmentNumber = f"{jenisPerawatan}{randomNumber}"
        return treatmentNumber
    

# kelas rawat jalan
class OutpatientCare(MedicalTreatment):
    def __init__(self, name, age, healthInsuranceCard):
        super().__init__(name, age, healthInsuranceCard)
        self.discount = None
        self.noOC = None
        

    def __generateCode(self, jenisPerawatan):
        return super().__generateCode(jenisPerawatan)
    
    def payment(self,cardType):
        if cardType == "basic":
            print("Get discount 20%")
            self.discount =  "discount 20%"
        elif cardType == "standart":
            print("Get discount 40%")
            self.discount = "discount 40%"
        elif cardType == "premium":
            print("Get discount 60%")
            self.discount = "discount 60%"


# kelas rawat inap
class Hospitalization(MedicalTreatment):
    def __init__(self, name, age, healthInsuranceCard, date):
        super().__init__(name, age, healthInsuranceCard)
        self.date = date
        self.room = None
        self.noHospitalization = None
        

    def __generateCode(self, jenisPerawatan):
        return super().__generateCode(jenisPerawatan)
    
    def chooseRoom(self):
        print(
        """
        Pilih Ruangan :
        1. Dahlia
        2. Kenanga
        3. Anggrek
        """
        )
        roomChoice = int(input("Masukkan pilihan ruangan: "))
        if roomChoice == 1:
            self.room = "Dahlia"
        elif roomChoice == 2:
            self.room = "Kenanga"
        elif roomChoice == 3:
            self.room = "Anggrek"

# kelas unit perawatan intensif (Intensif Care Unit)
class ICU(Hospitalization):
    def __init__(self, name, age, healthInsuranceCard, date):
        super().__init__(name, age, healthInsuranceCard, date)
        self.roomPrice = None
        self.noICU = None
        
        
    
    def __generateCode(self, jenisPerawatan):
        return super().__generateCode(jenisPerawatan)
    
    def calculateICURoomCost(self):
        roomPrice = 2000000
        dayStayed = int(input("Perkiraan lama tinggal (hari) : "))

        totalPrice = roomPrice * dayStayed
        print(f"Biaya kamar : {totalPrice} (belum termasuk biaya perawatan dan obat)")
        self.roomPrice = totalPrice
    




class Hospital:

    def printData(self,object):
        if type(object) is OutpatientCare:
            print(
            f"""
    Pasien Berhasil Diinputkan!
    Identitas Patient :
        Nama : {object.name}
        Umur : {object.age}
        Jenis Kartu Asuransi : {object._MedicalTreatment__healthInsuranceCard}
        No. Rawat Jalan : {object.noOC}
    """
        )
        elif type(object) is Hospitalization:
            print(
            f"""
    Pasien Berhasil Diinputkan!
    Identitas Patient :
        Nama : {object.name}
        Umur : {object.age}
        Jenis Kartu Asuransi : {object._MedicalTreatment__healthInsuranceCard}
        Tanggal Mulai Rawat : {object.date}
        Ruangan : {object.room}
        No. Rawat Inap : {object.noHospitalization}
    """
        )
        elif type(object) is ICU:
            print(
            f"""
    Pasien Berhasil Diinputkan!
    Identitas Patient :
        Nama : {object.name}
        Umur : {object.age}
        Jenis Kartu Asuransi : {object._MedicalTreatment__healthInsuranceCard}
        Tanggal Mulai Rawat : {object.date}
        Biaya Kamar : Rp {object.roomPrice}
        No. ICU : {object.noICU}
    """
        )
            
            
    
    def treatPatient(self, treatmentClass, conn, *args):
        dbInstance = Database()
        treatment = treatmentClass(*args)
        treatmentCode = treatment._MedicalTreatment__generateCode(treatmentClass.__name__.upper()[:3])
        
        # Penyesuaian atribut berdasarkan jenis perawatan
        if type(treatment) is OutpatientCare:
            treatment.noOC = treatmentCode
            treatment.payment(treatment._MedicalTreatment__healthInsuranceCard)
            dbInstance.insertData(conn,treatment)
            self.printData(treatment)
        elif type(treatment) is Hospitalization:
            treatment.noHospitalization = treatmentCode
            treatment.chooseRoom()
            dbInstance.insertData(conn,treatment)
            self.printData(treatment)
        elif type(treatment) is ICU:
            treatment.noICU = treatmentCode
            treatment.calculateICURoomCost()
            dbInstance.insertData(conn,treatment)
            self.printData(treatment)

    
    def searchPatient(self, conn):
        patientName = input('Nama pasien : ')
        patientFound = False  # Inisialisasi variabel untuk melacak apakah pasien ditemukan atau tidak

        Menu().loadingEffect("Mencari pasien berdasarkan nama", "pasien ditemukan")

        # Assuming data_patient is the name of the table in your database
        query = f"SELECT * FROM data_patient WHERE nama = '{patientName}'"
        with conn.cursor() as cur:
            cur.execute(query)
            result = cur.fetchone()

        if result:
            patientFound = True  # Set variabel ke True ketika pasien ditemukan
            patientObject = result 

            Menu().secondMenu()
            choice2 = int(input("Masukkan pilihan anda : "))
            if choice2 == 1:
                self.treatPatient(OutpatientCare, conn,patientObject[0], patientObject[1], patientObject[2])
            elif choice2 == 2:
                date = input("Inputkan tanggal : ")
                self.treatPatient(Hospitalization, conn, patientObject[0], patientObject[1], patientObject[2], date)
            elif choice2 == 3:
                date = input("Inputkan tanggal : ")
                self.treatPatient(ICU, conn, patientObject[0], patientObject[1], patientObject[2], date)
        else:
            print("Pasien tidak ditemukan.")
    
    def newPatient(self,conn):
        dbInstance = Database()
        while True:
            patientName = input('Nama pasien baru : ')
            patientAge = int(input('Usia pasien baru : '))
            healthInsurance = input('Jenis kartu asuransi anda (basic, standart, premium) : ')

            # make object patient
            patient = MedicalTreatment(patientName,patientAge,healthInsurance)

            Menu().secondMenu()
            choice2 = int(input("Masukkan pilihan anda : "))
            if choice2 == 1:
                self.treatPatient(OutpatientCare,conn,patient.name,patient.age,patient._MedicalTreatment__healthInsuranceCard)
                dbInstance.insertDataPatient(conn,patient)
                choice3 = input("Ingin menginput lagi? (y/n) : ").upper()
                if choice3 == "Y":
                    continue
                elif choice3 == "N":
                    print("Terima Kasih")
                    return
            elif choice2 == 2:
                date = input("Inputkan tanggal : ")
                self.treatPatient(Hospitalization,conn,patient.name,patient.age,patient._MedicalTreatment__healthInsuranceCard,date)
                dbInstance.insertDataPatient(conn,patient)
                choice3 = input("Ingin menginput lagi? (y/n) : ").upper()
                if choice3 == "Y":
                    continue
                elif choice3 == "N":
                    print("Terima Kasih")
                    return
            elif choice2 == 3:
                date = input("Inputkan tanggal : ")
                self.treatPatient(ICU,conn,patient.name,patient.age,patient._MedicalTreatment__healthInsuranceCard,date)
                dbInstance.insertDataPatient(conn,patient)
                choice3 = input("Ingin menginput lagi? (y/n) : ").upper()
                if choice3 == "Y":
                    continue
                elif choice3 == "N":
                    print("Terima Kasih")
                    return

    def process(self):

        # database instance
        dbInstance = Database()

        # init connection database
        connection = dbInstance.connection()

        # make database
        database = dbInstance.createDatabase(connection)

        # make table
        outpatientCare = dbInstance.createTableOC(connection)
        hospitalization = dbInstance.createTableHO(connection)
        icu = dbInstance.createTableICU(connection)
        dataPatient = dbInstance.createTableDataPatient(connection)

        while True:
            Menu().mainMenu()
            choice = int(input("Masukkan pilihan anda : "))
            if choice == 1:
                self.newPatient(connection)
            elif choice == 2:
                self.searchPatient(connection)
            elif choice == 3:
                dbInstance.printDatabase(connection,"outpatient_care")
                dbInstance.printDatabase(connection,"hospitalization")
                dbInstance.printDatabase(connection,"icu")
            elif choice == 4:
                dbInstance.printDatabase(connection,"data_patient")
            elif choice == 5:
                dbInstance.updateDate(connection)
            elif choice == 6:
                dbInstance.deleteData(connection)
            else:
                print("Inputan Salah!")
                Menu().loadingEffect("Menghapus command line", "command line selesai dihapus")
                os.system("cls")
                continue


if __name__ == "__main__":
    Hospital().process()
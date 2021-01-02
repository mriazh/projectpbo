import sqlite3

class Database:
    def __init__(self):
        self.connector = sqlite3.connect("main.db")
        self.cursor = self.connector.cursor()
        
    def executeQuery(self, query):
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        self.connector.commit()
        return data
    
class User(Database):
    def __init__(self):
        Database.__init__(self)
        self.username = None
        self.password = None
        
    def register(self, username, password):
        query = 'INSERT INTO tb_userdata (username, password) \
                VALUES (\'%s\', \'%s\')'
        query = query % (username, password)
        self.executeQuery(query)
        self.username = username
        self.password = password
        print(f"Pembuatan akun berhasil.\nSelamat datang {self.username} di Bus Management Jember!")
    
    def login(self, username, password):
        query = 'SELECT username, password FROM tb_userdata \
            where username=\'%s\' and password=\'%s\' '
        query = query % (username, password)
        data_login = self.executeQuery(query)
        confirm = False
        for i in data_login:
            if username == i[0] and password == i[1]:
                confirm = True
                self.username = i[0]
                self.password = i[1]
                print(f"Login berhasil. Selamat datang {self.username} di Bus Management Jember!")
        if confirm == False:
            print(f"Username '{username}' atau password '{password}' tidak ditemukan, harap dicek kembali atau melakukan registrasi")
    
    def jenis_bus(self, jenis, kelas):
        tambahan = 0
        tipe = 0
        if kelas == '1':
            tambahan = 100000
            tipe = 'Bus Sinar Jaya'
        elif kelas == '2':
            tambahan = 50000
            tipe = 'Bus Lorena'
        elif kelas == '3':
            tambahan = 10000
            tipe = 'Bus Maju Lancar'
        else:
            print("Masukkan angka sesuai pilihan yang ada.")
        
        if jenis == '1':
            print("Banyuwangi")
            print(tambahan + 100000,f"{tipe}")
        elif jenis == '2':
            print("Bondowoso")
            print(tambahan + 80000,f"{tipe}")
        elif jenis == '3':
            print("Situbondo")
            print(tambahan + 90000,f"{tipe}")
        elif jenis == '4':
            print("Probolinggo")
            print(tambahan + 95000,f"{tipe}")
        elif jenis == '5':
            print("Lumajang")
            print(tambahan + 85000,f"{tipe}")
        elif jenis == '6':
            print("Malang")
            print(tambahan + 150000,f"{tipe}")
        elif jenis == '7':
            print("Pasuruan")
            print(tambahan + 180000,f"{tipe}")
        elif jenis == '8':
            print("Sidoarjo")
            print(tambahan + 250000,f"{tipe}")
        elif jenis == '9':
            print("Mojokerto")
            print(tambahan + 240000,f"{tipe}")
        elif jenis == '10':
            print("Blitar")
            print(tambahan + 230000,f"{tipe}")
        else:
            print("Masukkan angka sesuai pilihan yang ada.")

u = User()
print("Selamat datang di Bus Management Jember!")

while True:
    print("==========[Menu Utama]==========")
    print("1. Masuk\n2. Daftar\n3. Pilih Asal atau Tujuan anda\n4. Keluar")
    menu = input("Memilih : ")
    if menu == '1':
        print("==========Masuk]==========")
        username = input("Username:")
        password = input("Password:")
        u.login(username, password)
    elif menu == '2':
        print("==========[Daftar]==========")
        username = input("Username:")
        password = input("Password:")
        u.register(username, password)
    elif menu == '3':
        print("==========[Asal atau Tujuan]==========")
        if u.username == None:
            print("Silahkan Login terlebih dahulu!")
        else:
            print("Pilih Asal atau Tujuan anda")
            print("1. Banyuwangi\n2. Bondowoso\n3. Situbondo\n4. Probolinggo\n5. Lumajang\n6. Malang\n7. Pasuruan\n8. Sidoarjo \n9. Mojokerto\n10. Blitar")
            jenis = input("Memilih : ")
            print("Pilih tingkatan kelas")
            print("1. Eksekutif\n2. Bisnis\n3. Ekonomi")
            kelas = input("Memilih : ")
            u.jenis_bus(jenis, kelas)
    elif menu == '4':
        print("Terima kasih telah memakai program ini!")
        break
    else:
        print("Masukkan angka sesuai pilihan yang ada.")
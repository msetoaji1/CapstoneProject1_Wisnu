dataAlumni = [
    {
        'Nama': 'Wisnu',
        'Jurusan': 'Ekonomi',
        'Gender': 'L',
        'Nim': 1250,
        'IPK': 3.70
    },
    {
        'Nama': 'Windah',
        'Jurusan': 'Manajemen',
        'Gender': 'L',
        'Nim': 2245,
        'IPK': 3.56
    },
    {
        'Nama': 'Alfa',
        'Jurusan': 'Ekonomi',
        'Gender': 'L',
        'Nim': 1001,
        'IPK': 3.58
    },
    {
        'Nama': 'Aliqah',
        'Jurusan': 'Manajemen',
        'Gender': 'P',
        'Nim': 2001,
        'IPK': 3.90
    },
    {
        'Nama': 'Brenda',
        'Jurusan': 'Ekonomi',
        'Gender': 'P',
        'Nim': 1023,
        'IPK': 3.27
    },
    {
        'Nama': 'Cris',
        'Jurusan': 'Manajemen',
        'Gender': 'L',
        'Nim': 2002,
        'IPK': 3.72
    },
    {
        'Nama': 'Faris',
        'Jurusan': 'Ekonomi',
        'Gender': 'L',
        'Nim': 1034,
        'IPK': 3.70
    },
    {
        'Nama': 'Mikail',
        'Jurusan': 'Manajemen',
        'Gender': 'L',
        'Nim': 2067,
        'IPK': 3.56
    },
    {
        'Nama': 'Rima',
        'Jurusan': 'Ekonomi',
        'Gender': 'P',
        'Nim': 2115,
        'IPK': 3.80
    },
    {
        'Nama': 'Tina',
        'Jurusan': 'Manajemen',
        'Gender': 'P',
        'Nim': 2165,
        'IPK': 3.45
    }
]



# Fungsi untuk menampilkan seluruh data alumni
def daftar_alumni():
    print('''
        = = = = =   DATA ALUMNI = = = = =
         = = = = UNIVERSITAS PAGI SORE = = = \n''')
    print('No\t| Nama\t\t| Jurusan\t| Gender\t| Nim\t| IPK')
    print('=' * 60)
    for i, alumni in enumerate(dataAlumni):
        print(f"{i+1}\t| {alumni['Nama']}\t| {alumni['Jurusan']}\t| {alumni['Gender']}\t\t| {alumni['Nim']}\t| {alumni['IPK']}")

# Fungsi untuk menampilkan data alumni tertentu berdasarkan Nim
def unik_data():
    nim = int(input("Masukkan NIM alumni yang ingin dicari: "))
    found = False
    for alumni in dataAlumni:
        if alumni['Nim'] == nim:
            print(f"\nNama: {alumni['Nama']}")
            print(f"Jurusan: {alumni['Jurusan']}")
            print(f"Gender: {alumni['Gender']}")
            print(f"NIM: {alumni['Nim']}")
            print(f"IPK: {alumni['IPK']}")
            found = True
            break
    if not found:
        print(f"Alumni dengan NIM {nim} tidak ditemukan.")

# Fungsi untuk menampilkan menu data alumni
def MenuDataAlumni():
    while True:
        print('''
              1. Menampilkan Seluruh Data Alumni
              2. Menampilkan Data Tertentu
              3. Kembali Ke Menu Utama\n''')
        submenu = int(input('Silahkan pilih daftar menu di atas [1-3]: '))
        if submenu == 1:
            daftar_alumni()
        elif submenu == 2:
            unik_data()
        elif submenu == 3:
            break  # Kembali ke menu utama
        else:
            print('Input yang Anda masukkan salah. Silahkan masukkan pilihan yang benar [1-3].')

# Fungsi untuk menambahkan data alumni baru
def tambahData():
    nama = input("Masukkan nama alumni: ")
    jurusan = input("Masukkan jurusan: ")
    gender = input("Masukkan gender (L/P): ")
    nim = int(input("Masukkan NIM: "))
    ipk = float(input("Masukkan IPK: "))
    dataAlumni.append({'Nama': nama, 'Jurusan': jurusan, 'Gender': gender, 'Nim': nim, 'IPK': ipk})
    print("Data berhasil ditambahkan!")

# Fungsi untuk mengubah data alumni berdasarkan NIM
def updateData():
    nim = int(input("Masukkan NIM alumni yang ingin diubah: "))
    found = False
    for alumni in dataAlumni:
        if alumni['Nim'] == nim:
            print("Data yang ditemukan:")
            print(alumni)
            nama = input("Masukkan nama baru (biarkan kosong untuk tidak mengubah): ")
            jurusan = input("Masukkan jurusan baru (biarkan kosong untuk tidak mengubah): ")
            gender = input("Masukkan gender baru (biarkan kosong untuk tidak mengubah): ")
            ipk = input("Masukkan IPK baru (biarkan kosong untuk tidak mengubah): ")
            
            if nama:
                alumni['Nama'] = nama
            if jurusan:
                alumni['Jurusan'] = jurusan
            if gender:
                alumni['Gender'] = gender
            if ipk:
                alumni['IPK'] = float(ipk)
            print("Data berhasil diperbarui!")
            found = True
            break
    if not found:
        print(f"Alumni dengan NIM {nim} tidak ditemukan.")

# Fungsi untuk menghapus data alumni berdasarkan NIM
def deleteData():
    nim = int(input("Masukkan NIM alumni yang ingin dihapus: "))
    for i, alumni in enumerate(dataAlumni):
        if alumni['Nim'] == nim:
            del dataAlumni[i]
            print(f"Data alumni dengan NIM {nim} berhasil dihapus.")
            return
    print(f"Alumni dengan NIM {nim} tidak ditemukan.")

# Fungsi menu utama
def menuAwal():
    while True:
        print('''
        = = = = = Selamat datang Alumni Universitas Pagi Sore = = = = =
              
              = = = = = Daftar Pilihan : = = = = =
              
              1. Report Data Alumni
              2. Menambahkan Data Alumni
              3. Mengubah Data Alumni
              4. Menghapus Data Alumni
              5. Exit ''')
        
        pilihanMenu = input('Masukkan Nomer yang dipilih (1-5): ')
        if pilihanMenu == '1':
            MenuDataAlumni()
        elif pilihanMenu == '2':
            tambahData()
        elif pilihanMenu == '3':
            updateData()
        elif pilihanMenu == '4':
            deleteData()
        elif pilihanMenu == '5':
            print('Terima kasih, sampai jumpa lagi :)')
            break
        else:
            print("Pilihan tidak valid, silahkan coba lagi.")

# Menjalankan menu utama
menuAwal()

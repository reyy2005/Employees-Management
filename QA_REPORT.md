# QA Report - Employees Management

## Informasi Pengujian

- Project: Employees Management
- File diuji: `programs.py`
- Fitur diuji: Create Data dan Show Data dalam bentuk tabel
- Status akhir: Passed untuk flow utama create data lalu lihat data

## Ringkasan

Pengujian dilakukan pada fitur input data karyawan dan fitur menampilkan data dalam bentuk tabel menggunakan `tabulate`.

Masalah utama yang ditemukan adalah data karyawan tidak tampil di tabel karena database dibuat ulang saat berpindah menu, dan fungsi `show_data()` mengambil database kosong baru, bukan database aktif yang sudah berisi data input user.

## Temuan Bug

### 1. Data Hilang Saat Pindah Menu

Lokasi lama: fungsi `show_header()`

Kode bermasalah:

```python
db = db_emloyees()
```

Masalah:

Database dibuat ulang di dalam menu. Akibatnya setiap user kembali ke menu, data yang sudah diinput sebelumnya hilang.

Dampak:

User berhasil input data, tetapi saat memilih menu `Lihat Data`, program tetap menganggap data tidak tersedia.

Perbaikan:

Database dibuat satu kali di entry point program:

```python
if __name__ == "__main__" :
    db = db_emloyees()
    show_header(db)
```

Alasan perbaikan:

Database harus dibuat satu kali dan dikirim ke setiap fitur yang membutuhkan data, yaitu `create_data(db)` dan `show_data(db)`.

### 2. Tabel Mengambil Database Kosong

Lokasi lama: fungsi `show_data()`

Kode bermasalah:

```python
data = db_emloyees()
```

Masalah:

Kode tersebut membuat database baru yang masih kosong. Seharusnya fungsi `show_data()` memakai parameter `db` yang dikirim dari menu utama.

Dampak:

`tabulate()` tidak menampilkan data karyawan yang sudah diinput.

Perbaikan:

Data dari dictionary diubah menjadi list baris tabel:

```python
data = []
total_data = len(db['name'])

for index in range(total_data) :
    data.append([
        db['name'][index].capitalize(),
        db['age'][index],
        db['position'][index].capitalize(),
        db['role'][index].capitalize(),
        db['department'][index].upper(),
        db['salary'][index]
    ])
```

Alasan perbaikan:

`tabulate()` lebih sesuai menerima data berbentuk list of lists, contohnya:

```python
[
    ["Budi Santoso", 30, "Engineer", "Backend", "IT", 10000000]
]
```

### 3. Fungsi Create Memanggil Menu dari Dalam Fungsi

Lokasi lama: fungsi `create_data(db)`

Kode lama:

```python
show_header()
break
```

Masalah:

Fungsi `create_data()` memanggil `show_header()` secara langsung. Ini membuat alur program menjadi rekursif dan sulit dikontrol.

Dampak:

Program dapat masuk ke menu baru dari dalam proses create data. Dalam jangka panjang, pola ini berpotensi membuat flow program membingungkan.

Perbaikan:

Kode diganti menjadi:

```python
return
```

Alasan perbaikan:

Setelah proses create data selesai, fungsi cukup berhenti dan mengembalikan kontrol ke menu utama. Menu utama yang bertanggung jawab untuk menampilkan pilihan berikutnya.

### 4. Pesan Data Kosong Muncul Saat User Ingin Membuat Data

Lokasi lama: awal fungsi `create_data(db)`

Kode yang dihapus:

```python
if len(db['name']) == 0 : 
    print('Data tidak tersedia.')
    print("Silahkan untuk input data terlebih dahulu...")
    input("Tekan Enter Untuk Melanjutkan...")
```

Masalah:

Saat user memilih menu `Buat Data`, kondisi data kosong adalah hal yang normal.

Dampak:

User mendapat pesan yang tidak perlu sebelum masuk ke form input data.

Alasan penghapusan:

Pesan `Data tidak tersedia` lebih tepat ditampilkan pada fitur `Lihat Data`, bukan pada fitur `Buat Data`.

## Bagian yang Ditambahkan

### 1. Parameter Database pada Menu

Kode baru:

```python
def show_header(db) :
```

Alasan:

Menu utama perlu menerima database aktif agar data yang sama bisa digunakan oleh semua fitur.

### 2. Loop Menu Utama

Kode baru:

```python
while True :
```

Alasan:

Program perlu kembali ke menu utama setelah user selesai membuat data atau melihat data.

### 3. Pemanggilan `show_data(db)`

Kode baru:

```python
elif input_user_program == 2 :
    show_data(db)
```

Alasan:

Menu `Lihat Data` perlu memanggil fungsi `show_data()` dengan database aktif agar tabel bisa menampilkan data yang benar.

### 4. Entry Point Program

Kode baru:

```python
if __name__ == "__main__" :
    db = db_emloyees()
    show_header(db)
```

Alasan:

Ini adalah pola standar Python agar program hanya berjalan ketika file dieksekusi langsung.

## Code Change Highlights

Bagian ini menampilkan kode sebelum dan sesudah perbaikan, dengan format seperti history perubahan pada Git.

### 1. Menghapus Validasi Data Kosong dari `create_data()`

Sebelum:

```diff
 def create_data(db) :
-
-    """
-        1. Checking database while not have data
-    """
-    
-    if len(db['name']) == 0 : 
-        
-        print('Data tidak tersedia.')
-        print("Silahkan untuk input data terlebih dahulu...")
-        input("Tekan Enter Untuk Melanjutkan...")
     
     os.system("cls" if os.name == "nt" else "clear")
```

Sesudah:

```diff
 def create_data(db) :
     
     os.system("cls" if os.name == "nt" else "clear")
```

Alasan:

Menu `Buat Data` tidak perlu menampilkan pesan data kosong, karena tujuan menu tersebut memang untuk membuat data baru.

### 2. Mengganti Pemanggilan Menu Rekursif dengan `return`

Sebelum:

```diff
 elif input_user_action == "Y" :
     
     input("Tekan Enter Untuk ke Menu Utama...")
     
     os.system('cls' if os.name=="nt" else "clear")
-    show_header()
-    break
```

Sesudah:

```diff
 elif input_user_action == "Y" :
     
     input("Tekan Enter Untuk ke Menu Utama...")
     
     os.system('cls' if os.name=="nt" else "clear")
+    return
```

Alasan:

Fungsi `create_data()` cukup mengembalikan kontrol ke menu utama. Menu utama sudah berjalan dalam loop, sehingga tidak perlu dipanggil ulang dari dalam fungsi create.

### 3. Menambahkan Logic Konversi Data untuk Tabel

Sebelum:

```diff
 def show_data(db) :
     ...
-    data = db_emloyees()
     header = ["Nama Lengkap Karyawan","Umur","Posisi","Role/Jabatan","Departement/Divisi","Gaji"]
     print(tabulate(tabular_data=data,headers=header,tablefmt="fancy_grid"))
```

Sesudah:

```diff
 def show_data(db) :
     ...
+    data = []
+    total_data = len(db['name'])
+    
+    for index in range(total_data) :
+        data.append([
+            db['name'][index].capitalize(),
+            db['age'][index],
+            db['position'][index].capitalize(),
+            db['role'][index].capitalize(),
+            db['department'][index].upper(),
+            db['salary'][index]
+        ])
+        
     header = ["Nama Lengkap Karyawan","Umur","Posisi","Role/Jabatan","Departement/Divisi","Gaji"]
     print(tabulate(tabular_data=data,headers=header,tablefmt="fancy_grid"))
```

Alasan:

`tabulate()` membutuhkan data baris. Karena database program berbentuk dictionary berisi list, maka data perlu diubah menjadi list of lists sebelum ditampilkan.

### 4. Mengubah `show_header()` agar Menerima Database Aktif

Sebelum:

```diff
-def show_header() :
+def show_header(db) :
```

Sebelum, database dibuat ulang di dalam menu:

```diff
 input_user_program = int(input('Input No : '))
 
 if input_user_program == 1 :
-    db = db_emloyees()
     create_data(db)
```

Sesudah, menu memakai database yang dikirim dari entry point:

```diff
 input_user_program = int(input('Input No : '))
 
 if input_user_program == 1 :
     create_data(db)
```

Alasan:

Database tidak boleh dibuat ulang setiap kali user memilih menu. Database aktif harus dipakai bersama oleh semua fitur selama program berjalan.

### 5. Menambahkan Menu Loop dan Akses ke `show_data(db)`

Sebelum:

```diff
 def show_header() :
     
     print('Selamat Datang di Program Management-Karyawan'.center(20))
     ...
     input_user_program = int(input('Input No : '))
     
     if input_user_program == 1 :
         db = db_emloyees()
         create_data(db)
         
     elif input_user_program == 5 :
         print("Program Dihentikan.")
         exit()
```

Sesudah:

```diff
 def show_header(db) :
     
+    while True :
         os.system('cls' if os.name=="nt" else "clear")
         print('Selamat Datang di Program Management-Karyawan'.center(20))
         ...
         input_user_program = int(input('Input No : '))
         
         if input_user_program == 1 :
             create_data(db)
+            
+        elif input_user_program == 2 :
+            show_data(db)
             
         elif input_user_program == 5 :
             print("Program Dihentikan.")
             exit()
```

Alasan:

Menu utama perlu terus berjalan setelah user selesai melakukan aksi. Selain itu, pilihan `2. Lihat Data` harus diarahkan ke `show_data(db)`.

### 6. Menambahkan Entry Point Program

Sebelum:

```diff
-show_header()
```

Sesudah:

```diff
+if __name__ == "__main__" :
+    db = db_emloyees()
+    show_header(db)
```

Alasan:

Database dibuat satu kali saat program dijalankan, lalu dikirim ke menu utama. Dengan cara ini, data tidak hilang ketika user berpindah dari create data ke lihat data.

## Hasil Pengujian

### Syntax Check

Command:

```bash
python -m py_compile programs.py
```

Hasil:

Passed. Tidak ada syntax error.

### Smoke Test Manual

Skenario:

1. Pilih menu `1. Buat Data`
2. Input data karyawan
3. Konfirmasi data dengan `Y`
4. Kembali ke menu utama
5. Pilih menu `2. Lihat Data`

Hasil:

Passed. Data karyawan berhasil tampil dalam bentuk tabel menggunakan `tabulate`.

## Catatan QA Tambahan

Masih ada potensi bug pada bagian koreksi data ketika user memilih `N` pada validasi data.

Contoh masalah:

```python
db['name'].append(input_new_name)
db['age'].append(input_new_age)
db['position'].append(input_new_position)
```

Masalah:

Kode tersebut menambahkan data baru menggunakan `.append()`, bukan mengganti data yang sudah ada. Ini dapat membuat panjang list antar field menjadi tidak sama.

Rekomendasi:

Bagian koreksi data sebaiknya menggunakan assignment berdasarkan index, bukan `.append()`.

Contoh:

```python
db['name'][-1] = input_new_name
db['age'][-1] = input_new_age
db['position'][-1] = input_new_position
```

Dengan begitu, data terakhir yang sedang dikoreksi akan diperbarui, bukan ditambahkan sebagai data baru.

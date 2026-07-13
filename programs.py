from tabulate import tabulate
import os 
os.system("cls" if os.name == "nt" else "clear")

def db_emloyees() :
    
    return {
        'name' : [],
        'age' : [],
        'position' : [],
        'role' : [],
        'department' : [],
        'salary' : []
            
    }
    

def create_data(db) :

    """
        1. Checking database while not have data
    """
    
    if len(db['name']) == 0 : 
        
        print('Data tidak tersedia.')
        print("Silahkan untuk input data terlebih dahulu...")
        input("Tekan Enter Untuk Melanjutkan...")
    
    os.system("cls" if os.name == "nt" else "clear")
    
    """
        2. Feature for inputing employees data
    """
    while True :
        
        try :
            
            print("-"*15,'CREATE DATA'.center(20),"-"*15)
            
            print()
            
            input_name = input("Input Nama Lengkap Karyawan : ")
            input_age = int(input("Input Umur Karyawan : "))
            input_position = input("Input Posisi Karyawan : ")
            input_role = input("Input Role/Jabatan Karyawan : ")
            input_department = input("Input Departement/Divisi Karyawan : ")
            input_salary = int(input("Input Gaji Karyawan : "))
            
            """
                3. Append data to database
            """
            
            db['name'].append(input_name)
            db['age'].append(input_age)
            db['position'].append(input_position)
            db['role'].append(input_role)
            db['department'].append(input_department)
            db['salary'].append(input_salary)
            
            os.system("cls" if os.name == "nt" else "clear")
            
            """
                4. Showing all informations the employee
            """
            
            print(f"{"="*20}INFORMASI DATA KARYAWAN : {input_name.upper()} {"="*20} ".center(20))
            print()
            print(f"Nama Lengkap Karyawan : {input_name.capitalize()}")
            print(f"Umur Karyawan : {input_age}")
            print(f"Posisi Karyawan : {input_position.capitalize()}")
            print(f"Role/Jabatan Karyawan : {input_role.capitalize()}")
            print(f"Departement/Divisi Karyawan : {input_department.upper()}")
            print(f"Gaji Karyawan : {input_salary}")
            
            print()
        
        except ValueError :
            
            print("Format Input Tidak Valid. Masukkan Format Data Dengan Sesuai!")
            input("Tekan Enter Untuk Melanjutkan...")
            
        while True :    
            
            try :
                
                input_user_action = input("Apakah Data Di atas Sudah Valid? (Y/N) : ").capitalize()
                
                if input_user_action == "N" :
                    
                    os.system('cls' if os.name=="nt" else "clear")
                    print("Silahkan Input Kembali Data Dengan Benar")
                    print()
                    
                    print(f"1. Nama Lengkap Karyawan : {input_name.capitalize()}")
                    print(f"2. Umur Karyawan : {input_age}")
                    print(f"3. Posisi Karyawan : {input_position.capitalize()}")
                    print(f"4. Role/Jabatan Karyawan : {input_role.capitalize()}")
                    print(f"5. Departement/Divisi Karyawan : {input_department.upper()}")
                    print(f"6. Gaji Karyawan : {input_salary}")
                
                elif input_user_action == "Y" :
                    
                    input("Tekan Enter Untuk ke Menu Utama...")
            
                    os.system('cls' if os.name=="nt" else "clear")
                    show_header()
                    break
                    
            except ValueError :
                
                print("Format Input Tidak Valid. Masukkan Format Data Dengan Sesuai!")
                input("Tekan Enter Untuk Melanjutkan...")
        
            while True :
                            
                try : 
                    
                    print()
                    input_user_option = int(input("Pilih No yang Akan Di perbaiki : "))
                    
                    if input_user_option == 1 :
                        
                        print()
                        input_new_name = input("Masukkan Nama : ")
                        db['name'].append(input_new_name)
                        
                        os.system("cls" if os.name == "nt" else "clear")    
                        
                        print(f"1. Nama Lengkap Karyawan : {input_new_name.capitalize()}")
                        print(f"2. Umur Karyawan : {input_age}")
                        print(f"3. Posisi Karyawan : {input_position.capitalize()}")
                        print(f"4. Role/Jabatan Karyawan : {input_role.capitalize()}")
                        print(f"5. Departement/Divisi Karyawan : {input_department.capitalize()}")
                        print(f"6. Gaji Karyawan : {input_salary}")
                        
                        print()
                        break
                        
                    elif input_user_option == 2 :
                        
                        print()
                        input_new_age = int(input("Masukkan Umur : "))
                        db['age'].append(input_new_age)
                        
                        os.system("cls" if os.name=="nt" else "clear")
                        
                        print(f"1. Nama Lengkap Karyawan : {input_name.capitalize()}")
                        print(f"2. Umur Karyawan : {input_new_age}")
                        print(f"3. Posisi Karyawan : {input_position.capitalize()}")
                        print(f"4. Role/Jabatan Karyawan : {input_role.capitalize()}")
                        print(f"5. Departement/Divisi Karyawan : {input_department.capitalize()}")
                        print(f"6. Gaji Karyawan : {input_salary}")
                        
                        print()
                        break
                        
                    elif input_user_option == 3 :
                        
                        print()
                        input_new_position = input("Masukkan Posisi : ")
                        db['position'].append(input_new_position)
                        
                        os.system("cls" if os.name=="nt" else "clear")
                        
                        print(f"1. Nama Lengkap Karyawan : {input_name.capitalize()}")
                        print(f"2. Umur Karyawan : {input_age}")
                        print(f"3. Posisi Karyawan : {input_new_position.capitalize()}")
                        print(f"4. Role/Jabatan Karyawan : {input_role.capitalize()}")
                        print(f"5. Departement/Divisi Karyawan : {input_department.capitalize()}")
                        print(f"6. Gaji Karyawan : {input_salary}")
                        
                        print()
                        break
                        
                    elif input_user_option == 4 :
                        
                        print()
                        input_new_role = input("Masukkan Role/Jabatan : ")
                        db['role'].append(input_new_role)
                        
                        os.system('cls' if os.name=="nt" else "clear")
                        
                        print(f"1. Nama Lengkap Karyawan : {input_name.capitalize()}")
                        print(f"2. Umur Karyawan : {input_age}")
                        print(f"3. Posisi Karyawan : {input_position.capitalize()}")
                        print(f"4. Role/Jabatan Karyawan : {input_new_role.capitalize()}")
                        print(f"5. Departement/Divisi Karyawan : {input_department.capitalize()}")
                        print(f"6. Gaji Karyawan : {input_salary}")
                        
                        print()
                        break
                        
                    elif input_user_option == 5 :
                        
                        print()
                        input_new_division = input("Masukkan Divisi/Departement")
                        db['department'].append(input_new_division)
                        
                        print(f"1. Nama Lengkap Karyawan : {input_name.capitalize()}")
                        print(f"2. Umur Karyawan : {input_age}")
                        print(f"3. Posisi Karyawan : {input_position.capitalize()}")
                        print(f"4. Role/Jabatan Karyawan : {input_role.capitalize()}")
                        print(f"5. Departement/Divisi Karyawan : {input_new_division.capitalize()}")
                        print(f"6. Gaji Karyawan : {input_salary}")
                        
                        print()
                        break
                        
                    elif input_user_option == 6 :
                        
                        print()
                        input_new_salary = int(input("Masukkan Gaji : "))
                        db['salary'].append(input_new_salary)
                        
                        print(f"1. Nama Lengkap Karyawan : {input_name.capitalize()}")
                        print(f"2. Umur Karyawan : {input_age}")
                        print(f"3. Posisi Karyawan : {input_position.capitalize()}")
                        print(f"4. Role/Jabatan Karyawan : {input_role.capitalize()}")
                        print(f"5. Departement/Divisi Karyawan : {input_department.capitalize()}")
                        print(f"6. Gaji Karyawan : {input_new_salary}")
                        
                        print()
                        break
                    
                    else :
                        
                        print("Maaf Pilihan Tidak Valid. Silahkan Gunakan No yang Tertera.")
                        input("Tekan Enter Untuk Melanjutkan...")
                
                except ValueError :
                    
                    print("Format Input Tidak Valid. Masukkan Format Data Dengan Sesuai!")
                    input("Tekan Enter Untuk Melanjutkan...")
                                  

def show_header() :
    
    print('Selamat Datang di Program Management-Karyawan'.center(20))
    
    print()
    
    print('Pilih Tindakan : ')
    print('1. Buat Data')
    print('2. Lihat Data')
    print('3. Update Data')
    print('4. Hapus Data')
    print('5. Keluar Program')
    
    print()
    
    input_user_program = int(input('Input No : '))
    
    if input_user_program == 1 :
        db = db_emloyees()
        create_data(db)
        
    elif input_user_program == 5 :
        
        print("Program Dihentikan.")
        exit()
        
show_header()

    
    
        
        
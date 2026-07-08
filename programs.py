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
    

def create_data(db)     :

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
            
            print('CREATE DATA'.center(20))
            
            input_name = input("Input Nama Karyawan : ")
            input_age = int(input("Input Umur Karyawan : "))
            input_position = input("Input Posisi Karyawan : ")
            input_role = input("Input Role/Jabatan Karyawan : ")
            input_department = input("Input Departement/Divisi Karyawan : ")
            input_salary = int(input("Input Gaji Karywan : "))
            
            """
                3. Append data to database
            """
            
            db['name'].append(input_name)
            db['age'].append(input_age)
            db['position'].append(input_position)
            db['role'].append(input_role)
            db['department'].append(input_department)
            db['salary'].append(input_salary)
            
            os.system("cls" if os.name == "clear" else "nt")
            
            """
                4. Showing all informations the employee
            """
            
            print(f"INFORMASI DATA KARYAWAN : {input_name.capitalize()} ".center(20))
            print(f"Nama Lengkap Karyawan : {input_name}")
            print(f"Umur Karyawan : {input_age}")
            print(f"Posisi Karyawan : {input_position}")
            print(f"Role/Jabatan Karyawan : {input_role}")
            print(f"Departement/Divisi Karyawan : {input_position}")
            print(f"Gaji Karyawan : {input_salary}")
            
            print()
            
            while True :    
                
                try :
                    
                    input_user_action = input("Apakah Data Di atas Sudah Valid? (Y/N) : ").capitalize()
                    
                    if input_user_action == "Y" :
                        
                        print("Silahkan Input Kembali Data Dengan Benar")
                        print()
                        
                        print(f"1. Nama Lengkap Karyawan : {input_name}")
                        print(f"2. Umur Karyawan : {input_age}")
                        print(f"3. Posisi Karyawan : {input_position}")
                        print(f"4. Role/Jabatan Karyawan : {input_role}")
                        print(f"5. Departement/Divisi Karyawan : {input_position}")
                        print(f"6. Gaji Karyawan : {input_salary}")
                    
                        while True :
                            
                            input_user_option = int(input("Pilih No yang Akan Di perbaiki : "))
                            
                            if input_user_option == 1 :
                                
                                input_new_name = input("Masukkan Nama : ")
                                db['name'].append(input_new_name)
                                
                                os.system("cls" if os.name == "clear" else "nt")    
                                
                                print(f"1. Nama Lengkap Karyawan : {input_new_name}")
                                print(f"2. Umur Karyawan : {input_age}")
                                print(f"3. Posisi Karyawan : {input_position}")
                                print(f"4. Role/Jabatan Karyawan : {input_role}")
                                print(f"5. Departement/Divisi Karyawan : {input_position}")
                                print(f"6. Gaji Karyawan : {input_salary}")
                                
                                print()
                                input("Tekan Enter Untuk Kembali ke Menu Utama...")
                                
                
                except ValueError :
                    
                    print("Format Input Tidak Valid. Masukkan Format Data Dengan Sesuai!")
                    input("Tekan Enter Untuk Melanjutkan...")
                
        except ValueError :
            
            print("Format Input Tidak Valid. Masukkan Format Data Dengan Sesuai!")
            input("Tekan Enter Untuk Melanjutkan...")
                
    
    

def show_header() :
    
    print('Selamat Datang di Program Management-Karyawan'.center(20))
    
    print()
    
    print('Pilih Tindakan : ')
    print('1. Buat Data  \\t2. Lihat Data ')
    print('3. Update Data  \\t4. Hapus Data ')
    
    
    input_user_program = int(input('Input No : '))
    
    if input_user_program == 1 :
        db = db_emloyees()
        create_data(db)
        
show_header()
        
        
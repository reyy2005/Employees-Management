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
                    return
                    
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
                        db['name'][-1] = input_new_name
                        
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
                        db['age'][-1] = input_new_age
                        
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
                        db['position'][-1] = input_new_position
                        
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
                        db['role'][-1] = input_new_role
                        
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
                        db['department'][-1] = input_new_division
                        
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
                        db['salary'][-1] = input_new_salary
                        
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
                                  

def show_data(db) :

    os.system('cls' if os.name=="nt" else "clear")
    
    if len(db['name']) == 0 :
        
        print('Data tidak tersedia.')
        print("Silahkan untuk input data terlebih dahulu...")
        input("Tekan Enter Untuk Melanjutkan...")
        
    else :
        
        os.system('cls' if os.name=="nt" else "clear")
        
        print(f"{"="*20}INFORMASI KARYAWAN{"="*20}".center(20))
        
        data = []
        
        for index in range(len(db['name'])) :
            data.append([
                db['name'][index].capitalize(),
                db['age'][index],
                db['position'][index].capitalize(),
                db['role'][index].capitalize(),
                db['department'][index].upper(),
                db['salary'][index]
            ])
            
        header = ["Nama Lengkap Karyawan","Umur","Posisi","Role/Jabatan","Departement/Divisi","Gaji"]
        print(tabulate(tabular_data=data,headers=header,tablefmt="fancy_grid"))
        
        print()
        
        input("Tekan Enter Untuk Kembali Ke Menu Utama...")
        
def update_data(db) :
    
    if len(db['name']) == 0 :
        
        print("Tidak Ada Data Yang Tersedia.")
        print("Silahkan Input Data Terlebih Dahulu.")
        input("Tekan Enter Untuk Menlanjutkan...")
        
    else :
        
        os.system("cls" if os.name=="nt" else "clear")
        
        print("="*20,"INFORMASI KARYAWAN".center(20),"="*20)
        
        data = []
        
        for i in range(len(db['name'])) :
            
            data.append([
                db['name'][i].capitalize(),
                db['age'][i],
                db['position'][i].capitalize(),
                db['role'][i].capitalize(),
                db['department'][i].capitalize(),
                db['salary'][i],
                
            ])
        
        header = ["Nama Lengkap Karyawan",'Umur','Posisi','Role/Jabatan','Departement/Divisi','Gaji']
        print(tabulate(data,header,"fancy_grid"))
        
        print()
        
        while True :
            
            try :
                
                input_user_update = input('Masukkan Nama Karyawan Yang Akan Di Update : '.capitalize())
                
                if input_user_update in db['name'] :
                    
                    os.system('cls' if os.name=="nt" else "clear")
                    
                    print(f"Informasi Data Lengkap Karyawan : {input_user_update.capitalize()}")
                    get_index = db['name'].index(input_user_update)
                    print()
                    
                    print(f"Nama Lengkap : {db['name'][get_index]}")
                    print(f"Umur : {db['age'][get_index]}")
                    print(f"Posisi : {db['position'][get_index]}")
                    print(f"Role/Jabatan : {db['role'][get_index]}")
                    print(f"Departement/Divisi : {db['department'][get_index]}")
                    print(f'Gaji : {db['salary'][get_index]}')
                    
                else :
                    
                    print("Nama Karyawan Tidak Ditemukan.")
                    continue
                
            except ValueError :
                
                print("Format Input Tidak Valid. Gunakan Format Input Yang Benar!")
                input("Tekan Enter Untuk Melanjutkan...")
                    
                    
                    
                    
                    

            
def show_header(db) :
    
    while True :
        
        os.system('cls' if os.name=="nt" else "clear")
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
            create_data(db)
            
        elif input_user_program == 2 :
            
            show_data(db)
            
        elif input_user_program == 3 :
            update_data(db)
            
        elif input_user_program == 5 :
            
            print("Program Dihentikan.")
            exit()
        
if __name__ == "__main__" :
    db = db_emloyees()
    show_header(db)

    
    
        
        

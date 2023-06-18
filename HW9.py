# Создать телефонный справочник с 
# возможностью импорта и экспорта данных в 
# формате .txt. Фамилия, имя, отчество, номер 
# телефона - данные, которые должны находиться 
# в файле. 
# 1. Программа должна выводить данные 
# 2. Программа должна сохранять данные в 
# текстовом файле 
# 3. Пользователь может ввести одну из 
# характеристик для поиска определенной 
# записи(Например имя или фамилию 
# человека) 
# 4. Использование функций. Ваша программа 
# не должна быть линейной 
 
'''
file_path = 'tel_sprav.txt' 
def vvod(): 
    vizov = int (input('Введите команду: \n1 - Вывод всех данных \n2 - Добавление контакта \n3 - Поиск контакта \n4 - Удаление контакта\n:')) 
    return vizov 
 
def vivod_dannih(file_path): 
    with open(file_path, 'r', encoding='UTF-8') as f: 
        for line in f: 
            mass = line.strip().split(',') 
            for i in range(len(mass)): 
                print(mass[i], end=" ") 
            print("") 
        f.read() 
    return True 
 
def add_contact(file_path): 
    with open(file_path, 'a', encoding='UTF-8') as f: 
        surname = input('Введите данные контакта: Фамилия: ') 
        name = input('Имя: ') 
        patronymic = input('Отчество: ')  
        phone = input('Номер телефона: ') 
        print(f'Контакт успешно добавлен --> {surname} {name} {patronymic} {phone}') 
        f.write ('\n' + f'{surname},{name},{patronymic},{phone}') 
    return True 
     
            
def search_cont(file_path): 
    with open(file_path, 'r', encoding='UTF-8') as f: 
        poisk = input('Введите данные контакта: ') 
        for line in f: 
            if poisk in line: 
                mass = line.strip().split(',') 
                for i in range(len(mass)): 
                    print(mass[i], end=" ") 
                print("") 
        f.read()     
    return True 
 
def del_data (file_path): 
    with open(file_path, 'r', encoding='UTF-8') as fi: 
        lines = fi.readlines() 
        fi.close() 
    with open(file_path, 'w', encoding='UTF-8') as f: 
        poisk = input('Введите данные контакта для удаления: ') 
        for line in lines: 
            if poisk not in line: 
                f.write(line) 
        f.close() 
    print("Контакт успешно удален")     
    return True 
 
 
input_ = vvod() 
 
if input_ ==1: 
    vivod_dannih(file_path) 
elif input_ ==2: 
    add_contact(file_path) 
elif input_ ==3: 
    search_cont(file_path) 
elif input_ ==4: 
    del_data(file_path) 
else: 
    print("Выбран недопустимый параметр! Попробуйте снова! ")
'''
'''
    def change_contact():
    contact_data = []
    with open(file_path, 'r') as phone_book:
        for line in phone_book:
            contact_data.append(line.strip())
    
    search_info = input('Какой контакт: ')
    
    for contact_idx in range(len(contact_data)):
        if contact_data[contact_idx] in contact:
            new_info = input('Введите изменения: ')
            contact_data[contact_idx] = new_info
            break
    
    with open(file_path, 'w') as phone_book:
        for contact in contact_data[:-1]:
            phone_book.write(contact + '\n')
        phone_book.write(contact_data[-1])
'''
def write_contacts(filename):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write('\n' + str.lower(input(f'Введите через пробел: ФИО и номер телефона -> ')))
    return file

def read_contacts(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line)

def find_contacts(filename):
    find = str.lower(input('Введите данные для поиска: '))
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if find in line:
               print(line)

def edit_contacts(filename):
    words = str.lower(input('Введите, что будем менять -> '))
    with open(filename, 'r', encoding='utf-8') as file:
        old_data = file.read()
        new_data = old_data.replace(words, str.lower(input('Введите на что заменить -> ')))
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(new_data)

filename = r'tel_sprav.txt' 
flag = True
while flag:
    ask = int(input('1 - для ввода, 2 - для вывода, 3 - для поиска, 4 - для редактирования или удаления \n'))
    if ask == 1:
        write_contacts(filename)
        answ = str.lower(input('Продолжаем? да/нет -> '))
        if answ == 'нет': flag = False
        else: continue
    elif ask == 2:
        read_contacts(filename)
        answ = str.lower(input('Продолжаем? да/нет -> '))
        if answ == 'нет': flag = False
        else: continue
    elif ask == 3:
        find_contacts(filename)
        answ = str.lower(input('Продолжаем? да/нет -> '))
        if answ == 'нет': flag = False
        else: continue
    elif ask == 4:
        edit_contacts(filename)
        answ = str.lower(input('Продолжаем? да/нет -> '))
        if answ == 'нет': flag = False
        else: continue
    else:
        print('Нет такой функции!')
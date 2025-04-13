"""

-- Функции --

1. Регистрация -- Пользователь может зарегистрироваться, введя логин и пароль. Данные сохраняются в json-файл.

2. Авторизация(войти как обычный пользователь) -- Пользователь может войти в систему, используя логин и пароль. При успешной авторизации открывается доступ
                                                  к остальным функциям
                                                  
3. Авторизация(войти как администратор) -- функция доступна только после прохождения обычной авторизации. Если условие соблюдено, потребуется ввести пароль.

"""
# Импорт нужных дополнении.
import os
import json
from utils.helpers import check_password


def sign_up():
    """ Джабо """
    #Объявление пути к файлу и пустого словаря
    file_path = 'users.json'
    data = {}
    #Проверка существования файла по пути 
    if os.path.exists(file_path):
        #Открытие файла на чтение и запись его содержания в data
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    while True:
        login = input("Введите логин(минимум 8 символов):")
        if len(login) < 8:
            print('Слишком короткий логин')
            continue
        #Проверка введенного логина в массиве ключей словаря.
        if login not in data.keys():
            break
        print('Логин занят.')

    while True:
        password = input(
            'Введите пароль(минимум: 8 символов, 1 маленькая латинская буква, 1 большая латинская буква,1 спец. символ):')
        if check_password(password):
            break
        print('Ненадежный пароль')
    #Добавление данных в словарь 
    data[login] = password
  
    #Открытие файла на запись и запись в него значения словаря.
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
    return "Регистрация успешна!"

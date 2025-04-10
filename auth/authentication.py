"""

-- Функции --

1. Регистрация -- Пользователь может зарегистрироваться, введя логин и пароль. Данные сохраняются в json-файл.

2. Авторизация(войти как обычный пользователь) -- Пользователь может войти в систему, используя логин и пароль. При успешной авторизации открывается доступ
                                                  к остальным функциям
                                                  
3. Авторизация(войти как администратор) -- функция доступна только после прохождения обычной авторизации. Если условие соблюдено, потребуется ввести пароль.

"""

import os
import json
from utils.helpers import сheck_password


def sign_up():
  """ Джабо """
    file_path = 'users.json'
    data = {}

    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    while True:
        login = input("Введите логин:")
        if login not in data.keys():
            break
        print('Логин занят.')

    while True:
        password = input(
            'Введите пароль(минимум: 8 символов, 1 маленькая латинская буква, 1 большая латинская буква,1 спец. символ):')
        if сheck_password(password):
            break
        print('Ненадежный пароль')
    data[login] = password

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
    return "Регистрация успешна!"

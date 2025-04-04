import json
from user import User
import os


def load_data(filename='data.json'):
    """Функция загрузки списка пользователей из JSON-файла"""
    # Если файла с пользователями не существует, создаем его и добавляем в него пустой список
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            json.dump({}, f)

    # Если файл существует считывает его данные и возвращает их ввиде списка
    with open(filename, 'r') as f:
        try:
            return json.load(f)
        # Если файл пуст или испорчен, вовзращает пустой словарь
        except json.JSONDecodeError:
            return {}


def save_data(data, filename='data.json'):
    """ data: dict
        Функция сохранения списка пользователей в JSON-файл"""
    with open(filename, 'w') as f:
        # indent 4 делает отступы в файле для внешней аккуратной преезнтации
        json.dump(data, f, indent=4)


def register_user():
    """Функция регистрирует нового пользователя, если имя пользователя свободно"""
    # Загружаем список пользователей
    data = load_data()
    print("Регистрация нового пользователя\n\n")
    # Регистрация идет до тех пор пока не будет введен свободный логин
    while True:
        t_login = input("Введите логин: ")
        # Если логин свободен, вводится пароль и запись добавляется в список пользователей а затем JSON-файл сохраняется
        if t_login not in data.keys():
            t_password = input("Введите пароль: ")
            new_user = User(t_login, t_password)
            data[new_user.login] = new_user.password
            print("\nПользователь успешно зарегистрирован!\n")
            save_data(data)
            break
        # В противном случае ввод начинается заново
        else:
            print("\nИмя пользователя занято, введите другой\n")


if __name__ == "__main__":
    register_user()

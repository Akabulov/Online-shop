from auth import authentication as au


def login_page():
    """ Костя """
    print(
        "1. Регистрация\n"
        + "2. Авторизация\n"
        + "3. Войти как администратор\n"
        + "0. Закрыть приложение\n"
    )
    user_input = int(input())
    if user_input == 1:
        au.sign_up()
    elif user_input == 2:
        # Авторизация
        pass
    elif user_input == 3:
        # Авторизация от имени админа
        pass
    elif user_input == 0:
        quit()


def user_ui():
    """ Костя """
    print(
        "-" * 28
        + "\n"
        + "1. Посмотреть каталог товаров\n"
        + "2. Добавить товар в корзину\n"
        + "3. Просмотреть корзину\n"
        + "4. Найти товары (по названию)\n"
        + "5. Оформить заказ\n"
        + "6. Просмотреть историю заказов\n"
        + "0. Выйти из аккаунта\n"
        + ">>> ")
    user_input = int(input())
    if user_input == 1:
        pass
    elif user_input == 2:
        pass
    elif user_input == 3:
        pass
    elif user_input == 4:
        pass
    elif user_input == 5:
        pass
    elif user_input == 6:
        pass
    elif user_input == 0:
        login_page()


if __name__ == "__main__":
    login_page()

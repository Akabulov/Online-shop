from main import login_page
"""

class AdminPanel:
    -- Свойства --
    1.0. admin_menu: List[str] ~ на рассмотрение
    1.1. password

    -- Методы --
    1.2. показать админское меню ~ на рассмотрение
    1.3. вывод статистики продаж
    1.4. вывод информации обо всех зарегистрированных пользователях
    

"""


def admin_required(func):
    """Костя

        над функциями которые принадлежат роли админа
        пишите @admin_required

    """
    def wrapper(user, *args, **kwargs):
        if user.role != "admin":
            print("Доступ запрещён!")
            return
        return func(*args, **kwargs)
    return wrapper


def admin_ui():
    """ Костя """
    print(
        "1. Добавить товар\n"
        + "2. Удалить товар\n"
        + "3. Вывод списка пользователей\n"
        + "0. Выйти из аккаунта\n"
    )
    user_input = int(input())
    if user_input == 1:
        # Добавление товара
        pass
    elif user_input == 2:
        # Удаление товара
        pass
    elif user_input == 3:
        # Вывод списка пользователей
        pass
    elif user_input == 0:
        login_page()

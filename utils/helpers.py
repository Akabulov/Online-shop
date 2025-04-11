"""  файл для хранения второстепенных функций  """


def check_password(password):
    """ Джабо """
    symbols_counter = 0
    upper_letters_counter = 0
    lower_letters_counter = 0
    upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_letters = 'abcdefghijklmnopqrstuvwxyz'
    symbols = '!@#$%^&*()-+'
    if len(password) < 8:
        return False
    for i in password:
        if i in upper_letters:
            upper_letters_counter += 1
        elif i in lower_letters:
            lower_letters_counter += 1
        elif i in symbols:
            symbols_counter += 1
    if symbols_counter > 0 and lower_letters_counter > 0 and upper_letters_counter > 0:
        return True
    return False
    

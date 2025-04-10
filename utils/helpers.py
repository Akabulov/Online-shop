"""  файл для хранения второстепенных функций  """


def сheck_password(password):
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


"""
def check_password_strength(password):
    ''' Проверяет пароль на надежность. '''
    
    smb_counter, symbols = 0, "!@#$%^&*()-+" 
    
    upper_let, lower_let = "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"  
    up_counter, low_counter = 0, 0
    
    for gs in password:
        if gs in up_letters: up_counter += 1
        if gs in low_letters: low_counter += 1
        if gs in symbols: smb_counter += 1   
        
    return not (smb_counter == 0 or low_counter == 0 or up_counter == 0 or len(password) < 8)
"""

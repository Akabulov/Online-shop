"""

class User:
  -- Свойства --
  1.0. user_menu: List[str] ~ на рассмотрение
  1.1. username
  1.2. password
  1.3. is_admin

  -- Методы --
  1.4. показать пользовательское меню ~ на рассмотрение
  1.5. выйти из системы
  
"""


class User:
    def __init__(self, username, password, is_admin=False):
        self.username = username
        self.password = password
        self.is_admin = is_admin
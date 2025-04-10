"""
class Order:
  -- Свойства --
  1.1. order_items: List[Product]

  -- Методы --
  1.2. оформить заказ
  1.3. записать заказ в файл
  1.3. показать историю заказов
  1.4. очистить список заказа order_items (опционально)
"""

class Order:
    # -- Свойства -- 
    # ...

    # -- Методы --    
    def save_order(self, user: User, filepath: str = "../cart/orders.json"):
        """ Добавляет заказ в историю заказов пользователя """
        
        if user.username is None:
            return f"Сначала войдите в систему"
            
        try:
            with open(filepath, "r") as file:
                data = json.load(file)
         except FileNotFoundError as e:
            data = list()

        for item in self.order_items:
            data.append({"id": item.id, "title": item.title, "price": item.price})
             
        try:    
            with open(filepath, "w") as file:
                json.dump(data, file, indent=4)
            return f"Заказ успешно добавлен в историю!"
        except Exception as e:
            raise RuntimeError(f"Ошибка при сохранении файла: {e}")

    def print_orders_history(self, user: User, filepath: str = "../cart/orders.json"):
        """ Показывает историю заказов пользователя """

        if user.username is None:
            return f"Сначала войдите в систему"
            
        try:
            with open(filepath, "r") as file:
                content = file.read()
                orders = json.load(file) if content else list()
        except FileNotFoundError as e:
            with open(filepath, "w") as file:
                file.write("[]")
            return "Пусто"

        if not orders:
            return "Пусто"

        for ind, order in enumerate(orders, start=1):
            print(f"Заказ {i} -- [", end="")
            for key, val in order.items():
                print(f"{key}: {val}", end=", ")
            print("\b\b]")
            
        return "История заказов успешно выведена!"
        
  

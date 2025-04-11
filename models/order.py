"""
    ~ не хватает функции 'оформить заказ'
"""
import json
from typing import List
try:
    from product import Product
except ImportError:
    class Product: ...


class Order:
    """ Класс для одного Заказа товаров """
    
    def __init__(self):
        self.__order_items: List[Product] = list()

    def save_order(self, user: User, filepath: str = "../cart/orders.json") -> str:
        """ Добавляет заказ в историю заказов пользователя. """
        
        if user.username is None:
            return "Сначала войдите в систему"
            
        try:
            with open(filepath, "r") as file:
                lst = json.load(file)
         except FileNotFoundError as e:
            lst = list()

        for item in self.__order_items:
            lst.append({"id": item.id, "название": item.title, "цена": item.price})
             
        try:    
            with open(filepath, "w") as file:
                json.dump(lst, file, indent=4)
            self._clear()
            return "Заказ успешно добавлен в историю!"
        except Exception as e:
            self._clear()
            raise RuntimeError(f"Ошибка при сохранении файла: {e}")

    def print_orders_history(self, user: User, filepath: str = "../cart/orders.json") -> str:
        """ Показывает историю заказов пользователя. """

        if user.username is None:
            return "Сначала войдите в систему"
            
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
            print(f"Заказ {ind} -- [", end="")
            for key, val in order.items():
                print(f"{key}: {val}", end=", ")
            print("\b\b]")
            
        return "История заказов успешно выведена!"

    def _clear(self) -> None:
        """ Очищает список элементов заказа после его сохранения. """
        self.__order_items.clear()
        
  

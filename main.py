from datetime import *


class BikeRental:
    def __init__(self, stock=0):
        """Создание экземпляра пункта проката"""
        self.stock = stock

    def displayStock(self):
        """Показывает, сколько велосипедов доступно"""
        print(f'У нас {self.stock} велосипед(ов) доступно для аренды')
        return self.stock

    def rentBikeOnHour(self, n):
        """Сдает в аренду велиписед на час"""

        # отклонить отрицательный ввод
        if n <= 0:
            print('')

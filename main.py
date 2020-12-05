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
            print('Количество должно быть больше 0!')
            return None
        elif n > self.stock:
            print(f'У нас только {self.stock} велопид(ов) доступно для аренды')
            return None
        else:
            now = datetime.now()
            print(f'''Вы арендовали {n} велосипед(ов) на {now.hour} час(ов).
            С вас будут списывать по $5 за каждый час аренды.
            Наслаждайтесь!''')
            self.stock -= n
            return now

    def rentBikeOnDay(self, n):
        """Сдает в аренду велиписед на день"""

        # отклонить отрицательный ввод
        if n <= 0:
            print('Количество должно быть больше 0!')
            return None
        elif n > self.stock:
            print(f'У нас только {self.stock} велопид(ов) доступно для аренды')
            return None
        else:
            now = datetime.now()
            print(f'''Вы арендовали {n} велосипед(ов) на {now.day} дня(ей).
            С вас будут списывать по $20 за каждый день аренды.
            Наслаждайтесь!''')
            self.stock -= n
            return now

    def rentBikeOnWeek(self, n):
        """Сдает в аренду велиписед на неделю"""

        # отклонить отрицательный ввод
        if n <= 0:
            print('Количество должно быть больше 0!')
            return None
        elif n > self.stock:
            print(f'У нас только {self.stock} велопид(ов) доступно для аренды')
            return None
        else:
            now = datetime.now()
            print(f'''Вы арендовали {n} велосипед(ов) на {now.hour * 168} недель.
            С вас будут списывать по $60 за каждую неделю аренды.
            Наслаждайтесь!''')
            self.stock -= n
            return now

    def returnBike(self, request):
        """
        1. Принимает велосипед обратно
        2. Обновляет остатки
        3. Выставляет счет
        :param показывает, сколько велоиспедов вернули, срок аренды
        :return bill
        """

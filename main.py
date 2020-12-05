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
            print(f'''Вы арендовали {n} велосипед(ов) на {now.hour} дня(ей).
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
            print(f'''Вы арендовали {n} велосипед(ов) на {now.hour} недель.
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
        rentalTime, rentalBasis, numOfBikes = request
        bill = 0

        if rentalTime and rentalBasis and numOfBikes:
            self.stock += numOfBikes
            now = datetime.now()
            rentalPeriod = now - rentalTime

            if rentalBasis == 1:
                # часовая аренда
                bill = round(rentalPeriod.seconds / 3600) * 5 * numOfBikes
            elif rentalBasis == 2:
                # дневная аренда
                bill = round(rentalPeriod.days) * 20 * numOfBikes
            elif rentalBasis == 3:
                # недельная аренда
                bill = round(rentalPeriod.days / 7) * 60 * numOfBikes

            if 3 <= numOfBikes <= 5:
                print('Вы получаете семейную скидку - 30%')
                bill *= 0.7

            print('Спасибо, что пользуетесь нашим сервисом!')
            print(f'Стоимость аренды ${bill}.')
            return bill
        else:
            print('Вы не арендовали велосипеды!')
            return None


class Customer:
    """Класс для покупателя/арендатора"""

    def __init__(self):
        self.bikes = 0
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0

    def requestBike(self, n_b):
        """Получает количество велосипедов для аренды"""
        try:
            n_b = int(n_b)
        except ValueError:
            print('Неправильное число!')
            return -1

        if n_b < 1:
            print('Неправильный ввод! Количество велосипедов должно быть 1 и более.')
            return -1
        else:
            self.bikes = n_b

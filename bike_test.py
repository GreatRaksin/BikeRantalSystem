import unittest
from datetime import datetime, timedelta
from bikeRental import BikeRental, Customer


class BikeRentalTest(unittest.TestCase):

    def test_display_correct_stocks(self):
        shop1 = BikeRental(30)
        shop2 = BikeRental(15)
        self.assertEqual(shop1.displayStock(), 30, 'should be 30')
        self.assertEqual(shop2.displayStock(), 15, 'should be 15')

    def test_negative_number_of_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeOnHour(-3), None, 'should be None')
        self.assertEqual(shop.rentBikeOnHour(0), None, 'should be None')

    def test_incorrect_positive_number(self):
        pass

    def test_hourly_rent(self):
        shop = BikeRental(10)
        hour = datetime.now().hour
        self.assertEqual(shop.rentBikeOnHour(2).hour, hour, 'no assertion')


if __name__ == '__main__':
    unittest.main()

from unittest import TestCase, main
from project.car import Car

class TestCar(TestCase):
    def setUp(self):
        self.car = Car("Make", "Model", 5, 20)

    def test_car_init(self):
        self.assertEqual("Make", self.car.make)
        self.assertEqual("Model", self.car.model)
        self.assertEqual(5, self.car.fuel_consumption)
        self.assertEqual(20, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_car_make_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""
            self.car.make = None
        self.assertEqual('Make cannot be null or empty!', str(ex.exception))

    def test_car_make(self):
        self.assertEqual("Make", self.car.make)
        self.car.make = "New make"
        self.assertEqual("New make", self.car.make)

    def test_car_model_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""
            self.car.model = None
        self.assertEqual('Model cannot be null or empty!', str(ex.exception))

    def test_car_model(self):
        self.assertEqual("Model", self.car.model)
        self.car.model = "New model"
        self.assertEqual("New model", self.car.model)

    def test_car_fuel_consumption_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -1
            self.car.fuel_consumption = 0
        self.assertEqual('Fuel consumption cannot be zero or negative!', str(ex.exception))

    def test_car_fuel_consumption(self):
        self.assertEqual(5, self.car.fuel_consumption)
        self.car.fuel_consumption = 2.5
        self.assertEqual(2.5, self.car.fuel_consumption)

    def test_car_fuel_capacity_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -1
            self.car.fuel_capacity = 0
        self.assertEqual('Fuel capacity cannot be zero or negative!', str(ex.exception))

    def test_car_fuel_capacity(self):
        self.assertEqual(20, self.car.fuel_capacity)
        self.car.fuel_capacity = 0.75
        self.assertEqual(0.75, self.car.fuel_capacity)

    def test_car_fuel_amount_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1
        self.assertEqual('Fuel amount cannot be negative!', str(ex.exception))

    def test_car_fuel_amount(self):
        self.assertEqual(0, self.car.fuel_amount)
        self.car.fuel_amount = 1
        self.assertEqual(1, self.car.fuel_amount)

    def test_car_refuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
            self.car.refuel(-1)
        self.assertEqual('Fuel amount cannot be zero or negative!', str(ex.exception))

    def test_car_refuel(self):
        self.assertEqual(0, self.car.fuel_amount)
        self.car.refuel(10)
        self.assertEqual(10, self.car.fuel_amount)
        self.car.refuel(10)
        self.assertEqual(20, self.car.fuel_amount)
        self.car.refuel(5)
        self.assertEqual(20, self.car.fuel_amount)

    def test_car_drive_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(100)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_car_drive(self):
        self.assertEqual(0, self.car.fuel_amount)
        self.car.refuel(10)
        self.assertEqual(10, self.car.fuel_amount)
        self.car.drive(100)
        self.assertEqual(5.0, self.car.fuel_amount)

if __name__ == "__main__":
    main()
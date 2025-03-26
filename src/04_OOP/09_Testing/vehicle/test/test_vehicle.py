from unittest import TestCase
from project.vehicle import Vehicle

class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(10.0, 132.0)

    def test_vehicle_init(self):
        self.assertEqual(10.0, self.vehicle.fuel)
        self.assertEqual(10.0, self.vehicle.capacity)
        self.assertEqual(132.0, self.vehicle.horse_power)
        self.assertEqual(self.vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_vehicle_drive_raises(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_vehicle_drive(self):
        self.assertEqual(10.0, self.vehicle.fuel)
        self.vehicle.drive(5)
        self.assertEqual(3.75, self.vehicle.fuel)

    def test_vehicle_refuel_raises(self):
        self.assertEqual(10.0, self.vehicle.fuel)
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(100)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_vehicle_refuel(self):
        self.assertEqual(10.0, self.vehicle.fuel)
        self.vehicle.drive(5)
        self.assertEqual(3.75, self.vehicle.fuel)
        self.vehicle.refuel(5)
        self.assertEqual(8.75, self.vehicle.fuel)

    def test_vehicle_str(self):
        self.assertEqual("The vehicle has 132.0 horse power with 10.0 fuel left and 1.25 fuel consumption", self.vehicle.__str__())
        self.vehicle.drive(5)
        self.assertEqual("The vehicle has 132.0 horse power with 3.75 fuel left and 1.25 fuel consumption", self.vehicle.__str__())


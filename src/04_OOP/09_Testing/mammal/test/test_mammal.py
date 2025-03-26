from unittest import TestCase
from project.mammal import Mammal

class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal('name', 'mammal_type', 'sound')

    def test_mammal_init(self):
        self.assertEqual('name', self.mammal.name)
        self.assertEqual('mammal_type', self.mammal.type)
        self.assertEqual('sound', self.mammal.sound)
        self.assertEqual('animals', self.mammal._Mammal__kingdom)

    def test_mammal_make_sound(self):
        result = self.mammal.make_sound()
        self.assertEqual("name makes sound", result)

    def test_mammal_get_kingdom(self):
        result = self.mammal.get_kingdom()
        self.assertEqual("animals", result)

    def test_mammal_info(self):
        result = self.mammal.info()
        self.assertEqual("name is of type mammal_type", result)


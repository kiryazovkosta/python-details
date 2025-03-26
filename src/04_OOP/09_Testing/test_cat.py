class Cat:
    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')
        self.sleepy = False

from unittest import TestCase, main

class TestCat(TestCase):
    def setUp(self):
        self.cat = Cat("Lady")

    def test_cat_init(self):
        self.assertEqual("Lady", self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_cat_eat_is_fed_raises(self):
        self.cat.fed = True
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertEqual('Already fed.', str(ex.exception))

    def test_cat_eat_not_fed(self):
        self.cat.size = 2
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(2, self.cat.size)
        self.cat.eat()
        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(3, self.cat.size)

    def test_cat_sleep_not_fed_raises(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_cat_sleep_is_fed(self):
        self.cat.fed = True
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)

if __name__ == "__main__":
    main()


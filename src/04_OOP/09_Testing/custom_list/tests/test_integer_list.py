from unittest import TestCase, main
from project.integer_list import IntegerList

class TestIntegerList(TestCase):
    def setUp(self):
        self.il = IntegerList(1,2,3)

    def test_init_int_values(self):
        self.assertListEqual([1, 2, 3], self.il._IntegerList__data)

    def test_init_non_integers_are_skipped(self):
        new_lis = IntegerList(1, 's', [1, 2, 3], 2.5, 5)
        self.assertListEqual([1, 5], new_lis._IntegerList__data)

    def test_get_data_returns_private_data(self):
        result = self.il.get_data()
        self.assertListEqual([1, 2, 3], result)
        self.assertIs(self.il._IntegerList__data, result)

    def test_add_non_integer_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.il.add(2.5)
            self.il.add("test")
            self.il.add([1, 2, 3])
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_add_integer_append(self):
        self.assertListEqual([1, 2, 3], self.il._IntegerList__data)
        self.il.add(4)
        self.assertListEqual([1, 2, 3, 4], self.il._IntegerList__data)

    def test_remove_index_invalid_index_raises(self):
        length_index = len(self.il._IntegerList__data)
        with self.assertRaises(IndexError) as ex:
            self.il.remove_index(length_index)
            self.il.remove_index(length_index + 1)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_remove_valid_index(self):
        self.assertListEqual([1, 2, 3], self.il._IntegerList__data)
        result = self.il.remove_index(1)
        self.assertEqual(2, result)
        self.assertListEqual([1, 3], self.il._IntegerList__data)
        self.assertNotIn(2, self.il._IntegerList__data)

    def test_get_invalid_index_raises(self):
        length_index = len(self.il._IntegerList__data)
        with self.assertRaises(IndexError) as ex:
            self.il.get(length_index)
            self.il.get(length_index + 1)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_valid_index(self):
        self.assertListEqual([1, 2, 3], self.il._IntegerList__data)
        result = self.il.get(1)
        self.assertEqual(2, result)
        self.assertListEqual([1, 2, 3], self.il._IntegerList__data)
        result = self.il.get(0)
        self.assertEqual(1, result)
        self.assertListEqual([1, 2, 3], self.il._IntegerList__data)

    def test_insert_invalid_index_raises(self):
        length_index = len(self.il._IntegerList__data)
        with self.assertRaises(IndexError) as ex:
            self.il.insert(length_index, 4)
            self.il.insert(length_index + 1, 4)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_valid_index_non_integer_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.il.insert(1, [1, 2])
            self.il.insert(0, "test")
            self.il.insert(0, 2.5)
            self.il.insert(0, {"x": 1})
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_insert_valid_index_integer(self):
        self.assertListEqual([1, 2, 3], self.il._IntegerList__data)
        self.il.insert(0, 0)
        self.assertListEqual([0, 1, 2, 3], self.il._IntegerList__data)
        self.il.insert(3, 4)
        self.assertListEqual([0, 1, 2, 4, 3], self.il._IntegerList__data)

    def test_get_biggest(self):
        result = self.il.get_biggest()
        self.assertEqual(3, result)

    def test_get_index(self):
        result = self.il.get_index(1)
        self.assertEqual(0, result)

if __name__ == "__main__":
    main()




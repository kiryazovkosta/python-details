from project.volcano import Volcano

from unittest import TestCase

class TestVolcano(TestCase):

    def setUp(self):
        Volcano._unique_names = set()  # Reset between tests to isolate uniqueness

    def test_valid_init_and_properties(self):
        v = Volcano(" Fuji ", 3776, 2010)
        self.assertEqual(v.name, "FUJI")
        self.assertEqual(v._name, "FUJI")
        self.assertEqual(v.height_m, 3776)
        self.assertEqual(v._height_m, 3776)
        self.assertEqual(v.last_eruption, 2010)
        self.assertTrue(v.is_active)

    def test_name_too_short(self):
        with self.assertRaises(ValueError) as e:
            Volcano("F", 1000)
        self.assertIn("at least two characters", str(e.exception))

    def test_duplicate_name(self):
        Volcano("Etna", 3329)
        with self.assertRaises(ValueError) as e:
            Volcano("Etna", 3000)
        self.assertIn("unique", str(e.exception))

    def test_name_is_trimmed_and_uppercase(self):
        v = Volcano("   vesuvius  ", 1281)
        self.assertEqual(v.name, "VESUVIUS")

    def test_height_zero_or_negative(self):
        with self.assertRaises(ValueError):
            Volcano("Kilauea", 0)
        with self.assertRaises(ValueError):
            Volcano("Kilauea", -5)

    def test_is_active_logic_variety(self):
        v1 = Volcano("Mauna", 3000, 2021)
        v2 = Volcano("Doom", 3200, 1990)
        v3 = Volcano("Calm", 1000, None)
        self.assertTrue(v1.is_active)
        self.assertFalse(v2.is_active)
        self.assertFalse(v3.is_active)

    def test_last_eruption_property_none(self):
        v = Volcano("Silent", 1234)
        self.assertIsNone(v.last_eruption)
        self.assertFalse(v.is_active)

    def test_name_setter_with_stripping_and_reuse_prevention(self):
        v = Volcano("Xeno", 500)
        with self.assertRaises(ValueError):
            Volcano("  xEnO ", 600)

    def test_height_m_setter_and_getter(self):
        v = Volcano("NewVolcano", 1500)
        self.assertEqual(v.height_m, 1500)
        v.height_m = 1600
        self.assertEqual(v.height_m, 1600)

    def test_unique_volcano_count(self):
        self.assertEqual(Volcano.unique_volcano_count(), 0)
        Volcano("Alpha", 1000)
        Volcano("Beta", 2000)
        self.assertEqual(Volcano.unique_volcano_count(), 2)






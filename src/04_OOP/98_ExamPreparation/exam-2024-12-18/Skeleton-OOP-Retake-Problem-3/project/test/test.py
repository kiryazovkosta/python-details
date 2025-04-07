from project.gallery import Gallery

from unittest import TestCase

class TestGallery(TestCase):

    def setUp(self):
        self.gallery = Gallery("Gallery", "City", 100.0)

    def test_gallery_init(self):
        self.assertEqual("Gallery", self.gallery.gallery_name)
        self.assertEqual("City", self.gallery.city)
        self.assertEqual(100.0, self.gallery.area_sq_m)
        self.assertTrue(self.gallery.open_to_public)
        self.assertEqual({}, self.gallery.exhibitions)

    def test_gallery_gallery_name_raises(self):
        with self.assertRaises(ValueError) as e:
            self.gallery.gallery_name = ""
            self.gallery.gallery_name = None
            self.gallery.gallery_name = "12_"
            self.gallery.gallery_name = "@a"
            self.gallery.gallery_name = " alo"
        self.assertEqual("Gallery name can contain letters and digits only!", str(e.exception))

    def test_gallery_city_raises(self):
        with self.assertRaises(ValueError) as e:
            self.gallery.city = ""
            self.gallery.city = None
            self.gallery.city = "1City"
            self.gallery.city = "@City"
        self.assertEqual("City name must start with a letter!", str(e.exception))

    def test_gallery_area_sq_m_raises(self):
        with self.assertRaises(ValueError) as e:
            self.gallery.area_sq_m = 0.0
            self.gallery.area_sq_m = -0.01
        self.assertEqual("Gallery area must be a positive number!", str(e.exception))

    def test_gallery_add_exhibition_return_error(self):
        self.assertEqual(0, len(self.gallery.exhibitions))
        self.gallery.exhibitions["one"] = 1000
        self.assertEqual(1, len(self.gallery.exhibitions))
        result = self.gallery.add_exhibition("one", 2000)
        self.assertEqual('Exhibition "one" already exists.', result)
        self.assertEqual(1, len(self.gallery.exhibitions))

    def test_gallery_add_exhibition_successfully(self):
        self.assertEqual(0, len(self.gallery.exhibitions))
        self.gallery.exhibitions["one"] = 1000
        self.assertEqual(1, len(self.gallery.exhibitions))
        result = self.gallery.add_exhibition("two", 2000)
        self.assertEqual('Exhibition "two" added for the year 2000.', result)
        self.assertEqual(2, len(self.gallery.exhibitions))

    def test_gallery_remove_exhibition_return_error(self):
        self.assertEqual(0, len(self.gallery.exhibitions))
        self.gallery.exhibitions["one"] = 1000
        self.assertEqual(1, len(self.gallery.exhibitions))
        result = self.gallery.remove_exhibition("two")
        self.assertEqual('Exhibition "two" not found.', result)
        self.assertEqual(1, len(self.gallery.exhibitions))

    def test_gallery_remove_exhibition_successfully(self):
        self.assertEqual(0, len(self.gallery.exhibitions))
        self.gallery.exhibitions["one"] = 1000
        self.assertEqual(1, len(self.gallery.exhibitions))
        result = self.gallery.remove_exhibition("one")
        self.assertEqual('Exhibition "one" removed.', result)
        self.assertEqual(0, len(self.gallery.exhibitions))

    def test_gallery_list_exhibitions_open_to_public_false(self):
        self.gallery.open_to_public = False
        result = self.gallery.list_exhibitions()
        self.assertEqual("Gallery Gallery is currently closed for public! Check for updates later on.", result)

    def test_gallery_list_exhibitions_open_to_public_true(self):
        self.gallery.open_to_public = True
        self.gallery.add_exhibition("one", 1000)
        self.gallery.add_exhibition("two", 2000)
        result = self.gallery.list_exhibitions()
        self.assertEqual("one: 1000\ntwo: 2000", result)




from project.gallery import Gallery

from unittest import TestCase

class TestGallery(TestCase):
    def setUp(self):
        self.gallery = Gallery("Name", "City", 120)

    def test_gallery_init(self):
        self.assertEqual("Name", self.gallery.gallery_name)
        self.assertEqual("City", self.gallery.city)
        self.assertEqual(120, self.gallery.area_sq_m)
        self.assertTrue(self.gallery.open_to_public)
        self.assertDictEqual({}, self.gallery.exhibitions)

    def test_gallery_gallery_name_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.gallery.gallery_name = "_1a"
            self.gallery.gallery_name = ""
            self.gallery.gallery_name = "   "
            self.gallery.gallery_name = "test_"
            self.gallery.gallery_name = "t a s"

        self.assertEqual("Gallery name can contain letters and digits only!", str(ex.exception))

    def test_gallery_city_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.gallery.city = ""
            self.gallery.city = None
            self.gallery.city = "   "
            self.gallery.city = "1test"
            self.gallery.city = "@test"

        self.assertEqual("City name must start with a letter!", str(ex.exception))

    def test_gallery_area_sq_m_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.gallery.area_sq_m = 0
            self.gallery.area_sq_m = -0.0001
            self.gallery.area_sq_m = "   "

        self.assertEqual("Gallery area must be a positive number!", str(ex.exception))

    def test_gallery_add_exhibition_already_exists(self):
        self.gallery.exhibitions = { "one": 1 }
        result = self.gallery.add_exhibition("one", 1979)
        self.assertEqual('Exhibition "one" already exists.', result)
        self.assertEqual(1, len(self.gallery.exhibitions))

    def test_gallery_add_exhibition_added_successfully(self):
        self.gallery.exhibitions = { "one": 1 }
        result = self.gallery.add_exhibition("two", 1979)
        self.assertEqual('Exhibition "two" added for the year 1979.', result)
        self.assertEqual(2, len(self.gallery.exhibitions))
        self.assertEqual(1, self.gallery.exhibitions["one"])
        self.assertEqual(1979, self.gallery.exhibitions["two"])

    def test_gallery_remove_exhibition_does_not_exists(self):
        self.gallery.exhibitions = { "one": 1 }
        result = self.gallery.remove_exhibition("two")
        self.assertEqual('Exhibition "two" not found.', result)
        self.assertEqual(1, len(self.gallery.exhibitions))

    def test_gallery_remove_exhibition_successfully(self):
        self.gallery.exhibitions = { "one": 1 }
        result = self.gallery.remove_exhibition("one")
        self.assertEqual('Exhibition "one" removed.', result)
        self.assertEqual(0, len(self.gallery.exhibitions))

    def test_gallery_list_exhibitions_open_to_public_true(self):
        self.gallery.open_to_public = True
        self.gallery.exhibitions = { "one": 1, "two": 2 }
        result = self.gallery.list_exhibitions()
        self.assertEqual('one: 1\ntwo: 2', result)

    def test_gallery_list_exhibitions_open_to_public_false(self):
        self.gallery.open_to_public = False
        self.gallery.exhibitions = { "one": 1, "two": 2 }
        result = self.gallery.list_exhibitions()
        self.assertEqual('Gallery Name is currently closed for public! Check for updates later on.', result)
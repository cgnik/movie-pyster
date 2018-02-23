import unittest
from unittest.mock import MagicMock, patch

from movie_pyster import is_movie, movie_files, is_extension, filename, best_match, best_dict_match, find_image, \
    is_image

import os


class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code


class TestUtil(unittest.TestCase):
    def test_is_extension(self):
        assert (is_extension("a.mkv", ['mkv']))
        assert (is_extension("a.m4v", ['m4v']))
        assert (not is_extension("a.m4v", ['txt']))
        assert (not is_extension("a.txt", ['blu', 'pnu']))

    def test_is_movie(self):
        assert (is_movie("a.mkv"))
        assert (is_movie("a.m4v"))
        assert (not is_movie("a.txt"))

    def test_is_image(self):
        assert (is_image("a.jpg"))
        assert (is_image("a.gif"))
        assert (not is_image("a.txt"))
        assert (not is_image("a.mkv"))
        assert (not is_image("a.m4v"))

    def test_movie_files(self):
        files = ["a.txt", "b.mkv", "c.m4v", "d.urk"]
        os.listdir = MagicMock(return_value=files)
        dir = "blah"
        self.assertEqual(movie_files(dir), ["b.mkv", "c.m4v"])
        os.listdir.assert_called_with(dir)

    def test_filename(self):
        self.assertEqual("urk", filename("urk.bla"))
        self.assertEqual("nub", filename("/nub.flo"))
        self.assertEqual("eLS", filename("/SoME/thIng/eLS.es"))
        self.assertEqual("blu", filename("blu"))

    def test_best_match(self):
        self.assertEqual(0, best_match("urk", ["urk", "boo"]))
        self.assertEqual(0, best_match("bork", ["burk", "boo"]))
        self.assertEqual(1, best_match("blah", ["urk", "blah"]))
        self.assertEqual(1, best_match("bro", ["urk", "boo", "stoo", "flah"]))
        self.assertEqual(2, best_match("urk", ["derp", "dorp", "jurk", "boo"]))
        self.assertEqual(3, best_match("Aliens",
                                       ["Aliens in the attic", "Alien Nation", "My Little Aliens", "Aliens", "Alien"]))
        self.assertEqual(None, best_match("Duomo", "Nanites"))
        self.assertEqual(None, best_match(None, None))

    def test_best_dict_match(self):
        test = [
            {'title': 'donk'},
            {'title': 'wugink'},
            {'title': 'klink'}]
        result = best_dict_match('dink', 'title', test)
        self.assertEqual(test[0], result)
        result = best_dict_match('baaa', 'title', test)
        self.assertEqual(None, result)

    def test_find_images(self):
        files = ["werp.jpg", "flerp.m4v", "slurp.gif", "hurp.jpeg", "jerp.txt"]
        os.listdir = MagicMock(return_value=files)
        self.assertTrue(find_image("werp", "werp"))
        self.assertTrue(find_image("werp", "slurp"))
        self.assertTrue(find_image("werp", "hurp"))
        self.assertFalse(find_image("werp", "flerp"))
        self.assertFalse(find_image("werp", "jerp"))
        os.listdir.assert_called_with("werp")
        self.assertEqual(os.listdir.call_count, 5)

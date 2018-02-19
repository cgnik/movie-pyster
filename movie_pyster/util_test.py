import unittest
from unittest.mock import MagicMock

from movie_pyster import is_movie, movie_files, is_extension, filename

import os


class TestMain(unittest.TestCase):
    def test_is_extension(self):
        assert (is_extension("a.mkv", ['mkv']))
        assert (is_extension("a.m4v", ['m4v']))
        assert (not is_extension("a.m4v", ['txt']))
        assert (not is_extension("a.txt", ['blu', 'pnu']))

    def test_is_movie(self):
        assert (is_movie("a.mkv"))
        assert (is_movie("a.m4v"))
        assert (not is_movie("a.txt"))

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


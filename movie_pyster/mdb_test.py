from unittest import TestCase
from unittest.mock import patch, Mock, MagicMock

from movie_pyster import mdb

import tmdbsimple


class TestMdb(TestCase):

    @patch('tmdbsimple.Configuration')
    def test_configuration(self, c):
        expected = "urk/nok"
        type(c()).info = MagicMock(return_value={'images': {'secure_base_url' : expected}})
        self.assertEqual(mdb.base_url(), expected)

    @patch('tmdbsimple.Search')
    def test_search(self, s):
        expected = ['blah']
        s().movie = Mock(return_value={'results': expected})
        self.assertEquals(mdb.search("Aliens"), expected)
        s().movie.assert_called_with(query="Aliens")

    def test_match_movie(self):
        pass

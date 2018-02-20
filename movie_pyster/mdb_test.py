from unittest import TestCase
from unittest.mock import patch, Mock, PropertyMock

from movie_pyster import mdb

import tmdbsimple


class TestMdb(TestCase):

    @patch('tmdbsimple.Configuration')
    def test_configuration(self, c):
        expected = "urk/nok"
        type(c()).base_url = PropertyMock(return_value=expected)
        self.assertEqual(mdb.base_url(), expected)

    @patch('tmdbsimple.Search')
    def test_search(self, s):
        expected = ['blah']
        s().movie = Mock(return_value={'results': expected})
        self.assertEquals(mdb.search("Aliens"), expected)
        s().movie.assert_called_with(query="Aliens")


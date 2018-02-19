from unittest import TestCase
from unittest.mock import patch, Mock

from movie_pyster import mdb

import tmdbsimple


class TestMdb(TestCase):
    @patch('tmdbsimple.Search')
    def test_search(self, s):
        expected = ['blah']
        s().movie = Mock(return_value={'results': expected})
        result = mdb.search("Aliens")
        self.assertEquals(result, expected)
        s().movie.assert_called_with(query="Aliens")
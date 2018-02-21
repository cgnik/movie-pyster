import tmdbsimple
from movie_pyster.util import best_dict_match


def base_url():
    return tmdbsimple.Configuration().base_url


def search(name):
    return tmdbsimple.Search().movie(query=name)['results']


def best_movie_match(title):
    return best_dict_match(title, 'title', search(title))

import tmdbsimple
from movie_pyster.util import best_dict_match

with open('themoviedb-key.txt', 'rb')as keyfile:
    tmdbsimple.API_KEY = keyfile.read()


def base_url():
    return tmdbsimple.Configuration().base_url


def search(name):
    return tmdbsimple.Search().movie(query=name)['results']

def best_movie_match(title, titles):
    return 0
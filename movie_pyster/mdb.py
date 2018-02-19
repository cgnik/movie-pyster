import tmdbsimple

# with open('themoviedb-key.txt', 'rb')as keyfile:
#     tmdb.API_KEY = keyfile.read()


def search(name):
    return tmdbsimple.Search().movie(query=name)['results']

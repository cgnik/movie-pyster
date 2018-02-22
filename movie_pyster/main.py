from sys import argv
import tmdbsimple

with open(argv[1], 'rb')as keyfile:
    tmdbsimple.API_KEY = keyfile.read()

from os import getcwd

from movie_pyster.util import movie_files, filename, http_fetch
from movie_pyster.mdb import best_movie_match, base_url

# base_url + w780 + poster_path
if __name__ == '__main__':
    dirs = argv[2:] if len(argv) > 2 else [getcwd()]
    base_url = base_url()
    for dir in dirs:
        moviefiles = movie_files(dir)
        for moviefile in moviefiles:
            name = filename(moviefile)
            best = best_movie_match(name)
            if best:
                print(best)
                url = "{}/{}{}".format(base_url, 'w780', best['poster_path'])
                print(url)
                http_fetch(url, name)
            else:
                print("No match for title '{}'".format(name))
    print("Done.")

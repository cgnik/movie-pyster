from sys import argv
import logging
import tmdbsimple

with open(argv[1], 'rb')as keyfile:
    tmdbsimple.API_KEY = keyfile.read()

from os import getcwd

from movie_pyster.util import movie_files, filename, http_fetch
from movie_pyster.mdb import best_movie_match, base_url


class MoviePyster:

    def __init__(self):
        self.logger = logging.getLogger("movie_pyster")
        self.logger.setLevel(logging.INFO)
        con = logging.StreamHandler()
        con.setLevel(logging.INFO)
        self.logger.addHandler(con)

    def log(self, message):
        self.logger.info(message)

    def process(self, dirs):
        image_base_url = base_url()
        count = 0
        for dir in dirs:
            for moviefile in movie_files(dir):
                count = count + 1
                self.update_movie(image_base_url, moviefile)
        self.log("\nDone processing {} movie files from {} directories".format(count, len(dirs)))

    def fetch_movie_image(self, base_url, name, poster_path):
        if poster_path:
            http_fetch("{}/{}{}".format(base_url, 'w780', poster_path), name)
            self.log("Fetched image for {}".format(name))

    def update_movie(self, image_base_url, moviefile):
        name = filename(moviefile)
        best = best_movie_match(name)
        if best:
            self.fetch_movie_image(image_base_url, name, best['poster_path'])
        else:
            self.log("No match for movie {}".format(moviefile))


if __name__ == '__main__':
    dirs = argv[2:] if len(argv) > 2 else [getcwd()]
    MoviePyster().process(dirs)

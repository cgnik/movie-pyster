from sys import argv
from os import getcwd

from movie_pyster.util import movie_files, filename
from movie_pyster.mdb import best_movie_match

if __name__ == '__main__':
    keyfile = argv[2]
    dirs = argv[:2] if len(argv) > 3 else [getcwd()]
    for dir in dirs:
        moviefiles = movie_files(dir)
        for moviefile in moviefiles:
            print("{} matched: {}".format(moviefile, best_movie_match(filename(moviefile))))
    print("Done.")
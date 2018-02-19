import os, re


def is_extension(file, extensions):
    return any(map(lambda e: file.endswith(e), extensions))


def is_movie(file):
    return is_extension(file, ["mkv", "m4v"])


def movie_files(dir):
    return list(filter(lambda m: is_movie(m), os.listdir(dir)))

def filename(filepath):
    names = list(filter(lambda n: n != '', re.findall('([^./\\\\]+)*', filepath)))
    return names[-2] if len(names) > 1 else filepath

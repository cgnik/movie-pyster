import os, re
from fuzzywuzzy import process


def is_extension(file, extensions):
    return any(map(lambda e: file.endswith(e), extensions))


def is_movie(file):
    return is_extension(file, ["mkv", "m4v"])


def movie_files(dir):
    return list(filter(lambda m: is_movie(m), os.listdir(dir)))


def filename(filepath):
    names = list(filter(lambda n: n != '', re.findall('([^./\\\\]+)*', filepath)))
    return names[-2] if len(names) > 1 else filepath


def best_match(query, matches):
    scores = process.extract(query, matches)
    maxScore = max(scores, key=lambda x : x[1])
    best = matches.index(maxScore[0]) if maxScore[1] > 65 else None
    return best


def best_dict_match(query, propname, matches):
    index = best_match(query, list(map(lambda m: m[propname], matches)))
    return matches[index] if index != None else None

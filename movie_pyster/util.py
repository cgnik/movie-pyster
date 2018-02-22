import os, re, requests
import mimetypes
from fuzzywuzzy import process

mimetypes.init()

def http_fetch(url, name):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        ext = mimetypes.guess_all_extensions(r.headers.get('content-type').split(';')[0].strip())[-1]
        with open("{}{}".format(name, ext), 'wb') as f:
            for chunk in r:
                f.write(chunk)


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
    if scores:
        scoremax = max(scores, key=lambda x: x[1])
        return matches.index(scoremax[0]) if scoremax[1] > 65 else None
    return None


def best_dict_match(query, propname, matches):
    index = best_match(query, list(map(lambda m: m[propname], matches)))
    return matches[index] if index != None else None

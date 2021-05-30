
import os
import re
import shlex
import subprocess

from .app import celery
from .conf import SEARCH_TEXT_SH


def tag_words(matchwords: list = None, txt: str = None):

    return re.sub(
        r"\b({})\b".format('|'.join(matchwords)),
        r'<span class="match">\1</span>',
        txt,
        flags=re.IGNORECASE
    )


def context_to_json(string: str = None):

    pattern = r"([a-z0-9]+)\:(.*)"
    data = re.findall(pattern, string)

    out = []
    for dataid, text in data:
        obj = {'dataid': dataid, 'text': text}
        if obj not in out:
            out.append(obj)

    return out


def words_context(words: list = None, path: str = None):

    if not os.path.isdir(path):
        raise ValueError(path)

    try:
        results = subprocess.run(
            shlex.split("sh {} {} {}".format(
                SEARCH_TEXT_SH,
                path,
                '|'.join(words)
            )),
            encoding="utf-8",
            capture_output=True,
            check=True
        )
    except subprocess.CalledProcessError as err:
        # the command exits with a non-zero exit code.
        raise

    return results.stdout


@celery.task
def search_text(container_path: str = None,
                highlight: bool = False,
                words: list = None) -> dict:
    """
    :return: http response that contains a json object
    """

    result = words_context(words=words, path=container_path)
    if highlight:
        result = tag_words(words, result)
    data = context_to_json(result)

    return {
        'success': True,
        'container_path': container_path,
        'highlight': highlight,
        'words': words,
        'data': data
    }

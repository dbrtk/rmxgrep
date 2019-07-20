import os
import re
import shlex
import subprocess

from flask import abort, Flask, jsonify, request

app = Flask(__name__)

SEARCH_CORPUS_SH = os.environ.get('SEARCH_CORPUS_SH')


def tag_words_corpus(matchwords: list = None, txt: str = None):

    return re.sub(
        r"\b({})\b".format('|'.join(matchwords)),
        r'<span class="match">\1</span>',
        txt,
        flags=re.IGNORECASE
    )


def context_to_json(string: str = None):

    pattern = r"([a-z0-9]+)\:(.*)"
    data = re.findall(pattern, string)

    out = {}
    for docid, txt in data:

        if docid not in out:
            out[docid] = []
        else:
            if txt in out[docid]:
                continue
        out[docid].append(txt)

    return out


def words_context(lemma: list = None, path: str = None):

    try:
        results = subprocess.run(
            shlex.split("sh {} {} {}".format(
                SEARCH_CORPUS_SH,
                path,
                '|'.join(lemma)
            )),
            encoding="utf-8",
            capture_output=True,
            check=True
        )
    except subprocess.CalledProcessError as err:
        # the command exits with a non-zero exit code.
        raise

    return results.stdout


@app.route("/", methods=['GET', ])
def search_corpus():
    """
    :return: http response that contains a json object
    """
    payload = request.get_json()
    corpus_path = payload.get('corpus_path')
    lemma = payload.get('lemma')

    if not corpus_path:
        abort(500, "a path to the corpus is required")
    if lemma is None:
        abort(500, "a search string is required")

    result = words_context(lemma=lemma, path=corpus_path)
    result = tag_words_corpus(lemma, result)
    data = context_to_json(result)

    return jsonify({
        'success': True,
        'data': data
    })
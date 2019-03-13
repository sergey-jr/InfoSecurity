from datetime import timedelta
from functools import update_wrapper
import json
from flask import make_response, request, current_app, Flask, jsonify

import ADFGX, ceasar, matrix, pair, viginer, rsa

app = Flask(__name__)
app.debug = True


def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, str):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, str):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)

    return decorator


@app.route('/adfgx', methods=['GET'])
@crossdomain(origin='*')
def get_adfgx_crypto():
    method = request.args.get('method')
    message = request.args.get('message')
    key = request.args.get('key')
    if method == 'encode':
        res = ADFGX.encode(message, key)
    elif method == 'decode':
        alphabet = request.args.get('alphabet')
        res = ADFGX.decode(message, key, alphabet)
    else:
        res = []
    return json.dumps(res, ensure_ascii=False)


@app.route('/caesar', methods=['GET'])
@crossdomain(origin='*')
def get_caesar_crypto():
    message = str(request.args.get('message'))
    key = request.args.get('key')
    method = str(request.args.get('method'))
    if method == str('encode'):
        res = ceasar.caesar_code(message, int(key))
    elif method == str('decode'):
        res = ceasar.decode(message, key)
    else:
        res = []
    return json.dumps(res, ensure_ascii=False)


@app.route('/matrix', methods=['GET'])
@crossdomain(origin='*')
def get_matrix_crypto():
    message = request.args.get('message')
    keys = [request.args.get('key_n'), request.args.get('key_m')]
    method = request.args.get('method')
    if method == 'encode':
        res = matrix.encode(message, keys)
    elif method == 'decode':
        res = matrix.decode(message, keys)
    else:
        res = []
    return json.dumps(res, ensure_ascii=False)


@app.route('/pair', methods=['GET'])
@crossdomain(origin='*')
def get_pair_crypto():
    message = request.args.get('message')
    method = request.args.get('method')
    if method == 'encode':
        lang = request.args.get('lang')
        res = pair.encode(message, lang)
    elif method == 'decode':
        alphabet = request.args.get('alphabet')
        res = pair.decode(message, alphabet)
    else:
        res = []
    return json.dumps(res, ensure_ascii=False)


@app.route('/viginer', methods=['GET'])
@crossdomain(origin='*')
def get_viginer_crypto():
    message = request.args.get('message')
    lang = request.args.get('lang')
    key = request.args.get('key')
    method = request.args.get('method')
    if method in ['encode', 'decode']:
        res = viginer.encode(message, key, lang, method)
    else:
        res = []
    return json.dumps(res, ensure_ascii=False)


@app.route('/rsa', methods=['GET'])
@crossdomain(origin='*')
def get_rsa_crypto():
    message = request.args.get('message')
    lang = request.args.get('lang')
    method = request.args.get('method')
    p = request.args.get('p')
    q = request.args.get('q')
    p, q = int(p), int(q)
    if method == 'encode':
        res = rsa.encode(message, lang, p, q)
    elif method == 'decode':
        e = request.args.get('e')
        e = int(e)
        res = rsa.decode(message, lang, e, p, q)
    else:
        res =[]
    return json.dumps(res, ensure_ascii=False)

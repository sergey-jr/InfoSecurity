from datetime import timedelta
from functools import update_wrapper

from flask import make_response, request, current_app, Flask, jsonify
from receiver import PasswordGenerator

app = Flask(__name__)


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


@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/get/password', methods=['GET'])
@crossdomain(origin='*')
def get_password():
    params = {
        'lu': request.args.get('lu'), 'll': request.args.get('ll'),
        'ru': request.args.get('ru'), 'rl': request.args.get('rl'),
        'yo': request.args.get('yo'), 'you': request.args.get('you'),
        'numbers': request.args.get('numbers'), 'special': request.args.get('special'),
        'k': int(request.args.get('k')), 'v': int(request.args.get('v')), 'n_max': int(request.args.get('n_max')),
        'method': int(request.args.get('method')), 'n': int(request.args.get('n'))
    }
    for k in params:
        if params[k] in ['false', 'False', '0', 'f', 'F']:
            params[k] = False
        elif params[k] in ['true', 'True', '1', 't', 'T']:
            params[k] = True
    password_generator = PasswordGenerator(**params)
    return password_generator.generate_password()


@app.route('/get/password_strength', methods=['GET'])
@crossdomain(origin='*')
def get_password_strength():
    params = {
        'lu': request.args.get('lu'), 'll': request.args.get('ll'),
        'ru': request.args.get('ru'), 'rl': request.args.get('rl'),
        'yo': request.args.get('yo'), 'you': request.args.get('you'),
        'numbers': request.args.get('numbers'), 'special': request.args.get('special'),
        'k': int(request.args.get('k')), 'v': int(request.args.get('v')), 'n_max': int(request.args.get('n_max')),
    }
    for k in params:
        if params[k] in ['false', 'False', '0', 'f', 'F']:
            params[k] = False
        elif params[k] in ['true', 'True', '1', 't', 'T']:
            params[k] = True
    password_generator = PasswordGenerator(**params)
    return jsonify(password_generator.password_strength_analysis())


@app.route('/get/alphabet', methods=['GET'])
@crossdomain(origin='*')
def get_alphabet():
    params = {
        'lu': request.args.get('lu'), 'll': request.args.get('ll'),
        'ru': request.args.get('ru'), 'rl': request.args.get('rl'),
        'yo': request.args.get('yo'), 'you': request.args.get('you'),
        'numbers': request.args.get('numbers'), 'special': request.args.get('special'),
        'k': 10 ** 9, 'v': 10 ** 6, 'n_max': 100,
    }
    for k in params:
        if params[k] in ['false', 'False', '0', 'f', 'F']:
            params[k] = False
        elif params[k] in ['true', 'True', '1', 't', 'T']:
            params[k] = True
    password_generator = PasswordGenerator(**params)
    return jsonify(password_generator.get_ascii_table())

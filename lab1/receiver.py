import string
import random
from numpy import log, array, floor


class PasswordGenerator:
    def __init__(self, **kwargs):
        russian = ''.join([chr(i) for i in range(1040, 1071)])
        enable = {
            'lu': {'enabled': kwargs.get('lu'), 'alphabet': string.ascii_uppercase},
            'll': {'enabled': kwargs.get('ll'), 'alphabet': string.ascii_lowercase},
            'numbers': {'enabled': kwargs.get('numbers'), 'alphabet': string.digits},
            'ru': {'enabled': kwargs.get('ru'), 'alphabet': russian},
            'rl': {'enabled': kwargs.get('rl'), 'alphabet': russian.lower()},
            'special': {'enabled': kwargs.get('special'), 'alphabet': string.punctuation},
            'yo': {'enabled': kwargs.get('yo', False), 'alphabet': 'ё'},
            'you': {'enabled': kwargs.get('you', False), 'alphabet': 'Ё'}
        }
        self.alphabet = ''.join([enable[i]['alphabet'] for i in enable.keys() if enable[i]['enabled']])
        self.n_max = kwargs.get('n_max')
        self.length = kwargs.get('n')
        self.strength = kwargs.get('k')
        self.speed = kwargs.get('v')
        self.method = kwargs.get('method', 1)
        self.a = len(self.alphabet)
        self.n = array([
            floor(log(self.strength) / log(self.a)) + 1,
            floor(log(2 * self.strength - 1) / log(self.a)) + 1,
            floor(log(2 * self.speed * self.strength - 1) / log(self.a)) + 1
        ], dtype=int) if all([self.n_max, self.speed, self.strength, self.a]) else None

    def get_alphabet(self):
        return self.alphabet

    def get_ascii_table(self):
        return [{'number': i, 'code': ord(val), 'symbol': val} for i, val in enumerate(self.alphabet)]

    def password_strength_analysis(self):
        if self.n_max:
            return [{'length': i + 1, 'number': self.password_strength(i + 1)['P'],
                     'average': self.password_strength(i + 1)['S'],
                     'time': self.password_strength(i + 1)['T']} for i in range(self.n_max)]
        return None

    def generate_password(self):
        if self.n[self.method - 1] <= self.n_max:
            if self.n[self.method - 1] <= self.length:
                password = "".join(random.sample(self.alphabet, self.n[self.method - 1]))
            else:
                password = "".join(random.sample(self.alphabet, self.length))
        else:
            password = "".join(random.sample(self.alphabet, self.n_max))
        return password

    def password_strength(self, n):
        return {'P': self.a ** n,
                'S': (self.a ** n + 1) / 2,
                'T': (self.a ** n + 1) / (2 * self.speed)}

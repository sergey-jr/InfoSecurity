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
        self.length = kwargs.get('n_max')
        self.strength = kwargs.get('k')
        self.speed = kwargs.get('v')
        self.method = kwargs.get('method', 1)
        self.a = len(self.alphabet)
        self.n = array([
            floor(log(self.strength) / log(self.a)) + 1,
            floor(log(2 * self.strength - 1) / log(self.a)) + 1,
            floor(log(2 * self.speed * self.strength - 1) / log(self.a)) + 1
        ], dtype=int) if all([self.length, self.speed, self.strength, self.a]) else None

    def get_alphabet(self):
        return self.alphabet

    def get_ascii_table(self):
        return [{'number': i, 'code': ord(val), 'symbol': val} for i, val in enumerate(self.alphabet)]

    def password_strength_analysis(self):
        return array([array([i + 1, *list(self.password_strength(i + 1).values())]) for i in range(self.length)])

    def generate_password(self):
        return "".join(random.sample(self.alphabet, self.n[self.method - 1]))

    def password_strength(self, n):
        return {'P': self.a ** n,
                'S': (self.a ** n + 1) / 2,
                'T': (self.a ** n + 1) / (2 * self.speed)}


# choices = input('Генерация алфавита\n'
#                 'Введите набор из цифр(как минимум 1, через пробел):\n'
#                 '1 - Латиница (верхний регистр)\n'
#                 '2 - Латиница (нижний регистр)\n'
#                 '3 - Кирилица (верхний регистр)\n'
#                 '4 - Кирилица (нижний регистр)\n'
#                 '5 - Цифры\n'
#                 '6 - Знаки припенания + особые символы\n').split()
# password_generator = PasswordGenerator(lu='1' in choices, ll='2' in choices,
#                                        ru='3' in choices, rl='4' in choices,
#                                        numbers='5' in choices, special='6' in choices, k=10 ** 9, n_max=100, v=10 ** 6)
# alphabet = password_generator.get_alphabet()
# ANSI_table = password_generator.get_ascii_table()
# analysis = password_generator.password_strength_analysis()
# password = password_generator.generate_password()
# print()

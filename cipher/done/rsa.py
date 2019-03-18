import string
from numpy import array
from math import gcd, pow
import random


def gen_d(fi):
    # 1<d<=fi
    # НОД(d, fi)=1
    d = random.randint(2, fi)
    while not (fi >= d > 1 and 1 == gcd(d, fi)):
        d += 1
    return d


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def mulinv(a, b):
    """return x such that (x * a) % b == 1"""
    g, x, _ = egcd(a, b)
    if g == 1:
        return x % b


def get_d(e, fi):
    # (e * d) % fi = 1
    return mulinv(e, fi)


def gen_e(n, d, fi):
    # e<n
    # (e * d) % fi = 1
    e = 0
    while not (e < n and (e * d) % fi == 1):
        e += 1
    return e


def encode(message, lang, p, q):
    n = p * q
    fi = (p - 1) * (q - 1)
    russian = ''.join([chr(i).lower() for i in range(ord('а'), ord('я') + 1)])
    message = message.lower()
    for i in range(len(message)):
        if message[i] == 'ё':
            message[i] = 'е'
    if lang == 'ru':
        alphabet = russian
    elif lang == 'en':
        alphabet = string.ascii_lowercase
    d = gen_d(fi)
    e = gen_e(n, d, fi)
    indexes = array([alphabet.index(char) + 1 for char in message])
    c = [int((item ** e) % n) for item in indexes]
    return {'c': c, 'e': e}


def decode(message, lang, e, p, q):
    n = p * q
    fi = (p - 1) * (q - 1)
    d = get_d(e, fi)
    russian = ''.join([chr(i).lower() for i in range(ord('а'), ord('я') + 1)])
    if lang == 'ru':
        alphabet = russian
    elif lang == 'en':
        alphabet = string.ascii_lowercase
    message = array([int(item) for item in message.split()])
    m = array([pow(item, d) % n - 1 for item in message], dtype=int)
    return ''.join([alphabet[item] for item in m])

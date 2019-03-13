import re
import string
from numpy import array


def sum_chr(a, b, alphabet):
    ind = array([alphabet.index(a), alphabet.index(b)])
    sum_ind = ind.sum() % len(alphabet)
    return alphabet[sum_ind]


def dif_chr(a, b, alphabet):
    ind = array([alphabet.index(a), alphabet.index(b)])
    dif = (ind[0] - ind[1]) % len(alphabet)
    return alphabet[dif]


def encode(message, key, lang, method):
    russian = ''.join([chr(i).lower() for i in range(ord('а'), ord('я') + 1)])
    if lang == 'ru':
        alphabet = russian
    elif lang == 'en':
        alphabet = string.ascii_lowercase
    message = re.sub('\s', '', message)
    n = len(message)
    k = n // len(key) + 1
    key = (key * k)[:n]
    encoded = [' ' for _ in range(n)]
    for i in range(n):
        if method == 'encode':
            encoded[i] = sum_chr(message[i], key[i], alphabet)
        if method == 'decode':
            encoded[i] = dif_chr(message[i], key[i], alphabet)
    return ''.join(encoded)

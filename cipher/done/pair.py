import random
import string


def find_char(char, alphabet):
    upper = False
    if char.isupper():
        upper = True
        char = char.lower()
    k = -1
    m = -1
    if char in alphabet[0]:
        m = 1
        for j in range(len(alphabet[0])):
            if char == alphabet[0][j]:
                k = j
                break
    elif char in alphabet[1]:
        m = 0
        for j in range(len(alphabet[1])):
            if char == alphabet[1][j]:
                k = j
                break
    if any([k == -1, m == -1]):
        coded = '-'
    elif k >= len(alphabet[m]):
        if not upper:
            coded = alphabet[m][-1]
    else:
        if not upper:
            coded = alphabet[m][k]
        else:
            coded = alphabet[m][k].upper()
    return coded


def encode(message, lang):
    random.seed()
    if lang == "ru":
        russian = ''.join([chr(i).lower() for i in range(ord('а'), ord('я') + 1)]) + 'ё'
        alphabet = "".join(random.sample(russian, len(russian)))
    elif lang == "en":
        alphabet = "".join(random.sample(string.ascii_lowercase, len(string.ascii_lowercase)))
    n = len(alphabet) // 2
    alphabet = [alphabet[:n + 1], alphabet[n + 1:]]
    coded = ''
    for i in message:
        if i.isalpha():
            coded += find_char(i, alphabet)
        else:
            coded += i
    return alphabet, coded


def decode(message, alphabet):
    decoded = ''
    for i in message:
        if i.isalpha():
            decoded += find_char(i, alphabet)
        else:
            decoded += i
    return decoded

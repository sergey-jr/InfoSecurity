import string
import random
from numpy import array


def encode(message: str, key: str):
    alphabet = random.sample(string.ascii_lowercase, len(string.ascii_lowercase))
    matrix = [[j for j in alphabet[i * 5:(i + 1) * 5]] for i in range(len(alphabet) // 5)]
    a = 'ADFGX'
    liter = message[-1]
    message = ''.join(message.split())
    while (len(message) * 2) % len(key) != 0:
        message += liter
    encoded = ''
    for char in message:
        find = False
        for i in range(5):
            for j in range(5):
                if char == matrix[i][j]:
                    encoded += ''.join([a[i], a[j]])
                    find = True
        if not find:
            encoded += 'ZZ'
    encoded_matrix = array(
        [array([j for j in encoded[i * len(key):(i + 1) * len(key)]]) for i in range(len(encoded) // len(key))])
    encoded_matrix = array([array([j for j in key]), *encoded_matrix]).transpose()
    encoded_matrix = array(sorted(encoded_matrix, key=lambda item: item[0])).transpose()[1:]
    encoded_matrix = array(encoded_matrix).transpose()
    encoded_final = ''.join([''.join(row) for row in encoded_matrix])
    return alphabet, matrix, encoded_final


def decode(message, key, alphabet):
    matrix = array([array([j for j in alphabet[i * 5:(i + 1) * 5]]) for i in range(len(alphabet) // 5)])
    a = 'ADFGX'
    encoded_matrix = array(
        [array([j for j in message[i * len(message) // len(key):(i + 1) * len(message) // len(key)]]) for i in
         range(len(key))]).transpose()
    sorted_key = sorted(key)
    encoded_matrix = array([array([j for j in sorted_key]), *encoded_matrix]).transpose()
    for i in range(len(key)):
        for j in range(len(encoded_matrix)):
            if j != i:
                if key[i] == encoded_matrix[j][0]:
                    encoded_matrix[i], encoded_matrix[j] = list(encoded_matrix[j]), list(encoded_matrix[i])
                    break
    encoded_matrix = encoded_matrix.transpose()[1:]
    encoded_final = ''.join([''.join(row) for row in encoded_matrix])
    decoded = ''
    for i in range(0, len(encoded_final), 2):
        try:
            row, col = a.index(encoded_final[i]), a.index(encoded_final[i + 1])
            decoded += matrix[row][col]
        except ValueError:
            decoded += '?'
    return decoded

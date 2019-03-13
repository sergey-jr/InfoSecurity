def get_next(letter_code, n):
    russian_upper = sorted([ord('Ё'), *[i for i in range(ord('А'), ord('Я') + 1)]])
    russian_lower = sorted([ord('ё'), *[i for i in range(ord('а'), ord('я') + 1)]])
    latin_upper = range(ord('A'), ord('Z') + 1)
    latin_lower = range(ord('a'), ord('z') + 1)
    if letter_code in russian_upper:
        if n + letter_code > ord('Я'):
            n -= ord('Я') - letter_code
            letter_code = ord('А')
            return get_next(letter_code, n)
        else:
            return chr(n + letter_code)
    elif letter_code in russian_lower:
        if n + letter_code > ord('я'):
            n -= ord('я') - letter_code
            letter_code = ord('а')
            return get_next(letter_code, n)
        else:
            return chr(n + letter_code)
    elif letter_code in latin_upper:
        if n + letter_code > ord('Z'):
            n -= ord('Z') - letter_code
            letter_code = ord('A')
            return get_next(letter_code, n)
        else:
            return chr(n + letter_code)
    elif letter_code in latin_lower:
        if n + letter_code > ord('z'):
            n -= ord('z') - letter_code
            letter_code = ord('a')
            return get_next(letter_code, n)
        else:
            return chr(n + letter_code)


def caesar_code(message: str, key: int) -> str:
    translated = ''
    for symbol in message:
        if symbol.isalpha():
            if symbol not in ['Ё', 'ё']:
                translated += get_next(ord(symbol), key)
            else:
                if symbol == 'Ё':
                    translated += get_next(ord('Е'), key)
                else:
                    translated += get_next(ord('е'), key)
        else:
            translated += symbol
    return translated


def decode(message, key):
    return caesar_code(message, -key)

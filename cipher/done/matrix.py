from numpy import array


def encode(message, keys):
    message = ''.join(message.split())
    liter = message[-1]
    n, m = len(keys[0]), len(keys[1])
    while len(message) % n != 0:
        message += liter
    matrix = [[j for j in message[i * n:(i + 1) * n]] for i in range(len(message) // n)]
    while len(matrix) % m != 0:
        tmp = liter * n
        matrix.append([j for j in tmp])
    # add key_n and sort
    matrix = array([array(item) for item in matrix])
    matrix = array([array([j for j in keys[0]]), *matrix]).transpose()
    matrix = array(sorted(matrix, key=lambda item: item[0])).transpose()[1:]
    # add key_m and sort
    key_m = keys[1] * (len(matrix) // m)
    matrix = array(matrix).transpose()
    matrix = array([array([j for j in key_m]), *matrix]).transpose()
    matrix = array([array(matrix[i * m:(i + 1) * m]) for i in range(len(matrix) // m)])
    matrix = array([array(sorted(item, key=lambda row: row[0])) for item in matrix])
    matrix = array([array(item.transpose()[1:]) for item in matrix])
    encoded = ''.join([''.join([''.join(row) for row in item]) for item in matrix])
    return encoded


def decode(message, keys):
    n, m = len(keys[0]), len(keys[1])
    encoded_keys = array([sorted(key) for key in keys])
    encoded = []
    # key_m
    for i in range(len(message) // m):
        if i == 0:
            tmp = [[j for j in message[i * m:(i + 1) * m]]]
        else:
            if i % n == 0:
                if tmp:
                    tmp = [[j for j in encoded_keys[1]], *tmp]
                    encoded.append(array([array(item) for item in tmp]).transpose())
                tmp = [[j for j in message[i * m:(i + 1) * m]]]
            else:
                tmp.append([j for j in message[i * m:(i + 1) * m]])
        if i + 1 == len(message) // m:
            tmp = [[j for j in encoded_keys[1]], *tmp]
            encoded.append(array([array(item) for item in tmp]).transpose())
    encoded = array(encoded)

    for k, item in enumerate(encoded):
        for i in range(len(keys[1])):
            for j, val in enumerate(item):
                if j != i:
                    if keys[1][i] == item[j][0]:
                        encoded[k][i], encoded[k][j] = array(list(encoded[k][j])), array(list(encoded[k][i]))
                        break

    encoded = array([array(item.transpose()[1:]).transpose() for item in encoded])
    # key_n
    encoded = array([array([array([j for j in encoded_keys[0]]), *item]).transpose() for item in encoded])
    for k, item in enumerate(encoded):
        for i in range(len(keys[0])):
            for j, val in enumerate(item):
                if j != i:
                    if keys[0][i] == item[j][0]:
                        encoded[k][i], encoded[k][j] = array(list(encoded[k][j])), array(list(encoded[k][i]))
                        break

    encoded = array([array(item.transpose()[1:]) for item in encoded])
    decoded = ''.join([''.join([''.join(row) for row in item]) for item in encoded])
    return decoded

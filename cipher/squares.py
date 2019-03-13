import random
from numpy import array

random.seed()
russian = ''.join([chr(i).lower() for i in range(ord('а'), ord('я') + 1)])
alphabet = [[[], []], [[], []]]
for i in range(2):
    for j in range(2):
        random.seed()
        tmp = "".join(random.sample(russian, 25))
        for k in range(5):
            tmp_arr = []
            for sym in tmp[k * 5:k * 5 + 5]:
                tmp_arr.append(sym)
            alphabet[i][j] += [tmp_arr]
alphabet = array(alphabet)
print(alphabet)

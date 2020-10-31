from itertools import permutations, product, combinations
from unrar import rarfile
import os
from tqdm import tqdm

codes = [
    ['7ui8'],
    ['3an2'],
    ['a101', 'a1o1'],
    ['e7g5', 'g5e7'],
    ['j26k'],
    ['4S3D'],
    ['a3Y9', 'd3Y9']
    #,    ['h154', 'h1s4']
]

def all_casings(input_string):
    if not input_string:
        yield ""
    else:
        first = input_string[:1]
        if first.lower() == first.upper():
            for sub_casing in all_casings(input_string[1:]):
                yield first + sub_casing
        else:
            for sub_casing in all_casings(input_string[1:]):
                yield first.lower() + sub_casing
                yield first.upper() + sub_casing

def generate_passwords_file(words):
    total = len(list(permutations(words)))

    with open('passwords.txt', 'w') as file:
        for permutacao in tqdm(total = total, iterable=permutations(words)):
            for L in range(0, len(permutacao)+1):
                for subset in combinations(permutacao, L):
                    for word in [''.join(p) for p in product(*subset)]:
                        for password in all_casings(word):
                            file.write(password)
                            file.write('\n')

generate_passwords_file(codes)


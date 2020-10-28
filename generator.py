from itertools import permutations, product, combinations
from unrar import rarfile
import os
from tqdm import tqdm

codes = [
    ['7ui8'],
    ['e7g5', 'g5e7'],
    ['3an2'],
    ['a3Y9', 'd3Y9', '43Y9'],
    ['a101', 'a1o1', 'a10i', 'ai01'],
    ['h154', 'h1s4']
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
    a = 0

    total = len(list(permutations(words)))

    with open('passwords.txt', 'w') as file:
        for permutacao in tqdm(total = total, iterable=permutations(words)):
            for L in range(0, len(permutacao)+1):
                for subset in combinations(permutacao, L):            
                    for word in [''.join(p) for p in product(*subset)]:
                        for password in all_casings(word):                          
                            a +=1
                            file.write(password)
                            file.write('\n')


generate_passwords_file(codes)


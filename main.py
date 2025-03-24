from copy import deepcopy
import FrequencyAnalysis as fa
import encryption as en
import utils as ut
import parser

import json
import random
import multiprocessing

cipher = ut.read_and_clean_text('CIPHER.txt')
comparison = ut.read_and_clean_text('cmp.txt')

analysis_dict = parser.read()

characters_to_translate = len(cipher)


def worker():
    final_dict = { char: '_' for char in ['G', 'N', 'L', 'J', 'M', 'R', 'A', 'U', 'X', 'B', 'C', 'D', 'K', 'V', 'Y', 'S', 'E', 'I', 'F', 'H', 'W', 'O', 'Z', 'T'] }
    
    while True:
        ngram = str(random.randint(2, 3))
        index = random.randint(0, characters_to_translate - int(ngram))
        
        citext = cipher[index:index+int(ngram)]
        translation = '_'        
        
        t = random.randint(0, 10)
        
        translation = analysis_dict[ngram][citext][t]

        for i in range(len(citext)): 
            final_dict[citext[i]] = translation[i]
        
        number = 1
        if en.final_dict_is_regular(final_dict):
            with open(f'solution_{number}_{random.randint(0, 100)}.txt', 'w') as file:
                file.write(json.dumps(final_dict))
                file.write(json.dumps(en.translate(cipher, final_dict)))
            number += 1

if __name__ == '__main__':
    processes = []
    for _ in range(multiprocessing.cpu_count()):
        p = multiprocessing.Process(target=worker)
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
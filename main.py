from copy import deepcopy
import FrequencyAnalysis as fa
import encryption as en
import utils as ut
import parser

import json

cipher = ut.read_and_clean_text('CIPHER.txt')
comparison = ut.read_and_clean_text('cmp.txt')

generate_structure = input("Use existing strucutre.txt or generate new? You need a CIPHER.txt and cmp.txt. There will be the frequency analysis. May take 5 to 10 minutes to generate.\nYes/No")

if generate_structure == "yes": 
    data = fa.get_ngram_dict_sorted_probability(cipher, comparison, 4)
    parser.write(data)

analysis_dict = parser.read()

final_dict = { char: '_' for char in list(map(chr,range(ord('A'),ord('Z')+1))) }

characters_to_translate = int(input("How much characters do you want to use for encryption?"))

while True:         
    c_cipher = cipher[:characters_to_translate]
    
    print("The Cipher to translate: ")
    print(ut.group_in_blocks(c_cipher, 4))
    print("The translation: ")
    print(ut.group_in_blocks(en.translate(c_cipher, final_dict, 1), 4))
    
    ngram = input("What ngram (1-4) would you like to translate?")
    index = int(input("What index? (0-19)"))
    
    citext = c_cipher[index:index+int(ngram)]
    print("Citext: ", citext)
    translation = '_'
        
    using = ""
    t = 0
    while using != "yes" and using!="exit" and t <= len(analysis_dict[ngram][citext])-1:
        translation = analysis_dict[ngram][citext][t]
        final_dict_cp = deepcopy(final_dict)
        for i in range(len(citext)): 
            final_dict_cp[citext[i]] = translation[i]
        
        print("The translation: ")
        print(ut.group_in_blocks(en.translate(c_cipher, final_dict_cp, 1), 4))
        print(translation)
        t+=1
        using = input("Use this? (yes/no/exit)")           

    for i in range(len(citext)): 
        final_dict[citext[i]] = translation[i]
        
    if using == "exit": 
        print("Solution: ")
        print(ut.group_in_blocks(en.translate(c_cipher, final_dict, 1), 4))
        print("\n")
        print(final_dict)
        break
from copy import deepcopy


def frequency_count(cipher, n=1):
    # Erstellen eines Wörterbuchs, um die Häufigkeiten zu speichern
    freq_dict = {}
    # Zählen der Vorkommen jeder Buchstabenkombination der Größe n
    for i in range(len(cipher) - n + 1):
        item = cipher[i:i+n]
        if item in freq_dict:
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1
    # Berechnung der relativen Häufigkeiten
    total_count = sum(freq_dict.values())
    relative_freq_dict = {k: v / total_count for k, v in freq_dict.items()}

    return relative_freq_dict


# returns dicts for n ngram. key is the string with size of n and value is the relative frequency.
def frequency_analysis(cipher: str, ngram: int): 
    rtn = []
    rtn.extend([frequency_count(cipher, i+1) for i in range(ngram)])
    return rtn

# 2*frequency analysis with cipher and cmp.txt and ngram between 1 and 4.
# rtn of this function should be: dict { ngram -> dict { char -> [char] }] }
# ngram von 1 bis n. char der länge n. nach absteigender wahrscheinlichkeit im array sortiert. 
def get_ngram_dict_sorted_probability(cipher: str, cmp: str, ngram: int) -> dict:
    result = {}
    cipher_freqs = frequency_analysis(cipher, ngram)
    cmp_freqs = frequency_analysis(cmp, ngram)
    
    for i in range(ngram):
        ngram_dict_cipher = cipher_freqs[i]
        ngram_dict_cmp = cmp_freqs[i]
        
        ngram_dict = {}
        for cipher in list(ngram_dict_cipher.keys()):
            rel_frq = ngram_dict_cipher[cipher]
            ngram_dict_cmp_cp = deepcopy(ngram_dict_cmp)
            ngram_dict_cmp_cp = {k: v for k, v in sorted(ngram_dict_cmp_cp.items(), key=lambda item: abs(item[1] - rel_frq))}
            ngram_dict[cipher] = list(ngram_dict_cmp_cp.keys())
        
        result[i+1] = ngram_dict
    return result

# encrypt cipher by dict
# n is sice of the cipher sclice to be translated. should be the same sice als string in the dict. 
def translate(cipher: str, dict: dict, n=1)->str:
    results = ''
    for index in range(len(cipher)):
        if cipher[index:index+n] in dict: 
            results += dict[cipher[index:index+n]]
            index+=n
        else:
            results += cipher[index]
    return results

def final_dict_is_regular(final_dict: dict) -> bool:
    values = list(final_dict.values())
    if len(values) != len(set(values)):
        return False
    return True
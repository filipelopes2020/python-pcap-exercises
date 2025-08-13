import string_utils
import math

def halve_strings(string_list):
    to_return = []
    for i in string_list:
        to_return.append(string_utils.halve_string(i))
    
    return to_return


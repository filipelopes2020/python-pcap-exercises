import math

def halve_string(input_string):
    """
    Halves the input string.
    
    :param s: The string to be halved.
    :return: The first half of the string.
    """
    mid = math.ceil(len(input_string) / 2)
    return [input_string[:mid],input_string[mid:]]
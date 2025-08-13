sample_story = '''Once upon a time, there was a beginner programmer named Alice who was eager to learn Python. She tried to learn from books, but found it difficult to grasp the concepts. One day, she stumbled upon an online course.\n
Alice was thrilled. The course was taught by a well-known programmer who made the lessons interesting and easy to understand. The course covered everything a beginner programmer needed, and Alice was finally able to understand how to code in Python.'''


def get_longest_word(lista_splitada):
    maxsize = 0
    #print(lista_splitada)
    for i in lista_splitada:
        if len(i) > maxsize:
            maxsize = len(i)
            word = i            
    return word


xis=get_longest_word(sample_story.split())
print(f'A maior palavra é "{xis}" com {len(xis)} caracteres.')
#print(get_longest_word(sample_story))
#print(f'A maior palavra é "{word}" com {maxsize} caracteres.')
#print(f'A frase tem {len(lista_splitada)} palavras.')  
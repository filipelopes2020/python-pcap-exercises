import string
sample_story = '''Once upon a time, there was a beginner programmer named Alice who was eager to learn Python. She tried to learn from books, but found it difficult to grasp the concepts. One day, she stumbled upon an online course.

Alice was thrilled. The course was taught by a well-known programmer who made the lessons interesting and easy to understand. The course covered everything a beginner programmer needed, and Alice was finally able to understand how to code in Python.'''

#sample_story = '''Once I\'m awaken, I\'ll sacrifice, your soul to the ruler of darkness.'''

def get_longest_word(lista_splitada):
    lista = lista_splitada.replace('.', ' ').replace(',', ' ').split()
    maxsize = 0
    word= ''
    for i in lista:
        if len(i) > maxsize:
            maxsize = len(i)
            word = i            
    return word
    
    
bigest=get_longest_word(sample_story)
print(f'The biggest word is "{bigest}"')

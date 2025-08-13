#for i in 'Hello from the world of Python':
#    print(i,end='=')

sample_story = '''Once upon a time, there was a beginner programmer named Alice who was eager to learn Python. She tried to learn from books, but found it difficult to grasp the concepts. One day, she stumbled upon an online course.

Alice was thrilled. The course was taught by a well-known programmer who made the lessons interesting and easy to understand. The course covered everything a beginner programmer needed, and Alice was finally able to understand how to code in Python.'''


lista_splitada=sample_story.split()
maxsize = 0
print(lista_splitada)
for i in lista_splitada:
    if len(i) > maxsize:
        maxsize = len(i)
        word = i

print(f'A maior palavra é "{word}" com {maxsize} caracteres.')
print(f'A frase tem {len(lista_splitada)} palavras.')   


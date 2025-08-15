try:
    stream = open('animals.txt')
    # your code goes here
    stream.close()
except Exception as e:
    print('An error occurred: ', e)
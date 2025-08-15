try:
    value = int(input('Enter an int: '))
    print(1/value)
except:
    print('Something went wrong')
else:
    print('Eveyrthing is perfect')
finally:
    print('I am always printed!')
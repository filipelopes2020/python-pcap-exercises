list_1 = list('Chewie')
list_2 = list('Han')
list_3 = list('Luke')
    
try:
    list_1=list_2
    list_2.insert(0,list_3[0])
    assert list_1[0] == 'H'
except:
    print('Error')
else:
    print('OK')
finally:
    print('Done')

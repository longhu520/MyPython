def div(a, b) :
    try :
        print(a/b)
    except ZeroDivisionError :
        print("attetion, division par 0")
    except TypeError :
        print('il faut des intR')
    print('Continuons...')




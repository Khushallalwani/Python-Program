'''
try:
    print(x)
except NameError:
    print("variable x is not defined")
except:
    print("something wrong")
'''
  
'''
try:
    print('hello')
except:
    print('Something went wrong')   
else:
    print("nothing went wrong")
    '''

'''
try:    
    print('hello')
except:
    print("Something went wrong")
finally:
    print("the try except is finished") 
'''

'''
try:
    f=open('hlo.txt','w+')
    try:
        f.write("Hello")
    except:
        print("something went wrong")
    finally:
        f.close()
except:
    print("something file not found")  
'''
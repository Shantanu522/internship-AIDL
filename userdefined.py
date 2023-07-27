def func():
 print('hi')
 
func()

def abc1():
    print('no input no output')
    
def abc(x):
    print(f'its fetching x={x} no output')
    
def abc3():
    return "its a string returned from function as output"
        
def abc4(x,y):
    return x*2,y+x+y

a = abc1()
print(a)

a4 = abc4(5,8)
print(a4)

a41,a42 = abc4(5,8)
print(a41)
print(a42)

abc4(y=5,x=8)
abc4(5,y=8)

#abc4(y=5,8) not allowed
#abc4(x=9,y=5,z=4) not allowed

#default arguments to function
def abc5(x=1,y=0):
    return x*2,y+x+y
print(abc5(4))
print(abc5())
print(abc5(3,2))

#*args and **kwargs
def abc6(x=1,y=0, *p , **q ):
    print(x*2,y+x+y)

    print(p)
    print(q)    

abc6()
abc6(5,4)
abc6(5,6,3,5,7,'hi',23)
abc6(3,5,3,6,8,9,'hi',m=23,n=[4,7,8])

#error handling exception handling
try:
   a=10
   b=int(input('enter the number:'))
   d=(a/b)
   print(d)
except ValueError as err:
   print(err)
   print(a)
   
except KeyboardInterrupt as err:
    print('error')   
except Exception as err:
    print(err)   
    
else:
    print('all ok')    
finally:
    print('final')
    
      
print('done')

# In python 
# a function can be assigned to a variable
# passed as a argument to a function
# defined inside another function
# returned from another function
a=10
def xyz():
    print(a)
    
print(a)
xyz() 

def abc(x,y):
    return x+y
k=abc
k
abc
def pot():
    print('pot')
def pqr(f):
    f() 
pqr(pot)          

def basket():
    def dox():
        print('nox')
    dox()
    
basket() 

def hi(f,m,n):
    return f,m+n

p=hi(pot,3,4)

p,_ = hi(pot,3,4)
p()       

#Decorator
def decorate(f):
    def special():
        print('special function')
        f()
        print('decorated')
    return special


def simple():
    print('simple')

simple=decorate(simple)
print(simple()) 

def d1(f):
    def n1():
        print('e1')
        f()
        print('decorated')
    return n1

@d1
@d1
def s1():
    print('simple')
    
    
simple() 

## Anonymous functions

def normal(x,y):
    return x*y
m=normal(4,5)
print(m)
      
normals=lambda x,y:x*y
normals(4,5)

def my_mapper(func,values):
    result=[]
    for value in values:
        result=result+[func(value)]
    return result 

data=[3,6,4,3,3]

print(my_mapper(lambda x:x*2,data))
print(my_mapper(lambda x:x*2 if x%2 else x/2,data))
print(my_mapper(lambda x:str(x),data))
def first(v):
    return v*2
def second(v):
    return v*2 if v%2 else v/2
def third(v):
    return str(v)
print(my_mapper(first,data))
print(my_mapper(second,data))
print(my_mapper(third,data))  
range(10)
for i in range(10):
    print(i)
    
list(range(10))
def  normal():
    yield  5
    yield  6
    yield 'hi'
    
b=normal()
b    

normal
next(b)
next(b)
next(b)

for i in b:
    print(i)
    
list(b)

a=[4,5,6,7,8]
def gen(data):
    for i in data:
       yield i
       
b=[]
for i in gen(a):
    b.append(i*2)
print(b) 
a

b1=map(lambda x:x*2,a)          
b2=map(lambda x:x*2 if x%2 else x/2,a)
print(b1)
print(b2) 

# def my_map(func,data):
#   for d in data:
#     yield func(d)       

# def my_filter(func,data):
#   for d in data:
#     if func(d):
#       yield d

p=[3,5,3,7,8,4,5,6]
p1=[i for i  in b if i%2]
p2=filter(lambda x:x%2==1,p)
print(p)
print(p1)
print(list(p2))

x=[3,4,5,6]
y=[3,5,4,7]
print(x+y)
print(list(zip(x,y)))


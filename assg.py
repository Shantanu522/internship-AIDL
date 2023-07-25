#fibonacci series
nterms = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0
if nterms <= 0:
   print("Please enter a positive integer")

elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)

else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
   
       n1 = n2
       n2 = nth
       count += 1
       
#print your name    
height = 5
width = (2 * height) - 1
  
def abs(d):
    if d < 0:
        return -1*d
    else:
        return d



def printS() :
    for i in range(0,height) :
        for j in range(0,height) :
            if ( (i == 0 or i == height // 2 or i == height - 1) ):
                print("*",end="")
            elif ( i < height // 2 and j == 0 ) :
                print("*",end="")
            elif ( i > height // 2 and j == height - 1 ) :
                print("*",end="")
            else :
                print(end=" ")
        print()
def printH() :
      
    for i in range(0,height) :
        print("*",end="")
        for j in range(0,height) :
            if ( (j == height - 1) or (i == height // 2) ):
                print("*",end="")
            else :
                print(end=" ")
        print()
def printA():
  
    n = width // 2
    for i in range(0, height):
        for j in range(0, width+1):
            if (j == n or j == (width - n) or (i == (height // 2) and j > n and j < (width - n))):
                print("*", end="")
            else:
                print(end=" ")
        print()
        n = n-1
def printN() :
    counter = 0
    for i in range(0,height) :
        print("*",end="")
        for j in range(0,height+1) :
            if ( j == height ):
                print("*",end="")
            elif ( j == counter) :
                print("*",end="")
            else :
                print(end=" ")
        counter = counter + 1
        print()
def printT() :
    for i in range(0,height) :
        for j in range(0,height) :
            if ( i == 0 ):
                print("*",end="")
            elif ( j == height // 2 ) :
                print("*",end="")
            else :
                print(end=" ")
        print()
def printA():
  
    n = width // 2
    for i in range(0, height):
        for j in range(0, width+1):
            if (j == n or j == (width - n) or (i == (height // 2) and j > n and j < (width - n))):
                print("*", end="")
            else:
                print(end=" ")
        print()
        n = n-1
def printN() :
    counter = 0
    for i in range(0,height) :
        print("*",end="")
        for j in range(0,height+1) :
            if ( j == height ):
                print("*",end="")
            elif ( j == counter) :
                print("*",end="")
            else :
                print(end=" ")
        counter = counter + 1
        print()
def printT() :
    for i in range(0,height) :
        for j in range(0,height) :
            if ( i == 0 ):
                print("*",end="")
            elif ( j == height // 2 ) :
                print("*",end="")
            else :
                print(end=" ")
        print()
def printA():
  
    n = width // 2
    for i in range(0, height):
        for j in range(0, width+1):
            if (j == n or j == (width - n) or (i == (height // 2) and j > n and j < (width - n))):
                print("*", end="")
            else:
                print(end=" ")
        print()
        n = n-1
def printN() :
    counter = 0
    for i in range(0,height) :
        print("*",end="")
        for j in range(0,height+1) :
            if ( j == height ):
                print("*",end="")
            elif ( j == counter) :
                print("*",end="")
            else :
                print(end=" ")
        counter = counter + 1
        print()
def printU() :
    for i in range(0,height) :
        if (i != 0 and i != height - 1) :
            print("*",end="")
        else :
            print(end = " ")
        for j in range(0,height) :
            if ( ((i == height - 1) and j >= 0 and j < height - 1) ):
                print("*",end="")
            elif ( j == height - 1 and i != 0 and i != height - 1 ) :
                print("*",end="")
            else :
                print(end=" ")
        print()
def printPattern(character) : 
      
    if character == 'A' : return  printA()
    elif character == 'N': return printN(),
    elif character == 'S': return printS(),
    elif character == 'T': return printT(),
    elif character == 'U': return printU(),
    else : printH()
  

if __name__ == "__main__":
    character = 'S'
    printPattern(character)
    character = 'H'
    printPattern(character) 
    character = 'A'
    printPattern(character) 
    character = 'N'
    printPattern(character) 
    character = 'T'
    printPattern(character) 
    character = 'A'
    printPattern(character) 
    character = 'N'
    printPattern(character) 
    character = 'U'
    printPattern(character) 
           
           
 #create student database using python
 
class Student:
 

    def __init__(self, name, rollno, m1, m2):
        self.name = name
        self.rollno = rollno
        self.m1 = m1
        self.m2 = m2
 

    def accept(self, Name, Rollno, marks1, marks2):
   
 
        ob = Student(Name, Rollno, marks1, marks2)
        ls.append(ob)
 
    def display(self, ob):
        print("Name : ", ob.name)
        print("RollNo : ", ob.rollno)
        print("Marks1 : ", ob.m1)
        print("Marks2 : ", ob.m2)
        print("\n")
 

    def search(self, rn):
        for i in range(ls.__len__()):
            if(ls[i].rollno == rn):
                return i
 
    def delete(self, rn):
        i = obj.search(rn)
        del ls[i]
 
    
    def update(self, rn, No):
        i = obj.search(rn)
        roll = No
        ls[i].rollno = roll
 
 
ls = []

obj = Student('', 0, 0, 0)
 
print("\nOperations used, ")
print("\n1.Accept Student details\n2.Display Student Details\n3.Search Details of a Student\n4.Delete Details of Student\n5.Update Student Details\n6.Exit")
 

obj.accept("A", 1, 100, 100)
obj.accept("B", 2, 90, 90)
obj.accept("C", 3, 80, 80)
 

print("\n")
print("\nList of Students\n")
for i in range(ls.__len__()):
    obj.display(ls[i])
 

print("\n Student Found, ")
s = obj.search(2)
obj.display(ls[s])
 

obj.delete(2)
print(ls.__len__())
print("List after deletion")
for i in range(ls.__len__()):
    obj.display(ls[i])
 

obj.update(3, 2)
print(ls.__len__())
print("List after updation")
for i in range(ls.__len__()):
    obj.display(ls[i])
 

print("Thank You !")          
class Abc:
    pass
x=Abc()
x
# class may have
# methods
# 1 user defined
# 2 special/dunders/magic methods
# 3 decorated methods
# Attributes
# 1 instance attributes
# 2 class attributes

# inheritance-single level,multilevel,hierarchical,multiple

class Abc():
    a=10
    b=20
    def show(p):
     print(p.a,Abc.b)
     
x=Abc()
print(x)
x.show()
# can use self in place of p and  put self.a
x.a
y=Abc()
z=Abc()
y.show()
x.show()
x.a=45
y.a=100
Abc.b=200
x.show()
y.show()
z.show()

class Abc():
    def __init__(self,a=10,b=20):
        self.a=a
        Abc.b=b

    def show(self):
        print(self.a,Abc.b)
x=Abc()
y=Abc(a=30)
z=Abc(a=15)
x.show()
y.show()
z.show()
w=Abc(b=30)
w.show()

class pqr(Abc):
    def __init__(self, a=10, b=20):
        super().__init__(a, b)
    def simple(self):
        print('simple')
p=pqr()
p.simple()    
p.show()

#GUI development in python
import tkinter as ktr

app=ktr.Tk(__name__)
app.geometry('400x400')
app.title('first gui')
app.mainloop()

#GUI development in python
import tkinter as ktr

app=ktr.Tk(__name__)
app.geometry('400x400')
app.title('first gui')
a=ktr.Label(app,text='showing text')
a.pack()
ktr.Label(app,text='showing text method next').pack()
app.mainloop()

app=ktr.Tk(__name__)
app.geometry('400x400')
app.title('first gui')
a=ktr.Label(app,text='showing text')
a.grid(row=0,column=0)
ktr.Label(app,text='showing text method next').grid(row=1,column=1)
app.mainloop()
var1=ktr.Variable()
var1.set('initial value')
var2=ktr.Variable()
ktr.Entry(app,textvariable=var2).grid(row=1,column=1)
 
def putText():
    var1.set(var2.get())
ktr.Button(app,text='put',command=putText).grid(row=2,column=1)    
     




   


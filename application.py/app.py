import tkinter as ttk
from tkinter import font
app=ttk.Tk()
app.title('Attendance system')
app.geometry('400x400')

font_=font.Font(size=20)
ttk.Label(app,text='face recognition based attendance system',font=font_,fg='black').pack()

def register():
    app.destroy()
    with open('opr','w') as f:
        f.write('register')
    import login_admin    
    
def attendance():
    print('attendance')
    import attendance
    attendance.attendance()
    
def clear_data():
     app.destroy()
     with open('opr','w') as f:
        f.write('clear')
     import login_admin    
    
ttk.Button(app,text='Register',command=register,font=font_,height=3,width=15,bg='red').pack(expand=True)
ttk.Button(app,text='attendance',command=attendance,font=font_,height=3,width=15,bg='green').pack(expand=True)    
ttk.Button(app,text='clear data',command=clear_data,font=font_,height=3,width=15,bg='blue').pack(expand=True)        

app.mainloop()
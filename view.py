from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import pymysql

def on_enter(event):
        if usernameentry.get()=='Username':
            usernameentry.delete(0,END)

def on_enter1(event):
        if passwordentry.get()=='Password':
            passwordentry.delete(0,END)
def display():
    con=pymysql.connect(host='',user='',password='',database='dataproject')
    cursor=con.cursor()
    query='select * from Customer where User=%s and Password=%s'
    cursor.execute(query,(usernameentry.get(),passwordentry.get()))
    row=cursor.fetchone()
    if row==None:
        messagebox.showerror("Error","Incorrect Credentials")
    else:
        name=Label(view,text= str(row[1]))
        name.grid(row=0,column=0)
        balance=Label(view,text=str(row[3]))
        balance.grid(row=0,column=1)
        number=Label(view,text=str(row[4]))
        number.grid(row=0,column=2)
view=Tk()
view.title("View Balance")
bgimage=ImageTk.PhotoImage(file='bg.jpg')
bglabel=Label(view,image=bgimage)
bglabel.grid(row=0,column=0)
heading=Label(view,text="BALANCE",font=("Microsoft Yahei UI Light",20,'bold'),bg='white',fg='firebrick1')
heading.place(x=625,y=120)

usernameentry=Entry(view,width=25,font=("Microsoft Yahei UI Light",11,'bold'),bd=0,fg='firebrick1')
usernameentry.place(x=580,y=200)
usernameentry.insert(0,'Username')
usernameentry.bind('<FocusIn>',on_enter)
frame1=Frame(view,width=250,height=2,bg='firebrick1').place(x=580,y=222)


passwordentry=Entry(view,width=25,font=("Microsoft Yahei UI Light",11,'bold'),bd=0,fg='firebrick1')
passwordentry.place(x=580,y=260)
passwordentry.insert(0,'Password')
passwordentry.bind('<FocusIn>',on_enter1)
frame2=Frame(view,width=250,height=2,bg='firebrick1').place(x=580,y=282)


loginbutton=Button(view,text="View",font=('open sans',15,'bold'),fg='white',bg='firebrick1',bd=0,width=19,command=display)
loginbutton.place(x=578,y=312)


view.mainloop()

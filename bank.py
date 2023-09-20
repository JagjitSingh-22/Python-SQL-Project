from tkinter import*
from tkinter import messagebox
from PIL import ImageTk
import pymysql


def forgot():
    root.destroy()
    import reset
def signup():
    root.destroy()
    import signup
def hide():
    eyeimg.config(file='closeye.png')
    passwordentry.config(show='*')
    eyebutton.config(command=show)

def show():
     eyeimg.config(file='openeye.png')
     passwordentry.config(show='')
     eyebutton.config(command=hide)


def on_enter(event):
    if usernameentry.get()=='Username':
        usernameentry.delete(0,END)

def on_enter1(event):
    if passwordentry.get()=='Password':
         passwordentry.delete(0,END)

def loginuser():
    if usernameentry.get()=='' or passwordentry.get()=='':
        messagebox.showerror("Error","All fields are required")
    else:
        try:
            con=pymysql.connect(host='',user='',password='')
            cursor=con.cursor()
        except:
            messagebox.showerror("Error","Connection is not established try again")
            return
        query='use dataproject'
        cursor.execute(query)
        query='select * from Customer where User=%s and Password=%s'
        cursor.execute(query,(usernameentry.get(),passwordentry.get()))
        #k=passwordentry.get()
        row=cursor.fetchone()
        #print(row[4])
        if row==None:
            messagebox.showerror("Error","Invalid Username or Password")
        else:
            messagebox.showinfo("Welcome","Login is Successful")
            root.destroy()
            import mainmenu
            '''
            def logout():
                main.destroy()
                import bank 
            def new():
                main.destroy()
                import newtransaction
            def view():
                main.destroy()
                import view
            def update():
                def updatedata():
                    query='update Customer set User=%s where Password=%s'
                    cursor.execute=(query,(userentry.get(),k))
                main.destroy()
                up=Tk()
                up.title("Update Record")
                bgimage=ImageTk.PhotoImage(file='bg.jpg')
                bglabel=Label(up,image=bgimage)
                bglabel.grid(row=0,column=0)
                heading=Label(up,text="UPDATE",font=("Microsoft Yahei UI Light",20,'bold'),bg='white',fg='firebrick1')
                heading.place(x=635,y=120)
                username=Label(up,text="Update Username:",font=("Microsoft Yahei UI Light",12,'bold'),fg='firebrick1',bg='white').place(x=572,y=180)
                userentry=Entry(up,width=25,font=("Microsoft Yahei UI Light",10,'bold'),fg='white',bg='firebrick1')
                userentry.place(x=575,y=205)


                balancelabel=Label(up,text="Update Balance:",font=("Microsoft Yahei UI Light",12,'bold'),fg='firebrick1',bg='white').place(x=572,y=230)
                balance1entry=Entry(up,width=25,font=("Microsoft Yahei UI Light",10,'bold'),fg='white',bg='firebrick1')
                balance1entry.place(x=575,y=255)

                nolabel=Label(up,text="Update Mobile Number:",font=("Microsoft Yahei UI Light",12,'bold'),fg='firebrick1',bg='white').place(x=572,y=280)
                noentry=Entry(up,width=25,font=("Microsoft Yahei UI Light",10,'bold'),fg='white',bg='firebrick1')
                noentry.place(x=575,y=305)

                loginbutton=Button(up,text="Update",font=('open sans',15,'bold'),fg='white',bg='firebrick1',activebackground='firebrick1',activeforeground='white',bd=0,command=updatedata)
                loginbutton.place(x=630,y=360)
            #gui part
            main=Tk()
            main.title("Main Menu")
            bgimage=ImageTk.PhotoImage(file='bg.jpg')
            bglabel=Label(main,image=bgimage)
            bglabel.grid(row=0,column=0)
            heading=Label(main,text="MAIN MENU",font=("Microsoft Yahei UI Light",23,'bold'),bg='white',fg='firebrick1')
            heading.place(x=605,y=120)
            button1=Button(main,width=19,text="New Transaction",font=("Microsoft Yahei UI Light",11,'bold'),fg="white",bg="firebrick1",activeforeground="white",activebackground="firebrick1",command=new).place(x=605,y=200)
            button2=Button(main,width=19,text="View Balance",font=("Microsoft Yahei UI Light",11,'bold'),fg="white",bg="firebrick1",activeforeground="white",activebackground="firebrick1",command=view).place(x=605,y=260)
            button3=Button(main,width=19,text="Update Record",font=("Microsoft Yahei UI Light",11,'bold'),fg="white",bg="firebrick1",activeforeground="white",activebackground="firebrick1",command=update).place(x=605,y=320)
            logout=Button(main,text="Logout",font=("Microsoft Yahei UI Light",11,'bold'),fg="white",bg="firebrick1",command=logout).place(x=670,y=390)
            main.mainloop()
            '''


#gui part
root=Tk()
root.title("Login Menu")
bgimage=ImageTk.PhotoImage(file='bg.jpg')
bglabel=Label(root,image=bgimage)
bglabel.grid(row=0,column=0)
heading=Label(root,text="USER LOGIN",font=("Microsoft Yahei UI Light",23,'bold'),bg='white',fg='firebrick1')
heading.place(x=605,y=120)
usernameentry=Entry(root,width=25,font=("Microsoft Yahei UI Light",11,'bold'),bd=0,fg='firebrick1')
usernameentry.place(x=580,y=200)
usernameentry.insert(0,'Username')
usernameentry.bind('<FocusIn>',on_enter)
frame1=Frame(root,width=250,height=2,bg='firebrick1').place(x=580,y=222)

passwordentry=Entry(root,width=25,font=("Microsoft Yahei UI Light",11,'bold'),bd=0,fg='firebrick1')
passwordentry.place(x=580,y=260)
passwordentry.insert(0,'Password')
passwordentry.bind('<FocusIn>',on_enter1)
frame2=Frame(root,width=250,height=2,bg='firebrick1').place(x=580,y=282)
eyeimg=PhotoImage(file="openeye.png")
eyebutton=Button(root,image=eyeimg,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyebutton.place(x=800,y=255)


forgetbutton=Button(root,text="Forgot password ?",font=("Microsoft Yahei UI Light",9,'bold'),fg='firebrick1',bd=0,bg='white',activebackground='white',cursor='hand2',command=forgot)
forgetbutton.place(x=715,y=285)

loginbutton=Button(root,text="Login",font=('open sans',15,'bold'),fg='white',bg='firebrick1',bd=0,width=19,command=loginuser)
loginbutton.place(x=578,y=320)


newbutton=Button(root,text="Don't have an account?",font=("Microsoft Yahei UI Light",9,'bold'),fg='firebrick1',bd=0,bg='white',activebackground='white',cursor='hand2')
newbutton.place(x=615,y=370)
Signup=Button(root,text="Signup",font=('open sans',9,'bold underline'),bg='white',fg='blue',bd=0,cursor='hand2',activebackground='white',activeforeground='blue',command=signup).place(x=773,y=370)



root.mainloop()

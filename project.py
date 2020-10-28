from tkinter import *
from tkinter import messagebox
from random import *

# layout
root = Tk()
root.title('LPG booking system')
root.geometry('400x400')


# root window labels
image1=PhotoImage(file="cylinder.png")
label=Label(root,image=image1)
label.place(x=0,y=0,relwidth=1,relheight=1)
title_label = Label(root, text='LPG SYSTEM',font=('Helvetica',16))
title_label.grid(row=0, column=0, columnspan=2,sticky=N, ipadx=20,ipady=10, padx=30, pady=20)

new_con_label = Label(root,text='Select Your Choice:',font=('Helvetica',12))
new_con_label.grid(row=1,column=0,columnspan=2, ipadx=20,ipady=20,padx=30,pady=(20,10))


# root window functions
def new_con_lpg():
    new_con = Tk()
    new_con.geometry('400x450')
    new_con.title('Enter Details')

    # labels
    Label(new_con,text='Enter Your Details',font=('Helvetica',16)).grid(row=0,column=0,columnspan=2,padx=10,pady=10,
                                                                        ipadx=10,ipady=10)
    Label(new_con,text='Name:').grid(row=1,column=0,sticky=W,padx=10,pady=10,ipadx=10)
    Label(new_con, text='Mobile Number:').grid(row=2, column=0, sticky=W, padx=10, pady=10, ipadx=10)
    Label(new_con, text='Email:').grid(row=3, column=0, sticky=W, padx=10, pady=10, ipadx=10)
    Label(new_con, text='Create Password:').grid(row=4, column=0, sticky=W, padx=10, pady=10, ipadx=10)
    Label(new_con, text='Address:').grid(row=5, column=0, sticky=W, padx=10, pady=10, ipadx=10)
    Label(new_con, text='Aadhar Card Number:').grid(row=6, column=0, sticky=W, padx=10, pady=10, ipadx=10)

    # entry boxes
    name = Entry(new_con,width=20)
    name.grid(row=1,column=1,sticky=E,padx=10,pady=10,ipadx=10)

    mobile = Entry(new_con,width=20)
    mobile.grid(row=2,column=1,sticky=E,padx=10,pady=10,ipadx=10)

    email = Entry(new_con, width=20)
    email.grid(row=3, column=1, sticky=E, padx=10, pady=10, ipadx=10)

    password = Entry(new_con,width=20)
    password.grid(row=4,column=1,sticky=E, padx=10, pady=10, ipadx=10)

    address = Entry(new_con, width=20)
    address.grid(row=5, column=1, sticky=E, padx=10, pady=10, ipadx=10)

    aadhar = Entry(new_con, width=20)
    aadhar.grid(row=6, column=1, sticky=E, padx=10, pady=10, ipadx=10)



    #functions
    def saveIt():
        if(len(password.get())<8):
            messagebox.showerror('Error','Password Must have at Least 8 Characters')
        elif (len(name.get())==0 or len(mobile.get())<10 or len(email.get())==0 or email.get().find('@')==-1
              or len(address.get())==0 or len(aadhar.get())!=12 or not aadhar.get().isnumeric() or not mobile.get().isnumeric()):
            messagebox.showwarning('Warning','Insert Valid Details')
        else:
            d=0
            ID = aadhar.get() + '\n'
            data = open("Connections Details.txt", "r")
            for i in data.readlines():
                if i == ID:
                    d=1
                    break
            data.close()

            if d:
                messagebox.showinfo('INFO','Aadhar Card Number Already Registered')
            else:
                data = open("Connections Details.txt", "a")
                data.write(name.get() + '\n')
                data.write(mobile.get() +" "+ password.get()+ '\n')
                data.write(email.get() + '\n')
                data.write(address.get() + '\n')
                data.write(aadhar.get() + '\n')
                messagebox.showinfo('Saved!','Connection Created!\n\n Remember your Password:\n' + str(password.get()))
                data.close()

    def clearIt():
        name.delete(0, END)
        mobile.delete(0, END)
        email.delete(0, END)
        address.delete(0, END)
        aadhar.delete(0, END)


    # buttons
    save = Button(new_con,text='Create Account',command=saveIt)
    save.grid(row=7, column=0, sticky=W, padx=10, pady=10, ipadx=10)

    clear_fields = Button(new_con,text='Clear',command=clearIt)
    clear_fields.grid(row=7, column=1, sticky=W, padx=10, pady=10, ipadx=35)

    cancel_btn = Button(new_con,text='Close',command=new_con.quit)
    cancel_btn.grid(row=8, column=0, sticky=W, padx=10, pady=10, ipadx=33)


def order_lpg():
    order_new = Tk()
    order_new.geometry('400x400')
    order_new.title('Order')

    # labels
    Label(order_new,text='Enter Credentials',font=('Helventica',16)).grid(row=0,column=0,sticky=W,columnspan=2,padx=10,
                                                                          pady=10,ipadx=10,ipady=10)
    Label(order_new,text='Mobile Number/ID:').grid(row=1,column=0,sticky=W,padx=10,pady=10,ipadx=10)
    Label(order_new, text='Password:').grid(row=2, column=0,sticky=W, padx=10, pady=10, ipadx=10)


    # entry boxes
    id = Entry(order_new,width=20)
    id.grid(row=1,column=1,sticky=E,padx=10,pady=10,ipadx=10)

    password = Entry(order_new, width=20)
    password.grid(row=2, column=1, sticky=E, padx=10, pady=10, ipadx=10)

    #functions
    def clearIt():
        id.delete(0, END)
        password.delete(0, END)

    def orderIt():
        # search id for verification
        d=0
        s=str(id.get()+" "+password.get()+'\n')
        data = open('Connections Details.txt','r')
        for i in data.readlines():
            if i == s:
                d=1
                break
        data.close()
        if d==0:
            messagebox.showerror('Error','Wrong Credentials')
        else:
            OTP = randint(100000,1000000)
            messagebox.showinfo('Done','Order Confirmed\n OTP: '+ str(OTP))


    # buttons
    order_btn = Button(order_new,text='Confirm Order',command=orderIt)
    order_btn.grid(row=3, column=0, padx=10, pady=10, ipadx=10)

    clear_btn = Button(order_new,text='Clear',command=clearIt)
    clear_btn.grid(row=3, column=1, padx=10, pady=10, ipadx=30)



# root window buttons
new_connection = Button(root,text='New LPG Connection',command=new_con_lpg)
new_connection.grid(row=2,column=0,sticky=N,padx=30,pady=10,ipadx=5,ipady=5)

order_lpg = Button(root,text='Order new LPG Cylinder',command=order_lpg)
order_lpg.grid(row=2,column=1,sticky=N,padx=30,pady=10,ipadx=5,ipady=5)



# mainloop
root.mainloop()

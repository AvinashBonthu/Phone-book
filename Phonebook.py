from Tkinter import *
from tkMessageBox import *
import sqlite3
con=sqlite3.Connection('Phonebook1')
cur=con.cursor()
cur.execute("PRAGMA foreign_keys=ON")
cur.execute("create table if not exists phonebook(contactid integer primary key autoincrement,fname varchar(30),mname varchar(30),lname varchar(30),company varchar(30),address varchar(30),city varchar(15),pin number(6),website varchar(50),dob varchar(30))")
cur.execute("create table if not exists phonenumber(contactid integer,contact_type varchar2(20),phone_number number(10),primary key(contactid,phone_number),foreign key(contactid)references phonebook(contactid) on delete cascade)")
cur.execute("create table if not exists emailid(contactid integer,email_type varchar2(20),email varchar2(50),primary key(contactid,email),foreign key(contactid)references phonebook(contactid) on delete cascade)")
root1=Tk()
Label(root1,text="Project Title :PHONEBOOK",font='times 20 bold').grid(row=0,column=0)
Label(root1,text="Project of Python And Database",font='times 20 bold',fg='#123456').grid(row=1,column=1)
Label(root1,text="Developed By:BONTHU AVINASH CHOWDARY(181B072)",font='times 20 bold',fg='#123456').grid(row=2,column=1)
Label(root1,text="---------------------------------------------",fg='#123456').grid(row=3,column=1)
Label(root1,text="Make mouse moment over this screen to close",font='times 15 bold',fg='Red').grid(row=3,column=1)
def close(e=1):
    root1.destroy()
root1.bind('<Motion>',close)
root1.mainloop()
root=Tk()
root.title("Phone Book")
root.configure(background='#A6B7C8')
#root.geometry('700x1250')
Label(root,text="PHONEBOOK",font='times 25 bold',fg='#123456',bg='#F6b334').grid(row=0,column=1)
im=PhotoImage(file="image4.gif")
im=im.subsample(7)
Label(root,image=im).grid(row=1,column=1)
Label(root,text="First Name:",font='times 15 bold').grid(row=3,column=0)
e1=Entry(root)
e1.grid(row=3,column=1)
Label(root,text="Middle Name:",font='times 15 bold').grid(row=4,column=0)
e2=Entry(root)
e2.grid(row=4,column=1)
Label(root,text="Last Name:",font='times 15 bold').grid(row=5,column=0)
e3=Entry(root)
e3.grid(row=5,column=1)
Label(root,text="Company Name:",font='times 15 bold').grid(row=6,column=0)
e4=Entry(root)
e4.grid(row=6,column=1)
Label(root,text="Address:",font='times 15 bold').grid(row=7,column=0)
e5=Entry(root)
e5.grid(row=7,column=1)
Label(root,text="City:",font='times 15 bold').grid(row=8,column=0)
e6=Entry(root)
e6.grid(row=8,column=1)
Label(root,text="Pin Code:",font='times 15 bold').grid(row=9,column=0)
e7=Entry(root)
e7.grid(row=9,column=1)
Label(root,text="Website URL:",font='times 15 bold').grid(row=10,column=0)
e8=Entry(root)
e8.grid(row=10,column=1)
Label(root,text="Date Of Birth:",font='times 15 bold').grid(row=11,column=0)
e9=Entry(root)
e9.grid(row=11,column=1)
Label(root,text="Select Phone Type:",font='times 15 bold').grid(row=12,column=0)
v1=IntVar()
Radiobutton(root,text="Office",variable=v1,value=1).grid(row=12,column=1)
Radiobutton(root,text="Home",variable=v1,value=2).grid(row=12,column=2,)
Radiobutton(root,text="Mobile",variable=v1,value=3).grid(row=12,column=3)
Label(root,text="Phone Number:",font='times 15 bold').grid(row=13,column=0)
Button(root,text='+').grid(row=13,column=2,sticky=W)
e10=Entry(root)
e10.grid(row=13,column=1)
Label(root,text="Select Email Type:",font='times 15 bold').grid(row=14,column=0)
Button(root,text='+').grid(row=15,column=2,sticky=W)
v2=IntVar()
Radiobutton(root,text="Office",variable=v2,value=1).grid(row=14,column=1)
Radiobutton(root,text="Personal",variable=v2,value=2).grid(row=14,column=2,sticky=E)
Label(root,text="Email ID:",font='times 15 bold').grid(row=15,column=0)
e11=Entry(root)
e11.grid(row=15,column=1)
def save():
    a=(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get())
    cur.execute("insert into phonebook(fname,mname,lname,company,address,city,pin,website,dob) values(?,?,?,?,?,?,?,?,?)",a)
    cur.execute("select contactid curval from phonebook")
    curr=cur.fetchall()
    current=len(curr)-1
    if v1.get()==1:
        msg="Office"
    elif v1.get()==2:
        msg='Home'
    elif v1.get()==3:
        msg="Mobile"
    else:
        msg=None
    b=(curr[current][0],msg,e10.get())
    cur.execute("insert into phonenumber values(?,?,?)",b)
    if v2.get()==1:
        msg2="Office"
    elif v2.get()==2:
        msg2="Personal"
    else:
        msg2=None
    c=(curr[current][0],msg2,e11.get())
    cur.execute("insert into emailid values(?,?,?)",c)
##    cur.execute("select * from phonebook")
##    print cur.fetchall()
##    cur.execute("select * from phonenumber")
    con.commit()
##    print cur.fetchall()
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)
    e8.delete(0,END)
    e9.delete(0,END)
    e10.delete(0,END)
    e11.delete(0,END)
    showinfo('Save',"Record saved successfully")
Button(root,text="Save",command=save).grid(row=16,column=0)
def search():
    root3=Tk()
    root3.title("Search")
    root3.geometry('550x700')
    Label(root3,text="Searching phone book",font='times 20 bold',fg='#453672').grid(sticky=W+E+N+S)
    Label(root3,text="Enter Name:",font='times 15 bold').grid(row=1,column=0,sticky=W)
    En=Entry(root3)
    En.grid(row=1,column=0,columnspan=2)
    lb2=Listbox(root3,height='35',width='90',selectmode=SINGLE)
    lb2.grid()
    p=cur.execute("select contactid,fname,mname,lname from phonebook")
    p=cur.fetchall()
    global impp
    impp=p
    def showvalue(e=1):
            line=En.get()
            #uni=unicode(line)
            #uni=('%'+line+'%',)
            lb2.delete(0,END)
            #print uni,type(En.get())
            cur.execute("select contactid,fname,mname,lname from phonebook where (fname like (?) or mname like(?) or lname like(?))",('%'+line+'%','%'+line+'%','%'+line+'%'))
            listbox=cur.fetchall()
            global impp
            impp=listbox
            k1=0
            for v in listbox:
                lb2.insert(k1,v[1]+" "+v[2]+" "+v[3])
                k1+=1
            #print cur.fetchall()
    
    def getvalue(e=1):
        
##        if(type(lb2.get(ACTIVE))==tuple):
##            q=(lb2.get(ACTIVE))
##            cur.execute("select contactid from phonebook where fname=?",(q[0],))
##            contact_id=cur.fetchall()
##        elif(type(lb2.get(ACTIVE))==unicode):
##            q=(lb2.get(ACTIVE))
##            q=q.split()
##            u=unicode(q[0])
##            uni=(u,)
##            cur.execute("select contactid from phonebook where fname=?",uni)
##            contact_id=cur.fetchall()
        tem=lb2.curselection()
        print impp
        print tem
        contact_id=impp[tem[0]][0]
        print contact_id,'hello'  
        cur.execute("select fname,mname,lname,company,address,city,pin,website,dob from phonebook where contactid=?",(contact_id,))
        value1=cur.fetchall()
        print value1
        cur.execute("select contact_type,phone_number from phonenumber where contactid=?",(contact_id,))
        value2=cur.fetchall()
        print value2
        cur.execute("select email_type,email from emailid where contactid=?",(contact_id,))
        value3=cur.fetchall()
        print value3
        root2=Tk()
        root2.title("Search")
        root2.geometry('550x700')
        Label(root2,text="Searching phone book",font='times 20 bold',fg='#453672').grid(sticky=W+E+N+S)
        Label(root2,text="Enter Name:",font='times 15 bold').grid(row=1,column=0,sticky=W)
        En=Entry(root2)
        En.grid(row=1,column=0,columnspan=2)
        lb3=Listbox(root2,height='35',width='90',selectmode=SINGLE)
        lb3.grid()
        
        
        lb3.insert(0,"First name    :"+str(value1[0][0]))
        lb3.insert(1,"Middle name    :"+str(value1[0][1]))
        lb3.insert(2,"Last name    :"+str(value1[0][2]))
        lb3.insert(3,"Company    :"+str(value1[0][3]))
        lb3.insert(4,"Address    :"+str(value1[0][4]))
        lb3.insert(5,"City    :"+str(value1[0][5]))
        lb3.insert(6,"Pin    :"+str(value1[0][6]))
        lb3.insert(7,"Website    :"+str(value1[0][7]))
        lb3.insert(8,"Date Of Birth    :"+str(value1[0][8]))
        lb3.insert(9,"Phone Details.......    :")
        lb3.insert(10,str(value2[0][0])+"    :"+str(value2[0][1]))
        
        lb3.insert(11,"Email Addresses.....  :")
        lb3.insert(12,str(value3[0][0])+'    :'+str(value3[0][1]))
        
        def close3():
            root2.destroy()
        Button(root2,text="Close",command=close3).grid(row=3,column=0)
        def delete():
            cur.execute("delete from phonebook where contactid=?",(contact_id,))
            con.commit()
            showinfo('Delete',"Record Successfully Deleted")
            showvalue()
            root2.destroy()
        Button(root2,text="Delete",command=delete).grid(row=3,column=0,sticky=E)
        root2.mainloop()
    lb2.bind("<Double-Button-1>",getvalue)
    lb2.yview()
    
    ind=0
    k=0
    for i in p:
        lb2.insert(ind,str(p[k][1])+" "+str(p[k][2])+" "+str(p[k][3]))
        ind+=1
        k+=1
    def close5():
        root3.destroy()
    Button(root3,text="Close",command=close5).grid(row=3,column=0)
    En.bind('<KeyRelease>',showvalue)
    root3.mainloop()
Button(root,text="Search",command=search).grid(row=16,column=1)
def edit():
    print 'Hello'
Button(root,text="Edit",command=edit).grid(row=16,column=2)
def closemain(e=1):
    root.destroy()
Button(root,text='Close',command=closemain).grid(row=16,column=3)
root.mainloop()


from tkinter import *
import mysql.connector
import time
import tkinter.font as tkfont


root=Tk()
root.title("CRUD Operation Project")
root.configure(bg="#FFD8FA")


ename=Entry(root,width=30)
ename.grid(row=1,column=1,padx=20,pady=5)
elast=Entry(root,width=30)
elast.grid(row=2,column=1,padx=20,pady=5)
eadd=Entry(root,width=30)
eadd.grid(row=3,column=1,padx=20,pady=5)
ecity=Entry(root,width=30)
ecity.grid(row=4,column=1,padx=20,pady=5)
estate=Entry(root,width=30)
estate.grid(row=5,column=1,padx=20,pady=5)
ezipcode=Entry(root,width=30)
ezipcode.grid(row=6,column=1,padx=20,pady=5)

edelete=Entry(root,width=30)
edelete.grid(row=9,column=1,padx=20,pady=5)
global eedit
eedit=Entry(root,width=30)
eedit.grid(row=10,column=1,padx=20,pady=5)

heading="CRUD OPERATION"+"\n"+"By Arivoli Sankar"

fontstyle=tkfont.Font(family="Times New Roman",size=23,weight="bold")
head=Label(root,text=heading,height=3,fg="#FFD8FA",bg="#740365",width=25,font=fontstyle)
head.grid(row=0,columnspan=2)


f=Label(root,text="First Name: ")
f.grid(row=1,column=0,padx=20,pady=5)
l=Label(root,text="Last Name: ")
l.grid(row=2,column=0,padx=20,pady=5)
a=Label(root,text="Address: ")
a.grid(row=3,column=0,padx=20,pady=5)
c=Label(root,text="City: ")
c.grid(row=4,column=0,padx=20,pady=5)
s=Label(root,text="State: ")
s.grid(row=5,column=0,padx=20,pady=5)
z=Label(root,text="Zipcode: ")
z.grid(row=6,column=0,padx=20,pady=5)


def submit():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        db="tkinter"
    )
    name=ename.get()
    last=elast.get()
    address=eadd.get()
    city=ecity.get()
    state=estate.get()
    zipcode=int(ezipcode.get())
   
    mycursor=mydb.cursor()

    sql="""INSERT INTO inside (name,last,address,city,state,zipcode) VALUES (%s,%s,%s,%s,%s,%s)"""
    insert=(name,last,address,city,state,zipcode)
    mycursor.execute(sql,insert)

    mydb.commit()
    mydb.close()

    info=Label(root,text="Records added sucessfully!!!",fg="black",font="bold")
    info.grid(row=12,columnspan=2)


    ename.delete(0,END)
    elast.delete(0,END)
    eadd.delete(0,END)
    ecity.delete(0,END)
    estate.delete(0,END)
    ezipcode.delete(0,END)

def query():
    head2=Label(root,text="Database Records",height=3,fg="#FFD8FA",bg="#740365",width=25,font=fontstyle)
    head2.grid(row=0,column=3,columnspan=6)
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        db="tkinter"
    )
   
    mycursor=mydb.cursor()

    sql="""select id,name,last,address,city,state,zipcode from inside"""
    mycursor.execute(sql)
    results=mycursor.fetchall()

    records=""
    for result in results:
        records+=str(result[0])+"     "+str(result[1]+"      "+ str(result[2])+"    "+ str(result[3])+"   "+ str(result[4])+"  "+ str(result[5])+"  "+ str(result[6])+"\n")
            
    showinfo=Label(root,text=records,bg="#FFD8FA",fg="black",width=65)
    showinfo.grid(row=1,column=3)
            
    #showinfo=Label(root,text=records,bg="#FFD8FA",fg="black",width=65)
    #showinfo.grid(row=1,column=3,columnspan=6)


def delete():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        db="tkinter"
    )
    did=str(edelete.get())
   
    mycursor=mydb.cursor()
    sql="DELETE FROM inside where id="+ did
    mycursor.execute(sql)

    mydb.commit()
    mydb.close()
    query()

    info=Label(root,text="Record Deleted sucessfully!!!",fg="red")
    info.grid(row=12,columnspan=2)


def update():
    root=Tk()
    root.title("CRUD Operation Project")
    root.configure(bg="#FFD8FA")
    
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    db="tkinter"
    )
   
    mycursor=mydb.cursor()
    iddata=eedit.get()
    sql="select * from inside where id="+iddata
    mycursor.execute(sql,iddata)
    results=mycursor.fetchall()
    
        
        
    
    ename=Entry(root,width=30)
    ename.grid(row=1,column=1,padx=20,pady=5)
    elast=Entry(root,width=30)
    elast.grid(row=2,column=1,padx=20,pady=5)
    eadd=Entry(root,width=30)
    eadd.grid(row=3,column=1,padx=20,pady=5)
    ecity=Entry(root,width=30)
    ecity.grid(row=4,column=1,padx=20,pady=5)
    estate=Entry(root,width=30)
    estate.grid(row=5,column=1,padx=20,pady=5)
    ezipcode=Entry(root,width=30)
    ezipcode.grid(row=6,column=1,padx=20,pady=5)

    heading="Update Information"
    head=Label(root,text=heading,height=3,fg="#FFD8FA",bg="#740365",width=65)
    head.grid(row=0,columnspan=2)



    f=Label(root,text="First Name: ")
    f.grid(row=1,column=0,padx=20,pady=5)
    l=Label(root,text="Last Name: ")
    l.grid(row=2,column=0,padx=20,pady=5)
    a=Label(root,text="Address: ")
    a.grid(row=3,column=0,padx=20,pady=5)
    c=Label(root,text="City: ")
    c.grid(row=4,column=0,padx=20,pady=5)
    s=Label(root,text="State: ")
    s.grid(row=5,column=0,padx=20,pady=5)
    z=Label(root,text="Zipcode: ")
    z.grid(row=6,column=0,padx=20,pady=5)
    for result in results:
        ename.insert(0,result[1])
        elast.insert(0,result[2])
        eadd.insert(0,result[3])
        ecity.insert(0,result[4])
        estate.insert(0,result[5])
        ezipcode.insert(0,result[6])

    def select():
        mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        db="tkinter"
        )
    
        mycursor=mydb.cursor()
        sql="UPDATE inside SET name=%s,last=%s,address=%s,city=%s,state=%s,zipcode=%s where id=%s"
        insert=(ename.get(),elast.get(),eadd.get(),ecity.get(),estate.get(),int(ezipcode.get()),int(eedit.get()))
        mycursor.execute(sql,insert)
        mydb.commit()
        mydb.close()
        query()
        showinfo=Label(root,text="Record Updated Successfully",fg="black")
        showinfo.grid(row=8,column=0,columnspan=2)

        
    btn=Button(root,text="Update Detail",command=select,width=30,fg="white",bg="#740365")
    btn.grid(row=7,columnspan=2,padx=10,pady=10,ipadx=100)

    root.mainloop()


btn=Button(root,text="Add Data to Database",command=submit,width=30,fg="white",bg="#740365")
btn.grid(row=7,columnspan=2,padx=10,pady=10,ipadx=100)

showbtn=Button(root,text="Show All Records",command=query,width=30,bg="#BB0AA4",fg="white")
showbtn.grid(row=8,columnspan=2,padx=10,pady=10,ipadx=100)

deletebtn=Button(root,text="Delete record By Id",command=delete,width=30,fg="white",bg="red")
deletebtn.grid(row=9,column=0,padx=10,pady=10)

editbtn=Button(root,text="Edit Data",command=update,width=30,fg="white",bg="blue")
editbtn.grid(row=10,column=0,padx=10,pady=10)

exitb=Button(root,text="Exit",command=root.quit,width=30,fg="white",bg="gray")
exitb.grid(row=11,columnspan=2,padx=10,pady=10,ipadx=100)








root.mainloop()
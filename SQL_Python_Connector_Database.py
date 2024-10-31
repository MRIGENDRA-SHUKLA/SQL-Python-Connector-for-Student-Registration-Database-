import mysql.connector as mysql

con=mysql.connect(host='localhost', user='root', password='Mrigendr@1234567',database='python_3_4PM')

cur=con.cursor()

from tkinter import*
from tkinter import messagebox

root=Tk()
root.geometry("200x200")


Label(root,text="Student id:").grid(row=0,column=0)
e1=Entry(root)
e1.grid(row=0,column=1)

Label(root,text="Amount:").grid(row=1,column=0)
e2=Entry(root)
e2.grid(row=1,column=1)

def submit():
    try:
       cur.execute( f" insert into billing(student_id,paid_fee) values({e1.get()},{e2.get()}) " )
       con.commit()
       messagebox.showinfo("Success","Data Inserted")
    except:
       messagebox.showinfo("Failed","Operation Failed")
         

Button(root,text="Submit",command=submit).grid(row=2,column=0)


root.mainloop()

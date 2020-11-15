from tkinter import *
import sqlite3

root=Tk()



'''
c.execute("""
CREATE TABLE address (
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer

)""")

'''
f_name=Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20)

l_name=Entry(root,width=30)
l_name.grid(row=1,column=1)

address=Entry(root,width=30)
address.grid(row=2,column=1)

city=Entry(root,width=30)
city.grid(row=3,column=1)


state=Entry(root,width=30)
state.grid(row=4,column=1)



zipcode=Entry(root,width=30)
zipcode.grid(row=5,column=1)

f_name_label=Label(root,text="first name")
f_name_label.grid(row=0,column=0)

l_name_label=Label(root,text="last name")
l_name_label.grid(row=1,column=0)

address_label=Label(root,text="address")
address_label.grid(row=2,column=0)

city_label=Label(root,text="city")
city_label.grid(row=3,column=0)

state_label=Label(root,text="state")
state_label.grid(row=4,column=0)

zipcode_label=Label(root,text="zipcode")
zipcode_label.grid(row=5,column=0)


conn=sqlite3.connect('address_book.db')
c=conn.cursor()
def submit():
    

    c.execute("insert into address values (:fname,:l_name,:address,:city,:state,:zipcode) ",
    {
        "f_name":f_name.get(),
        "l_name":l_name.get(),
        "address":address.get(),
        "city":city.get(),
        "state":state.get(),
        "zipcode":zipcode.get()

    }
    )

    



    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)






submit_btn=Button(root,text="Add Record",command=submit)
submit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)


query_btn=Button(root,text='show record',command=query)

conn.commit()
conn.close()

root.mainloop()
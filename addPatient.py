from tkinter import *
from tkinter import ttk, messagebox
import  mysql.connector
 #establishing connection
conn = mysql.connector.connect(user='root', password='', host='localhost', database='hospitalmanagement')




root= Tk()
# app title
root.title("Add Patient")
# window size
width  = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry(f'{width}x{height}')
root.configure(bg='#ffc0b4')

def home():
	root.destroy()
	import home

def doctor():
	root.destroy()
	import addDoctor

def patient():
	root.destroy()
	import patient

def appointment():
	root.destroy()
	import addAppointment

def logout():
        messagebox.askquestion("logout", "Do you really want to logout?")
        root.destroy()

def clear():
        f_nameentry.delete(0,END)
        l_nameentry.delete(0,END)
        gender.set('')
        addressentry.delete(0,END)
        diseaseentry.delete(0,END)
        a_dateentry.delete(0,END)
        
        
    
        
       
         

def register():
    #getting form data

    fname1=f_nameentry.get()
    lname1=l_nameentry.get()
    gender1=n.get()
    address1=addressentry.get()
    disease1=diseaseentry.get()
    a_date1=a_dateentry.get()
    
    
    #applying empty validation
    if fname1=='' or lname1=='' or gender1==''or address1=='' or disease1=='' or a_date1=='' :
        messagebox.showerror(title=None, message="Fill the empty fields", )
    else:
      
       # Creating a cursor object using the cursor() method
       cursor = conn.cursor()
       # Preparing SQL query to INSERT a record into the database.
       insert_stmt = (
           "INSERT INTO patient(p_first_name,p_last_name,p_gender,p_add,p_disease,a_date)"
           "VALUES (%s, %s,%s, %s, %s,%s)"
       )
       value=(fname1,lname1,gender1,address1,disease1,a_date1)
       
       try:
           #executing the sql command
           cursor.execute(insert_stmt,value)
           #commit changes in database
           conn.commit()
           clear()
       except:
           conn.rollback()
       messagebox.showinfo(title="Patient Confirmation", message="Patient Added Successfully")
       #conn.close()
       f_nameentry.delete(0,END)
       l_nameentry.delete(0,END)
       gender.set('')
       addressentry.delete(0,END)
       diseaseentry.delete(0,END)
       a_date1=a_dateentry.get()
       
    

    

#heading

heading = Label(root, text = "        Add Patient        " , font = 'Verdana 25 bold',bg="orange")
heading.place(x=400 , y=130)


frame = Frame(root, borderwidth=6, bg="lightgrey", relief=SUNKEN)
frame.pack(side=TOP, anchor="nw",fill="x",padx=20,pady=20)

b1 = Button(frame, fg="red", bg="honeydew",text="Home", command=home)
b1.pack(side=LEFT, padx=90,pady=5)

b2 = Button(frame, fg="red", text="Doctor", command=doctor, bg="honeydew")
b2.pack(side=LEFT, padx=90,pady=5)

b3 = Button(frame, fg="red", text="Patient", bg="honeydew",command=patient)
b3.pack(side=LEFT, padx=90,pady=5)

b4 = Button(frame, fg="red", text="Appointment", bg="honeydew",command=appointment )
b4.pack(side=LEFT, padx=90,pady=5)

b5 = Button(frame, fg="red", text="Logout", bg="honeydew",command=logout )
b5.pack(side=LEFT, padx=90,pady=5)

#field name
f_name= Label(root, text="Patient's First Name",font = 'Verdana 15 bold',bg="lightblue",width=18)
l_name= Label(root, text="Patient's last Name" ,font = 'Verdana 15 bold',bg="lightblue",width=18)
gender= Label(root, text="Gender",font = 'Verdana 15 bold',bg="lightblue",width=18)
address= Label(root, text="Address",font = 'Verdana 15 bold',bg="lightblue",width=18)
disease= Label(root, text="Disease",font = 'Verdana 15 bold',bg="lightblue",width=18)
a_date= Label(root, text="Admit Date",font = 'Verdana 15 bold',bg="lightblue",width=18)


#packing field
f_name.place(x=330,y=230)
l_name.place(x=330,y=290)
gender.place(x=330,y=350)
address.place(x=330,y=410)
disease.place(x=330,y=470)
a_date.place(x=330,y=530)


#variable to store values
f_namevalue=StringVar
l_namevalue=StringVar
addressvalue=StringVar
diseasevalue=StringVar
a_date=IntVar


#Creating entry field
f_nameentry=Entry(root,font = 'Verdana 15 ' )
l_nameentry=Entry(root,font = 'Verdana 15 ' )

addressentry=Entry(root,font = 'Verdana 15 ')
diseaseentry=Entry(root,font = 'Verdana 15 ')
a_dateentry=Entry(root,font = 'Verdana 15 ')


#packing entry field
f_nameentry.place(x=620,y=230)
l_nameentry.place(x=620,y=290)
addressentry.place(x=620,y=410)
diseaseentry.place(x=620,y=470)
a_dateentry.place(x=620,y=530)


#Submit Button
Button(root,text="Submit",command=register,font = 'Verdana 15 bold',fg="white",bg="blue",borderwidth=4,relief="sunken").place(x=450,y=650)
btn_login = Button(root, text = "Clear " ,font='Verdana 15 bold', command = clear,fg="white",bg="red",borderwidth=4,relief="sunken")
btn_login.place(x=630, y=650)

n = StringVar()
fontExample = ("Verdana", 18) 
gender = ttk.Combobox(root, width = 16, textvariable = n,font=fontExample)
root.option_add('*TCombobox*Listbox.font', fontExample)
gender.place(x=620,y=350) 
# Adding combobox drop down list
gender['values'] = ('Male','Female','Others')
  
#monthchoosen.grid(column = 1, row = 5)
gender.current()










root.mainloop()

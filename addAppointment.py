from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import Calendar
import  mysql.connector
 #establishing connection
conn = mysql.connector.connect(user='root', password='', host='localhost', database='hospitalmanagement')
root= Tk()

cursor = conn.cursor()

# app title
root.title("Add Appointment")

# window size
width  = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry(f'{width}x{height}')
root.configure(bg='#ffe5b4') #ws['bg']='#ffbf00'

def home():
	root.destroy()
	import home

def doctor():
	root.destroy()
	import addDoctor

def patient():
	root.destroy()
	import addPatient

def appointment():
	root.destroy()
	import appointment

def clear():
        combo1.set('')
        combo2.set('')
        diseaseentry.delete(0,END)
        dateentry.delete(0,END)
        
def logout():
        messagebox.askquestion("logout", "Do you really want to logout?")
        root.destroy()



    
def register():
    #getting form data
    name1=combo1.get()
    doctor1=combo2.get()
    disease1=diseaseentry.get()
    date1=dateentry.get()
    
    #applying empty validation
    if name1=='' or doctor1==''or disease1=='' or date1=='':
        messagebox.showerror(title=None, message="Fill the empty fields", )
    else:
      
       # Creating a cursor object using the cursor() method
       cursor = conn.cursor()
       # Preparing SQL query to INSERT a record into the database.
       insert_stmt = (
           "INSERT INTO appointment(a_p_name,doc_name,a_p_disease,a_date)"
           "VALUES (%s, %s, %s, %s)"
       )
       value=(name1,doctor1,disease1,date1)
       
       try:
           #executing the sql command
           cursor.execute(insert_stmt,value)
           #commit changes in database
           conn.commit()
       except:
           conn.rollback()
           
       messagebox.showinfo(title="Appointment Confirmation", message="Appointment Added Successfully")
       clear()
       
    

    

#heading
heading = Label(root, text = "        Add Appointment        " , font = 'Verdana 25 bold',bg="orange")
heading.place(x=400 , y=130)


frame = Frame(root, borderwidth=6, bg="#989898", relief=SUNKEN)
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
name= Label(root, text="Patient's Name:  " ,font = 'Verdana 15 bold',bg="lightblue")
doctor= Label(root, text="Doctor's Name:  ",font = 'Verdana 15 bold',bg="lightblue")
disease= Label(root, text="Disease:             ",font = 'Verdana 15 bold',bg="lightblue")
date= Label(root, text="Appointment Date:",font = 'Verdana 15 bold',bg="lightblue")

#packing field
name.place(x=400,y=230)
doctor.place(x=400,y=290)
disease.place(x=400,y=350)
date.place(x=400,y=410)

#variable to store values
diseasevalue=StringVar
datevalue=StringVar

#Creating entry field
diseaseentry=Entry(root,font = 'Verdana 15 ')
dateentry=Entry(root,font = 'Verdana 15 ')
dateentry.insert(0, 'YYYY-MM-DD ')


#packing entry field
diseaseentry.place(x=650,y=350)
dateentry.place(x=650,y=410)

#Submit Button
Button(root,text="Submit",command=register,font = 'Verdana 15 bold',fg="white",bg="blue",borderwidth=4,relief="sunken").place(x=450,y=515)
btn_login = Button(root, text = "Clear " ,font='Verdana 15 bold', command = clear,fg="white",bg="red",borderwidth=4,relief="sunken")
btn_login.place(x=630, y=515)

cursor.execute ("SELECT p_first_name,p_last_name FROM patient")
rows1= cursor.fetchall ()
fontExample = ("Verdana", 15)
bg=("red")
combo1= ttk.Combobox (root,width=18,font=fontExample,textvariable=patient)
combo1.place(x=650,y=230)
root.option_add('*TCombobox*Listbox.font', fontExample)
root.option_add('*TCombobox*Listbox.bg', bg)

def add_value (v):
    combo1 ['values']= tuple (list (combo1 ['values']) + rows1)
add_value (rows1 [0])


cursor.execute ("SELECT d_first_name,d_last_name FROM doctor")
row2= cursor.fetchall ()
fontExample = ("Verdana", 15)
bg=("red")
combo2= ttk.Combobox (root,width=18,font=fontExample,textvariable=doctor)
combo2.place(x=650,y=290)
root.option_add('*TCombobox*Listbox.font', fontExample)
root.option_add('*TCombobox*Listbox.bg', bg)

def value (v):
    combo2 ['values']= tuple (list (combo2 ['values']) + row2)
value (row2 [0])


root.mainloop()



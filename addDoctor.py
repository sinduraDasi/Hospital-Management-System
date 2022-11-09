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
	import doctor

def patient():
	root.destroy()
	import addPatient

def appointment():
	root.destroy()
	import addAppointment


def clear():
        f_nameentry.delete(0,END)
        l_nameentry.delete(0,END)
        gender.set('')
        addressentry.delete(0,END)
        diseaseentry.delete(0,END)
        expentry.delete(0,END)
        
def logout():
        messagebox.askquestion("logout", "Do you really want to logout?")
        root.destroy()
    
        
       
         

def register():
    #getting form data

    fname1=f_nameentry.get()
    lname1=l_nameentry.get()
    gender1=n.get()
    address1=addressentry.get()
    disease1=diseaseentry.get()
    exp1=expentry.get()
    
    #applying empty validation
    if fname1=='' or lname1=='' or gender1==''or address1=='' or disease1=='' or exp1=="":
        messagebox.showerror(title=None, message="Fill the empty fields", )
    else:
      
       # Creating a cursor object using the cursor() method
       cursor = conn.cursor()
       # Preparing SQL query to INSERT a record into the database.
       insert_stmt = (
           "INSERT INTO doctor(d_first_name,d_last_name,d_gender,d_add,d_specialization,d_experieence)"
           "VALUES (%s, %s,%s, %s, %s,%s)"
       )
       value=(fname1,lname1,gender1,address1,disease1,exp1)
       
       try:
           #executing the sql command
           cursor.execute(insert_stmt,value)
           #commit changes in database
           conn.commit()
           clear()
       except:
           conn.rollback()
       messagebox.showinfo(title="Doctor Confirmation", message="Doctor Added Successfully")
       #conn.close()
       f_nameentry.delete(0,END)
       l_nameentry.delete(0,END)
       gender.set('')
       addressentry.delete(0,END)
       diseaseentry.delete(0,END)
       expentry.delete(0,END)
    

    

#heading
# Label(root, text="Add Patient", font="Verdana 30 bold" ,bg="orange").grid(row=0,column=3)
heading = Label(root, text = "        Add Doctor        " , font = 'Verdana 25 bold',bg="orange")
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
f_name= Label(root, text="Doctor's First Name: ",font = 'Verdana 15 bold',bg="lightblue")
l_name= Label(root, text="Doctor's last Name: " ,font = 'Verdana 15 bold',bg="lightblue")
gender= Label(root, text="        Gender:             ",font = 'Verdana 15 bold',bg="lightblue")
address= Label(root, text="       Address:            ",font = 'Verdana 15 bold',bg="lightblue")
disease= Label(root, text="     Specialization:    ",font = 'Verdana 15 bold',bg="lightblue")
exp= Label(root, text=" Experience(in years):",font = 'Verdana 15 bold',bg="lightblue")

#packing field
f_name.place(x=330,y=230)
l_name.place(x=330,y=290)
gender.place(x=330,y=350)
address.place(x=330,y=410)
disease.place(x=330,y=470)
exp.place(x=330,y=530)

#variable to store values
f_namevalue=StringVar
l_namevalue=StringVar
addressvalue=StringVar
diseasevalue=StringVar
expvalue=IntVar

#Creating entry field
f_nameentry=Entry(root,font = 'Verdana 15 ' )
l_nameentry=Entry(root,font = 'Verdana 15 ' )
addressentry=Entry(root,font = 'Verdana 15 ')
diseaseentry=Entry(root,font = 'Verdana 15 ')
expentry=Entry(root,font = 'Verdana 15 ')

#packing entry field
f_nameentry.place(x=620,y=230)
l_nameentry.place(x=620,y=290)
addressentry.place(x=620,y=410)
diseaseentry.place(x=620,y=470)
expentry.place(x=620,y=530)

#Submit Button
Button(root,text="Submit",command=register,font = 'Verdana 15 bold',fg="white",bg="blue",borderwidth=4,relief="sunken").place(x=450,y=635)
btn_login = Button(root, text = "Clear " ,font='Verdana 15 bold', command = clear,fg="white",bg="red",borderwidth=4,relief="sunken")
btn_login.place(x=630, y=635)

n = StringVar()
fontExample = ("Verdana", 18) 
gender = ttk.Combobox(root, width = 16, textvariable = n,font=fontExample)
root.option_add('*TCombobox*Listbox.font', fontExample)
gender.place(x=620,y=350) 
# Adding combobox drop down list
gender['values'] = ('Male','Female','Others')
gender.current()










root.mainloop()

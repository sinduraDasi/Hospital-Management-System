import mysql.connector
import tkinter  as tk 
from tkinter import * 
from tkinter import messagebox as msg
my_w = tk.Tk()

width  = my_w.winfo_screenwidth()
height = my_w.winfo_screenheight()
my_w.geometry(f'{width}x{height}')
my_w.configure(bg='#ffeece')

my_connect = mysql.connector.connect(
  host="localhost",
  user="root", 
  passwd="",
  database="hospitalmanagement"
)
my_conn = my_connect.cursor()

def home():
	my_w.destroy()
	import home

def doctor():
	my_w.destroy()
	import addDoctor

def patient():
	my_w.destroy()
	import addPatient

def appointment():
	my_w.destroy()
	import addAppointment
	
def addAppointment():
        my_w.destroy()
        import addAppointment
        
def login():
        my_w.destroy()
        import appointment

def logout():
        msg.askquestion("logout", "Do you really want to logout?")
        my_w.destroy()

    
frame = Frame(my_w, borderwidth=6, bg="lightgrey", relief=SUNKEN)
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

f1=Frame(my_w,bg='lightgrey')
f1.pack(pady=150,padx=25)
heading = Label(my_w, text = "        Appointments        " , font = 'Verdana 25 bold',bg="orange")
heading.place(x=420 , y=130)
e=Entry(f1,width=10,text='ID',borderwidth=0,bg='lightgrey', font = 'Verdana 15 bold' )
e.insert(0,"ID")
e.grid(row=0,column=0,pady=20,padx=5)
e=Entry(f1,width=15,text='Name',borderwidth=0,bg='lightgrey', font = 'Verdana 15 bold'  )
e.insert(0,"Patient's Name")
e.grid(row=0,column=1,padx=10,pady=20)
e=Entry(f1,width=15,text='Class',borderwidth=0 ,bg='lightgrey', font = 'Verdana 15 bold' )
e.insert(0,"Doctor's Name")
e.grid(row=0,column=2,padx=10,pady=20)
e=Entry(f1,width=15,text='mark',borderwidth=0 ,bg='lightgrey', font = 'Verdana 15 bold'  )
e.insert(0,"Patient's Disease")
e.grid(row=0,column=3,padx=10,pady=20)
e=Entry(f1,width=17,text='Gender',borderwidth=0  ,bg='lightgrey', font = 'Verdana 15 bold' )
e.insert(0,"Appointment Date")
e.grid(row=0,column=4,padx=10,pady=20)


#Button(my_w,text="Add Appointment",command=addAppointment ,font = 'Verdana 15 bold',fg="black",bg="#ffc0b4",borderwidth=2,relief="sunken") \
#.place(x=930,y=210)

def my_show():
    my_conn.execute("SELECT * FROM `appointment`");
    i=1
    
    
        
        
    for appointment in my_conn: 
        for j in range(len(appointment)):
            e = Entry(f1, width=12, fg='blue',borderwidth=0,bg='lightgrey',font = 'Verdana 15' )
            e.grid(row=i, column=j,pady=15)#
            e.insert(END, appointment[j])
            #
        e = Button(f1, text='Delete',font = 'Verdana 15',bg="lightgreen",command= lambda d=appointment[0] : my_delete(d)) 
        e.grid(row=i, column=j+1,padx=10)
        i=i+1
    #return appointment
def my_delete(id):
    global my_conn
    my_var=msg.askyesnocancel("Delete ?","Delete appointment of id "+str(id),icon='warning',default='no')
    if my_var: # True if yes button is clicked
        my_conn.execute("DELETE FROM appointment where id=" + str(id) );
        
        my_connect.commit()
        login()
        
my_show()  # open the window with record at the starting      
    
my_w.mainloop()


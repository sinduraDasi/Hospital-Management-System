from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import Error

root1 = Tk()
root1.title("Patient  Tab")

canvas_width = 1200
canvas_height = 500
screen = Canvas(root1, width=canvas_width, height=canvas_height)
screen.grid(column=0, row=0, columnspan=15, rowspan=15)
screen.create_rectangle(10, 10, 1150, 490, fill="#707070")
screen.create_rectangle(20,20, 1135, 60, fill="#404040")
screen.create_rectangle(20, 70, 1135, 150, fill="#404040")
screen.create_rectangle(20, 130, 1135, 480, fill="#999999")

def home():
	root1.destroy()
	import home

def doctor():
	root1.destroy()
	import addDoctor

def patient():
	root1.destroy()
	import addPatient

def appointment():
	root1.destroy()
	import addAppointment

def addPatient():
    root1.destroy()
    import addPatient

def logout():
        messagebox.askquestion("logout", "Do you really want to logout?")
        root1.destroy()


hospitalName = Label(root1, text="Sunrise Hospital", bg="#404040", fg="#FFFFFF",font="Verdana 15 bold")
home = Button(root1, text="Home", width="10",command=home)
patient = Button(root1, text="Patient", width="10",command=patient)
doctor = Button(root1, text="Doctor", width="10",command=doctor)
appointment = Button(root1, text="Appointment", width="10",command=appointment)
add_patient = Button(root1, text="Logout", width="10",command=logout)
patient_id = Label(root1, text="Patient ID", width="10", bg='#999999')
patient_fname = Label(root1, text="First Name", width="10", bg='#999999')
patient_lname = Label(root1, text="Last Name", width="10", bg='#999999')
patient_gender = Label(root1, text="Gender", width="10", bg='#999999')
patient_add = Label(root1, text="Address", width="10", bg='#999999')
patient_disease = Label(root1, text="Disease", width="10", bg='#999999')
patient_adate = Label(root1, text="Admit Date", width="10", bg='#999999')


hospitalName.grid(row=0, column=0, columnspan=6, pady=17)
home.grid(row=1, column=0, padx=20,pady=1)
patient.grid(row=1, column=1, padx=20)
doctor.grid(row=1, column=2, padx=20)
appointment.grid(row=1, column=3, padx=20)
add_patient.grid(row=1, column=4, padx=20)
patient_id.grid(row=3, column=0)
patient_fname.grid(row=3, column=1)
patient_lname.grid(row=3, column=2)
patient_gender.grid(row=3, column=3)
patient_add.grid(row=3, column=4)
patient_disease.grid(row=3, column=5,padx=20)
patient_adate.grid(row=3, column=6,padx=20)



try:
    connection = mysql.connector.connect(host='localhost',
                                         database='hospitalmanagement',
                                         user='root',
                                         password='')
    sql_select_query = "select * from patient"
    cursor = connection.cursor()
    cursor.execute(sql_select_query)
    records = cursor.fetchall()
    grid_row = 6

    for row in records:
        p_id = Label(root1, text=row[0], width="10")
        p_fname = Label(root1, text=row[1], width="10")
        p_lname = Label(root1, text=row[2], width="10")
        p_gender = Label(root1, text=row[3], width="10")
        p_add = Label(root1, text=row[4], width="10")
        p_disease = Label(root1, text=row[5], width="10")
        p_adate = Label(root1, text=row[6], width="10")
        
        

        p_id.grid(row=grid_row, column=0)
        p_fname.grid(row=grid_row, column=1)
        p_lname.grid(row=grid_row, column=2)
        p_gender.grid(row=grid_row, column=3)
        p_add.grid(row=grid_row, column=4)
        p_disease.grid(row=grid_row, column=5)
        p_adate.grid(row=grid_row, column=6)
        grid_row += 1
        
        
        
except Error as e:
    print("Error while connecting to MySQL", e)

'''finally:
    if connection.is_connected():
        #cursor.close()
        #connection.close()
        #print("MySQL connection is closed")'''

root1.mainloop()


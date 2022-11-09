from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector as pymysql
from PIL import ImageTk, Image
#establishing connection
conn = pymysql.connect(user='root', password='', host='localhost', database='hospitalmanagement')

#------------------------------------------------------Admin Login --------------------------------------------------
def clear():
	userentry.delete(0,END)
	passentry.delete(0,END)

def close():
	root.destroy()
	import Home

def login():
	if user_name.get()=="" or password.get()=="":
		messagebox.showerror("Error","Enter User Name And Password",parent=root)	
	else:
		try:
			con = pymysql.connect(host="localhost",user="root",password="",database="hospitalmanagement")
			cur = con.cursor()

			cur.execute("select * from user where username=%s and password = %s",(user_name.get(),password.get()))
			row = cur.fetchone()

			if row==None:
				messagebox.showerror("Error" , "Invalid User Name And Password", parent = root)

			else:
				messagebox.showinfo("Success" , "Successfully Login" , parent = root)
				close()
				
                                
			con.close()
		except Exception as es:
			messagebox.showerror("Error" , f"Error Dui to : {str(es)}", parent = root)

root = Tk()


# app title
root.title("Docter Appointment App")



# window size
width  = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry(f'{width}x{height}')


label=Label(text="Welcome to Sunrise Hospital",bg="lightgrey",fg="black",font="Helvetica 19 bold",pady=10)
label.pack(fill="x")

label_tag=Label(text="The care you need. The compassion you deserve.",fg="black",font="Verdana 12 bold",pady="10")
label_tag.pack()

# image
image = Image.open(r"d:\Users\Admin\Desktop\Ekta\hospital management\home.PNG")
  
# Reszie the image using resize() method
resize_image = image.resize((width, 400))
  
img = ImageTk.PhotoImage(resize_image)
  
# create label and add resize image
label1 = Label(image=img)
label1.image = img
label1.pack()

#heading label
heading = Label(root , text = "Login" , font = 'Verdana 25 bold')
heading.place(x=550 , y=530)

username = Label(root, text= "User Name :" , font='Verdana 15 bold')
username.place(x=400,y=620)

userpass = Label(root, text= "Password :" , font='Verdana 15 bold')
userpass.place(x=400,y=680)

# Entry Box
user_name = StringVar()
password = StringVar()
	
userentry = Entry(root, width=40 , textvariable = user_name,font='Verdana 15 ')
userentry.focus()
userentry.place(x=550 , y=620)

passentry = Entry(root, width=40, show="*" ,textvariable = password,font='Verdana 15 ')
passentry.place(x=550 , y=680)


# button login and clear

btn_login = Button(root, text = "Login" ,font='Verdana 15',command = login,fg="white",bg="blue",borderwidth=4,relief="sunken")
btn_login.place(x=500, y=760)


btn_login = Button(root, text = "Clear" ,font='Verdana 15', command = clear,fg="white",bg="red",borderwidth=4,relief="sunken")
btn_login.place(x=620, y=760)





root.mainloop()

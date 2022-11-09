from tkinter import *

root = Tk()
root.title("Home_Page")


def h_tab():
    root.destroy()
    import Home


def p_tab():
    root.destroy()
    import addPatient

def d_tab():
    root.destroy()
    import addDoctor

def a_tab():
    root.destroy()
    import addAppointment



canvas_width = 600
canvas_height = 400
screen = Canvas(root, width=canvas_width, height=canvas_height)
screen.grid(column=0, row=0, columnspan=4, rowspan=15)
screen.create_rectangle(10, 10, 590, 390, fill="#707070")
screen.create_rectangle(20, 20, 580, 57, fill="#404040")
screen.create_rectangle(20, 65, 580, 120, fill="#404040")
screen.create_rectangle(20, 130, 415, 380, fill="#999999")
screen.create_rectangle(425, 130, 580, 380, fill="#999999")

#logo = PhotoImage(file="Logo.PNG")
#image = Image.open(r"d:\Users\Admin\Desktop\Ekta\hospital management\Logo.PNG")
#img = ImageTk.PhotoImage(imge)
img = PhotoImage(file=r"d:\Users\Admin\Desktop\Ekta\hospital management\Logo.PNG")   
hospitalName = Label(root, text="Sunrise Hospital", bg="#404040", fg="#FFFFFF", font="Comic_Sans 15")
home = Button(root, text="Home", width="10", command=h_tab)
patient = Button(root, text="Patient", width="10", command=p_tab)
doctor = Button(root, text="Doctor", width="10", command=d_tab)
appointment = Button(root, text="Appointment", width="10", command=a_tab)

info = Label(root, image=img, bg="#999999")
address = Label(root, text="ADDRESS:\n3rd Floor,\n Golden Palace,\n King Street,\n London, UK", bg="#999999", width="5")

hospitalName.grid(row=0, column=0, columnspan=4, pady=15)
home.grid(row=1, column=0, padx=1, sticky="ne")
patient.grid(row=1, column=1, padx=1, sticky="ne")
doctor.grid(row=1, column=2, padx=5, sticky="ne")
appointment.grid(row=1, column=3, padx=5, sticky="n")

info.grid(row=3, column=0, columnspan=3, rowspan=10, padx=10, sticky="ne")
address.grid(row=3, column=3, ipadx=45, padx=10, rowspan=10, sticky="n")

root.mainloop()

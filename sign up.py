from tkinter import *
import tkinter as tk
from tkinter import Entry,Tk
from PIL import Image
from PIL import ImageTk
from tkcalendar import Calendar
import webbrowser
root=Tk()
First_name=tk.StringVar()
last_name=tk.StringVar()
Clicked=tk.StringVar()
cal_name=tk.StringVar()
mob_name=tk.StringVar()
Add_name=tk.StringVar()
City_name=tk.StringVar()
Email_name=tk.StringVar()
Pass_name=tk.StringVar()
Confirm_name=tk.StringVar()
def finalsub():
	newWindow = Toplevel(root)

	# sets the title of the
	# Toplevel widget
	newWindow.title("Confirmation")

	# sets the geometry of toplevel
	newWindow.geometry("300x300")
	
	label7=Label(newWindow,text="Account is Created Successfully!!").place(x=10,y=50)
	name=First_name.get()
	lastname=last_name.get()
	gender=Clicked.get()
	DATE=CAL_NAME.GET()
	mobile=mob_name.get()
	address=Add_name.get()
	city=City_name.get()
	email=Email_name.get()
	
     
	label8=Label(newWindow,text="The name is : " + name).place(x=10,y=70)
	label9=Label(newWindow,text="The lastname is : " + lastname).place(x=10,y=90)
	label9=Label(newWindow,text="The place is : " + date).place(x=10,y=110)
	label9=Label(newWindow,text="The Mobile no is : " + mobile).place(x=10,y=130)
	label9=Label(newWindow,text="The address is : " + address).place(x=10,y=150)
	label9=Label(newWindow,text="The email is : " + email).place(x=10,y=170)
	
 
	First_name.set("")
	last_name.set("")
	Clicked.set("")
	cal_name.set("")
	mob_name.set("")
	Add_name.set("")
	City_name.set("")
	Email_name.set("")
def map_mode():
	webbrowser.open_new_tab("https://www.google.com/maps")
 
 
		
root.geometry("300x580")
root.minsize(300,580)
root.maxsize(300,580)
root.configure(bg='white')
image = Image.open("title.png")
 
# Resize the image using resize() method
resize_image = image.resize((300, 15))
 
img = ImageTk.PhotoImage(resize_image)

label1 = Label(image=img,bg='purple')                      
label1.image =img
label1.place(x=0,y=0)
image = Image.open("screen.png")
 
# Resize the image using resize() method
resize_image = image.resize((300, 50))
 
img = ImageTk.PhotoImage(resize_image)

label1 = Label(image=img,bg='white')
label1.image =img
label1.place(x=0,y=10)
image=Image.open("map3.png")
resize_image =image.resize((20, 20))
img = ImageTk.PhotoImage(resize_image)
button= Button(root, image=img,command= map_mode,borderwidth=0)
button.image=img
button.place(x=260,y=12)
image=Image.open("arrow.png")
resize_image =image.resize((20, 20))
img = ImageTk.PhotoImage(resize_image)
button= Button(root, image=img,borderwidth=0)
button.image=img
button.place(x=5,y=12)
label2=Label(root,text="SIGN UP",bg='white').place(x=130,y=60)
image=Image.open("icon1.png")
resize_image =image.resize((20, 20))
img = ImageTk.PhotoImage(resize_image)
label8 = Label(image=img,bg='orange')
label8.image=img
label8.place(x=5,y=100)
label3=Label(root,text=" First Name",bg="White").place(x=30,y=80)
label4=Label(root,text=" Last Name",bg="white").place(x=180,y=80)
First_name=tk.StringVar()
Firstname=Entry(root,width=15,textvariable=First_name).place(x=30,y=100)
last_name=tk.StringVar()
lastname=Entry(root,width=15,textvariable=last_name).place(x=160,y=100)

image=Image.open("icon6.png")
resize_image =image.resize((20, 20))
img = ImageTk.PhotoImage(resize_image)
label8 = Label(image=img,bg='orange')
label8.image=img
label8.place(x=5,y=130)
# creates a Tk() object
options=[ 
	"Select Gender",
	"Male",
	"Female",
	"Not Applicable"]
clicked=StringVar()
clicked.set("Select Gender")
drop=OptionMenu(root,clicked,*options).place(x=30,y=130)
# function to open a new window
# on a button click
def openNewWindow():
	
	# Toplevel object which will
	# be treated as a new window
	newWindow = Toplevel(root)

	# sets the title of the
	# Toplevel widget
	newWindow.title("Calendar")

	# sets the geometry of toplevel
	newWindow.geometry("200x200")
	
	cal = Calendar(newWindow, selectmode = 'day', year = 2020, month = 5,  day = 22)
 
	cal.pack()
 
	def grad_date():
		label=Label(root,text = cal.get_date(),bg='white').place(x=30,y=190)
 
# Add Button and Label
	Button(newWindow, text = "Get Date",  command = grad_date).place(x=50,y=170)
 
# a button widget which will open a
# new window on button click
image=Image.open("icon2.png")
resize_image =image.resize((20, 20))
img = ImageTk.PhotoImage(resize_image)
label8 = Label(image=img,bg='orange')
label8.image=img
label8.place(x=5,y=190)
label6=Label(root,text="Date of Birth",bg="white").place(x=30,y=170)
cal_name=tk.StringVar()
cal=Entry(root,width=25,textvariable=cal_name).place(x=30,y=190)
photo = PhotoImage(file="cal.png")
photo1 = photo.subsample(6, 6)
  
btn = Button(root,image=photo1,command = openNewWindow,height=15,width=15).place(x=250,y=190)


# mainloop, runs infinitely
image=Image.open("icon3.png")
resize_image =image.resize((20, 20))
img = ImageTk.PhotoImage(resize_image)
label8 = Label(image=img,bg='orange')
label8.image=img
label8.place(x=5,y=240)
label7=Label(root,text="Mobile No",bg="white").place(x=30,y=220)
mob_name=tk.StringVar()
mob=Entry(root,width=25,textvariable=mob_name,text="Enter Mobile No").place(x=30,y=240)
image=Image.open("icon4.png")
resize_image =image.resize((20, 20))
img = ImageTk.PhotoImage(resize_image)
label8 = Label(image=img,bg='orange')
label8.image=img
label8.place(x=5,y=290)
label6=Label(root,text="Address",bg="white").place(x=30,y=270)
Add_name=tk.StringVar()
Address=Entry(root,width=25,textvariable=Add_name).place(x=30,y=290)
image=Image.open("icon5.png")
resize_image =image.resize((20, 20))
img = ImageTk.PhotoImage(resize_image)
label8 = Label(image=img,bg='orange')
label8.image=img
label8.place(x=5,y=340)
label6=Label(root,text="City",bg="white").place(x=30,y=320)
City_name=tk.StringVar()
City=Entry(root,width=25,textvariable=City_name).place(x=30,y=340)
image=Image.open("icon5.png")
resize_image =image.resize((20, 20))
img = ImageTk.PhotoImage(resize_image)
label8 = Label(image=img,bg='orange')
label8.image=img
label8.place(x=5,y=390)
label6=Label(root,text="Email",bg="white").place(x=30,y=370)
Email_name=tk.StringVar()
Email=Entry(root,width=25,textvariable=Email_name).place(x=30,y=390)
image=Image.open("icon5.png")
resize_image =image.resize((20, 20))
img = ImageTk.PhotoImage(resize_image)
label8 = Label(image=img,bg='orange')
label8.image=img
label8.place(x=5,y=440)
label6=Label(root,text="Enter password",bg="white").place(x=30,y=420)
Pass_name=tk.StringVar()
Password=Entry(root,width=25,textvariable=Pass_name).place(x=30,y=440)
image=Image.open("icon5.png")
resize_image =image.resize((20, 20))
img = ImageTk.PhotoImage(resize_image)
label8 = Label(image=img,bg='orange')
label8.image=img
label8.place(x=5,y=490)
label6=Label(root,text="Confirm password",bg="white").place(x=30,y=470)
Confirm_name=tk.StringVar()
Confirm=Entry(root,width=25,textvariable=Confirm_name).place(x=30,y=490)

btn1 = Button(root,width=10,bg='orange',text='Submit',fg='White',command=finalsub,font=('Arial', 14, 'bold') ).place(x=90,y=540)

root.mainloop()

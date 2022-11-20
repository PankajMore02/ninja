from tkinter import *
import tkinter as tk
from tkinter import Entry,Tk
from PIL import Image
from PIL import ImageTk
from tkcalendar import Calendar
from tkinter.filedialog import askopenfilename
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
	date=cal_name.get()
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
def google_open():
	webbrowser.open_new_tab("https://www.google.com")
def facebook_open():
	webbrowser.open_new_tab("https://www.facebook.com")
def twitter_open():
	webbrowser.open_new_tab("https://www.twitter.com")
 
		
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
label2=Label(root,text="LOGIN",bg='white',font=('Helvetica', 14)).place(x=130,y=100)
label3=Label(root,text="Username",bg="white",font=('Arial', 12)).place(x=10,y=150)

user_name=tk.StringVar()
username=Entry(root,width=18,textvariable=user_name,font=('Arial 14')).place(x=100,y=150)
label6=Label(root,text="Password",bg="white",font=('Arial', 12)).place(x=10,y=220)
pass_name=tk.StringVar()
password=Entry(root,width=18,textvariable=pass_name,font=('Arial 14')).place(x=100,y=220)
label5=Label(root,text="forgot password",bg="white",fg='blue').place(x=180,y=250)
btn1 = Button(root,width=10,bg='orange',text='LOGIN',fg='White',command=finalsub,font=('Arial', 14, 'bold') ).place(x=90,y=280)
image=Image.open("design.png")
resize_image =image.resize((300, 30))
img = ImageTk.PhotoImage(resize_image)
label8 = Label(image=img,bg='white')
label8.image=img
label8.place(x=0,y=350)
image=Image.open("google.png")
resize_image =image.resize((50, 50))
img = ImageTk.PhotoImage(resize_image)
button2= Button(root, image=img,command=google_open,borderwidth=0)
button2.image=img
button2.place(x=40,y=400)
image=Image.open("facebook.png")
resize_image =image.resize((50, 50))
img = ImageTk.PhotoImage(resize_image)
button3= Button(root, image=img,command= facebook_open,borderwidth=0)
button3.image=img
button3.place(x=130,y=400)
image=Image.open("twitter.png")
resize_image =image.resize((50, 50))
img = ImageTk.PhotoImage(resize_image)
button4= Button(root, image=img,command= twitter_open,borderwidth=0)
button4.image=img
button4.place(x=220,y=400)
label4=Label(root,text="Not Register yet?",bg="white").place(x=100,y=460)
label5=Label(root,text="Click here to sign up",bg="white").place(x=90,y=480)
def file_open():
    text_window.delete('1.0', END)
    filePath = askopenfilename(
        initialdir='', title='Select a File', filetype=(("Text File", ".py"), ("All Files", "*.*")))
    with open(filePath, 'r+') as askedFile:
        fileContents = askedFile.read()

    text_window.insert(INSERT, fileContents)
    print(filePath)

button5=Button(root,text="sign up",bg="white",fg='blue').place(x=125,y=510)
root.mainloop()

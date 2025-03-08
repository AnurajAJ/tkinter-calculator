from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk
top = Tk()
radio = IntVar()
top.geometry("720x800")
top.title("Calculator")

bg_image = Image.open("top-view-desk-concept-with-notepad.jpg")
bg_image = bg_image.resize((1920,1080), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = Label(top, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


def perform_operations():
    n1 = int(e1.get())
    n2 = int(e2.get())

    if radio.get()==0:
        messagebox.showerror("Error","Please select an operation")

    if radio.get()==1:
        result=add(n1,n2)
    elif radio.get()==2:
        result=subtract(n1,n2)
    elif radio.get()==3:
        result=multiply(n1,n2)
    elif radio.get()==4:
        result=divide(n1,n2)

    result_text.delete("1.0",END)

    result_text.insert(END,f" Result = {result}")

def add(num1,num2):
    return(num1+num2)
def subtract(num1,num2):
    return(num1-num2)
def multiply(num1,num2):
    return (num1*num2)
def divide(num1,num2):
    return(num1/num2)


first_number = Label(top, text="Enter the first number")
first_number.grid(row=0, column=1,padx=50,pady=5)
e1=Entry(top)
e1.grid(row=0, column=2,pady=5)

second_number = Label(top, text="Enter the second number")
second_number.grid(row=1, column=1,padx=50,pady=5)
e2=Entry(top)
e2.grid(row=1, column=2,pady=5)

r1 = Radiobutton(top, text="Addition",variable=radio, value=1)
r1.grid(row=2, column=0,padx=20)
r2 = Radiobutton(top, text="Subtraction",variable=radio, value=2)
r2.grid(row=2, column=1,padx=20)
r3 = Radiobutton(top, text="Multiplication",variable=radio,value=3)
r3.grid(row=2, column=2,padx=20)
r4 = Radiobutton(top, text="Division",variable=radio, value=4)
r4.grid(row=2, column=3,padx=20)

button = Button(top, text="Submit",command=perform_operations)
button.grid(row=4, column=1)

result_text = Text(height=2, width=20)
result_text.grid(row=5, column=1)


top.mainloop()
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.maxsize(650,650)
root.minsize(650,650)

root.configure(background="blue")

open_img = ImageTk.PhotoImage(Image.open('open.png'))
save_img = ImageTk.PhotoImage(Image.open('save.png'))
exit_img = ImageTk.PhotoImage(Image.open('exit.jpg'))

lbl_file = Label(root, text="File name")
lbl_file.place(relx=0.28, rely=0.03, anchor= CENTER)

input_file = Entry(root)
input_file.place(relx=0.46, rely=0.03, anchor= CENTER)

my_text= Text(root,height=35,width=80)
my_text.place(relx=0.5, rely=0.55, anchor= CENTER)



def openfile():
    print("Hello miffy")
   
    print("Hello monisha")
    
    print("Hello mumma")
    
    print("Hello emilia")
    
    print("Hello renato")




root.mainloop()
from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry("200x200")

def encrypt_image():
    file1 = filedialog.askopenfile(mode = 'rb', filetype=[('jp file','*.jpg')])
    if file1 is not None :
         
        image = file1.read()
        file1.close()
        key = entry1.get(1.0,END)
        image = bytearray(image)
        for index,values in enumerate(image):
            image[index] = values^int(key)
        file1 = filedialog.asksaveasfile(mode = 'wb', defaultextension=".jpg")
        file1.write(image)
        file1.close()


buttn = Button(root, text = "encrypt/decrypt",command=encrypt_image)
buttn.place(x=50,y=90)

entry1 = Text(root, height = 1, width = 10) 
entry1.place(x=50,y=50)

key_label = Label(root, text="Key value: ")  
key_label.place(x=50, y=20)

root.mainloop()
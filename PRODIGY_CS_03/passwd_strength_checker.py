import tkinter as tk
from tkinter import *

main_window = Tk()
main_window.title("Password Complexity Checker")
main_window.geometry("400x400")
main_window.configure(bg="#bfc1c7")

framePass = Frame(main_window,bg="#bfc1c7")
framePass.pack(pady=10,fill = "x")

label1 = Label(framePass,text = "Password",bg = "#bfc1c7",pady=15,font=("Arial", 14))
label1.grid(row=0,column=1,pady=10,padx=(20, 0))
passwd = Entry(framePass,show="*",width=30)
passwd.grid(row=0,column=2,pady=10,padx=(20, 0))

messageLable= Label(main_window,text="",font = ("Arial",8))
messageLable.pack()

def clear_message(event):
    messageLable.configure(text="")

passwd.bind("<BackSpace>", clear_message)


def isValidPassword():
    messageLable.configure(text="")
    password = passwd.get()
    if len(password)<5 or len(password)>15 :
        messageLable.configure(text="Password length must be between 5 and 15 characters", fg = "red")
    else:
        lower_letter = False
        upper_letter = False
        special_char = False
        digit = False

        for char in password :
            if char.isdigit():
                digit = True
            if char.islower():
                lower_letter = True
            if char.isupper():
                upper_letter = True
            if (not char.isalnum()):
                special_char = True

        if ((digit) and (lower_letter) and (upper_letter) and (special_char)) == True:
            messageLable.configure(text = "Your password is strong", fg = "green")
        else :
            messageLable.configure(text = "Please make your password stronger. \nYour password is missing a number, uppercase letter,\n lowercase letter or special character", fg = "red")



check_button = Button(main_window, text = "Check", command = isValidPassword)
check_button.pack(pady=20)


main_window.mainloop()

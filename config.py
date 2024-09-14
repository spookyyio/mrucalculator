import customtkinter as ctk

def button_callback():
    print("button pressed!")

def create_button(app, text, command):
    button = ctk.CTkButton(master=app, text=text, command=command)
    return button

def button_callback():
    print("YUP..")

def createwindow():
    calculatorapp = ctk.CTk()
    ctk.set_appearance_mode("system")
    calculatorapp.title("URM Calculator")
    calculatorapp.geometry("700x400")

    button1 = create_button(calculatorapp, text="Horizontal Movement", command=button_callback)
    button1.pack()

    button2 = create_button(calculatorapp, text="Vertical Movement", command=button_callback)
    button2.pack()


    calculatorapp.mainloop()
    

    return calculatorapp
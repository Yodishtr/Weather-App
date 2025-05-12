from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
# from timezonefinder import TimeZoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

# search box
search_image = PhotoImage(file="./pics/search.png")
my_image = Label(image=search_image)
my_image.place(x=20, y=20)

textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040",
                     border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

search_icon = PhotoImage(file="./pics/search_icon.png")
my_search_icon = Button(root, image=search_icon, borderwidth=0, cursor="hand2", bg="#404040")
my_search_icon.place(x=400, y=34)

# Logo
logo_image = PhotoImage(file="./pics/logo.png")
logo = Label(root, image=logo_image)
logo.place(x=150, y=100)


# Bottom Box
frame_image = PhotoImage(file="./pics/box.png")
my_frame_image = Label(root, image=frame_image)
my_frame_image.pack(padx=5, pady=5, side=BOTTOM)

# Label 1
label1 = Label(root, text="Wind", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")






root.mainloop()

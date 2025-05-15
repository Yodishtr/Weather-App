from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import simpledialog
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

def getWeather():

    city = textfield.get()
    textfield.delete(0, tk.END)
    geolocator = Nominatim(user_agent="my_weather_app/1.0 (yodishtr@gmail.com)")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    name.config(text="Current Weather")

    # weather
    root.withdraw()
    api_key = simpledialog.askstring(title="API KEY", prompt="What is the api key", parent=root)
    root.deiconify()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    description = json_data['weather'][0]['description']
    temp = int(json_data['main']['temp'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']

    t.config(text=(str(temp) + "˚"))
    c.config(text=(condition + " | " + " Feels like " + str(temp) + "˚"))
    w.config(text=wind)
    h.config(text=humidity)
    d.config(text=description)
    p.config(text=pressure)
    textfield.focus()


# search box
search_image = PhotoImage(file="./pics/search.png")
my_image = Label(image=search_image)
my_image.place(x=20, y=20)

textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040",
                     border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

search_icon = PhotoImage(file="./pics/search_icon.png")
my_search_icon = Button(root, image=search_icon, borderwidth=0, cursor="hand2", bg="#404040",
                        command=getWeather)
my_search_icon.place(x=400, y=34)

# Logo
logo_image = PhotoImage(file="./pics/logo.png")
logo = Label(root, image=logo_image)
logo.place(x=150, y=100)


# Bottom Box
frame_image = PhotoImage(file="./pics/box.png")
my_frame_image = Label(root, image=frame_image)
my_frame_image.pack(padx=5, pady=5, side=BOTTOM)

# Time
name = Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock = Label(root, font=("Helvetica", 20))
clock.place(x=30, y=130)



# Label 1
label1 = Label(root, text="Wind", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)

# Label 2
label2 = Label(root, text="Humidity", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label2.place(x=250, y=400)

# Label 3
label3 = Label(root, text="Description", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label3.place(x=430, y=400)

# Label 4
label4 = Label(root, text="Pressure", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label4.place(x=650, y=400)

t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c = Label(font=("arial", 15, "bold"))
c.place(x=400, y=250)

w = Label(text=" ... ", font=("arial", 20, "bold"), fg="#1ab5ef")
w.place(x=120, y=430)

h = Label(text=" ... ", font=("arial", 20, "bold"), fg="#1ab5ef")
h.place(x=280, y=430)

d = Label(text=" ... ", font=("arial", 20, "bold"), fg="#1ab5ef")
d.place(x=450, y=430)

p = Label(text=" ... ", font=("arial", 20, "bold"), fg="#1ab5ef")
p.place(x=670, y=430)





root.mainloop()

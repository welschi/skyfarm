import tkinter as tk  # GUI Package importiert
from tkinter import ttk  # neuere ttk Widgets
from PIL import Image, ImageTk  # Pillow eingefügt für Bilder im Widget

########################################################################################################################

root = tk.Tk()  # Grundwidget erstellt --> Hauptfenster
root.title("Skyfarm")  # Titel des Gui erstellt
root.geometry("1500x1500")  # Größe des Fensters in Pixel
root.minsize(width=400, height=400)  # Minimalgröße des GUI
root.maxsize(width=4000, height=4000)  # Maximalgröße des GUI

style = ttk.Style()  # Theme geändert damit Farben gezeigt werden
style.theme_use("clam")

########################################################################################################################

def UpdaterButton():
    print("Das Interface wurde geupdated.")

########################################################################################################################

#  Bilder für die Widgets werden geöffnet

png_logo_open = Image.open("images/honeycomb.png").resize((300, 300))
png_logo = ImageTk.PhotoImage(png_logo_open)

png_temp_open = Image.open("images/temperatur.png").resize((300, 300))
png_temp = ImageTk.PhotoImage(png_temp_open)

png_time_open = Image.open("images/time.png").resize((300, 300))
png_time = ImageTk.PhotoImage(png_time_open)

png_level_open = Image.open("images/level.png").resize((300, 300))
png_level = ImageTk.PhotoImage(png_level_open)

png_humidity_open = Image.open("images/humidity.png").resize((300, 300))
png_humidity = ImageTk.PhotoImage(png_humidity_open)

########################################################################################################################

#  Die verschiedenen Widgets (statisch) werden erzeugt

temp = ttk.Label(root, text="Momentane Temperatur: ", image=png_temp, compound="left", font=("Arial", 30))
temp.pack(side="bottom")  # Label wird im Hauptfenster erstellt --> Pack = Layoutmanager

time = ttk.Label(root, text="Zeit verstrichen seit der Saat: ", image=png_time, compound="left", font=("Arial", 30))
time.pack(side="bottom")

level = ttk.Label(root, text="Wasserstandlevel des Tanks: ", image=png_level, compound="left", font=("Arial", 30))
level.pack(side="bottom")

humidity = ttk.Label(root, text="Momentane Luftfeuchtigkeit: ", image=png_humidity, compound="left", font=("Arial", 30))
humidity.pack(side="bottom",)

########################################################################################################################

#  Buttons werden erstellt

update = ttk.Button(root, text="UPDATE", padding=10, command=UpdaterButton)
update.pack(side="top")

quit_button = ttk.Button(root, text="Programm beenden", padding=10, command=root.destroy)
quit_button.pack(side="bottom")

#  for conf in level.keys():  # Zeigt mir mögliche cfg Optionen vom Widget in der Konsole an
#   print(conf, ": ", level[conf])

########################################################################################################################

root.mainloop()  # Startet die GUI und pausiert den nachfolgenden Code

import tkinter as tk  # GUI Package importiert
from tkinter import ttk  # neuere ttk Widgets
from PIL import Image, ImageTk  # Pillow eingefügt für Bilder im Widget

root = tk.Tk()  # Grundwidget erstellt --> Hauptfenster
root.title("Skyfarm")  # Titel des Gui erstellt
root.geometry("800x800")  # Größe des Fensters in Pixel
root.minsize(width=400, height=400)  # Minimalgröße des GUI
root.maxsize(width=4000, height=4000)  # Maximalgröße des GUI

style = ttk.Style()  # Theme geändert damit Farben gezeigt werden
style.theme_use("clam")

png_logo_open = Image.open("images/honeycomb.png").resize((300, 300))  # Bilder werden geöffnet
png_logo = ImageTk.PhotoImage(png_logo_open)

png_temp_open = Image.open("images/temperatur.png").resize((300, 300))  # Bilder werden geöffnet
png_temp = ImageTk.PhotoImage(png_temp_open)

temp = ttk.Label(root, text="Momentane Temperatur: ", image=png_temp, compound="left", font=("Arial", 30))  # Temp. Widget mit Icon
temp.pack()  # Label wird im Hauptfenster erstellt --> Pack = Layoutmanager

time = ttk.Label(root, text="Zeit verstrichen seit der Saat: ", font=("Arial", 30))  # Time Widget
time.pack()

level = ttk.Label(root, text="Wasserstandlevel des Tanks: ", font=("Arial", 30))  # Level Widget
level.pack()

humidity = ttk.Label(root, text="Momentane Luftfeuchtigkeit: ", font=("Arial", 30))  # Luftfeuchtigkeit Widget
humidity.pack()

for conf in level.keys():  # Zeigt mir mögliche cfg Optionen vom Widget in der Konsole an
    print(conf, ": ", level[conf])

root.mainloop()  # Startet die GUI und pausiert den nachfolgenden Code

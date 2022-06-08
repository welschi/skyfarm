import tkinter as tk  # GUI Package importiert

root = tk.Tk()  # Grundwidget erstellt --> Hauptfenster

label = tk.Label(root, text="Sky farms")  # Das was in dem Fenster drin steht
label.pack()  # Hallo Welt wird m Hauptfenster erstellt --> Pak = Layoutmanager

root.mainloop()  # Startet die GUI

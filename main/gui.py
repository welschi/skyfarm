import tkinter as tk  # GUI Package importiert

root = tk.Tk()  # Grundwidget erstellt --> Hauptfenster
root.title("Skyfarm")  # Titel des Gui erstellt
root.geometry("800x800")  # Größe des Fensters in Pixel
root.minsize(width=400, height=400)  # Minimalgröße des GUI
root.maxsize(width=4000, height=4000)  # Maximalgröße des GUI

label1 = tk.Label(root, text="Hier sollen unsere Buttons hin", bg="red")  # Das was in dem Fenster drin steht
label1.pack(side="left")  # Label wird im Hauptfenster erstellt --> Pack = Layoutmanager

label2 = tk.Label(root, text="Test", bg="blue")  # 2. Widget im GUI
label2.pack()

root.mainloop()  # Startet die GUI und pausiert den folgenden Code

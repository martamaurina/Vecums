import tkinter as tk
import datetime
from PIL import Image, ImageTk

#class Persona:
    #def __init__(self, vards, gads, menesis, diena,):
        #self.vards=vards
        #self.gads=gads
        #self.menesis=menesis
        #self.diena=diena
   # def age(self):
        #today = datetime.today()


def aprekina_vec():
    today = datetime.date.today()
    
    year =int(gads.get())
    month = int(men.get())
    day= int(diena.get())

    birt_date = datetime.date(year, month, day)
    age = today.year - birt_date.year
    #if (today.month)

    listbox.delete(0, tk.END)
    listbox.insert(tk.END, f"Sveiki, mani sauc {vards.get()} un man ir {age}. gadi")


master= tk.Tk()
master.geometry("500x500")
master.title("Vecuma aprēķinātājs")
#master.configure(background="grey")

btnvards = tk.Label(master, text="Vārds")
btnvards.grid(row=1, column=0, padx=5, pady=5)
vards = tk.Entry(master)
vards.grid(row=1, column=1)

btngads = tk.Label(master, text="Gads")
btngads.grid(row=2, column=0, padx=5, pady=5)
gads = tk.Entry(master)
gads.grid(row=2, column=1)

btnmen = tk.Label(master, text="Mēnesis")
btnmen.grid(row=3, column=0, padx=5, pady=5)
men = tk.Entry(master)
men.grid(row=3, column=1)

btndiena = tk.Label(master, text="Diena")
btndiena.grid(row=4, column=0, padx=5, pady=5)
diena = tk.Entry(master)
diena.grid(row=4, column=1)

btnaprek = tk.Button(master, text="Aprēķināt vecumu", command= lambda: aprekina_vec())
btnaprek.grid(row=5, column=1, padx=5, pady=5)

listbox=tk.Listbox(master, width=50)
listbox.grid(pady=10, padx=20, row=6, column=1)


master.mainloop()


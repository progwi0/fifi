import os
from tkinter import *
from tkinter import messagebox as dialogus
from tkinter import filedialog

app = Tk()
app.title("Fifi")

def info():
    dialogus.showinfo("🪶", "Fifi 1.0\nCreated in 2025 by progwi0.")

def save():
    filename = filedialog.asksaveasfilename(defaultextension=".txt",
                                        filetypes=[("Text Files", "*.txt")],
                                        title="Save as")
    with open(filename, "w") as f:
        f.write(text.get("1.0", "end-1c"))
        
def openf():
    filename = filedialog.askopenfilename(defaultextension=".txt",
                                        filetypes=[("Text Files", "*.txt")],
                                        title="Open")
    with open(filename, "r") as file:
        text.delete(1.0, "end")
        text.insert("1.0", file.read())

def menus():
    menu.post(app.winfo_pointerx(), app.winfo_pointery())

feather = Button(app, text = "🪶", command = lambda:menu.post(app.winfo_pointerx(), app.winfo_pointery()))
feather.pack(fill = "x")

text = Text(app)
text.pack(fill = "both", expand = True)

menu = Menu(app, tearoff = 0)
menu.add_command(label="New", command = lambda:os.system("fifi"))
menu.add_command(label="Open", command = openf)
menu.add_command(label="Save", command = save)
menu.add_separator()
menu.add_command(label="Reinstall (Only for pix version)", command = lambda:os.system("pix reinstall fifi"))
menu.add_separator()
menu.add_command(label="About", command = info)

app.mainloop()

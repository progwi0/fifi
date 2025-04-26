import os
import webbrowser
from tkinter import messagebox as dialogus
from tkinter import filedialog
from ttkbootstrap import *
from ttkbootstrap.constants import *

app = Window(themename="litera")
app.title("Fifi")

homus = os.path.expanduser("~")
patus = os.path.join(homus, ".progwi0")
themepath = os.path.join(patus, "theme.txt")

simplus = "~/.progwi0/theme.txt"

if not os.path.exists(simplus):
    os.system("cd ~ && mkdir .progwi0 && cd .progwi0 && touch theme.txt")

def info():
    dialogus.showinfo("🪶", "Fifi 5.0\nCreated in 2025 by progwi0.")

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

def light():
    app.style.theme_use("litera")
    with open(themepath, "w") as file:
        file.write("litera")

def dark():
    app.style.theme_use("darkly")
    with open(themepath, "w") as file:
        file.write("darkly")

def menus():
    menu.post(app.winfo_pointerx(), app.winfo_pointery())

feather = Button(app, text = "🪶", command = lambda:menu.post(app.winfo_pointerx(), app.winfo_pointery()), bootstyle = SECONDARY)
feather.pack(fill = "x")

text = Text(app)
text.pack(fill = "both", expand = True)

menu = Menu(app, tearoff = 0)
menu.add_separator()
menu.add_command(label="New", command = lambda:os.system("fifi"))
menu.add_command(label="Open", command = openf)
menu.add_command(label="Save", command = save)
menu.add_separator()
menu.add_command(label="Light theme", command = light)
menu.add_command(label="Dark theme", command = dark)
menu.add_separator()
menu.add_command(label="Update (Only for pix version)", command = lambda:os.system("pix reinstall fifi"))
menu.add_separator()
menu.add_command(label="My site", command = lambda:webbrowser.open("https://progwi0.github.io/"))
menu.add_command(label="About", command = info)
menu.add_separator()

with open(themepath, "r") as file:
        themus = file.read().strip()
        app.style.theme_use(themus)

app.mainloop()

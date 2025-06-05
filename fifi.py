import gi
gi.require_version("Gtk", "3.0")
gi.require_version("GdkPixbuf", "2.0")
from gi.repository import Gtk, GdkPixbuf
import os
import webbrowser

fifi = Gtk.Window(title = "Fifi")
fifi.set_default_size(1280, 960)
ui = Gtk.ScrolledWindow()

header = Gtk.HeaderBar()

fififeather = Gtk.MenuButton()
fififeather.set_hexpand(True)
fififeather.connect("clicked", lambda fififeather:exp.show_all())

closus = Gtk.Button()
closus.connect("clicked", Gtk.main_quit)

header.pack_start(fififeather)
header.pack_end(closus)

fifiimg = Gtk.Image.new_from_icon_name("emoji-symbols-symbolic", Gtk.IconSize.BUTTON)
fififeather.set_image(fifiimg)

closusimg = Gtk.Image.new_from_icon_name("window-close-symbolic", Gtk.IconSize.BUTTON)
closus.set_image(closusimg)

header.set_custom_title(fififeather)

entry = Gtk.TextView()

entry.set_hexpand(True)
entry.set_vexpand(True)

entry.set_left_margin(10)
entry.set_right_margin(10)
entry.set_top_margin(10)
entry.set_bottom_margin(10)

ui.add(entry)

menu = Gtk.Menu()

newwindow = Gtk.MenuItem(label = "New window")
newwindow.connect("activate", lambda newwindow:os.system("fifi"))
menu.append(newwindow)

def save(widget):
    filename = Gtk.FileChooserDialog(
        title="savus", 
        parent=fifi, 
        action=Gtk.FileChooserAction.SAVE
    )
    
    filename.add_button(Gtk.STOCK_SAVE, Gtk.ResponseType.OK)
    
    response = filename.run()
    
    if response == Gtk.ResponseType.OK:
        filus = filename.get_filename()
        
        buffer = entry.get_buffer()
        start_iter, end_iter = buffer.get_bounds()
        contentus = buffer.get_text(start_iter, end_iter, True)
        
        with open(filus, "w") as f:
            f.write(contentus)

    filename.destroy()
            
    filename.destroy()
    
def openf(widget):
    filename = Gtk.FileChooserDialog(
        title="openus", 
        parent=fifi, 
        action=Gtk.FileChooserAction.OPEN
    )
    
    filename.add_button(Gtk.STOCK_OPEN, Gtk.ResponseType.OK)
    
    response = filename.run()
    
    if response == Gtk.ResponseType.OK:
        filus = filename.get_filename()
        with open(filus, "r") as f:
            buffer = entry.get_buffer()
            buffer.set_text(f.read())
            filename.destroy()
            
    filename.destroy()

def about(widget):
    dialogus = Gtk.AboutDialog()
    
    dialogus.set_program_name("Fifi")
    dialogus.set_version("11.0")
    dialogus.set_copyright("© 2025 progwi0")
    dialogus.set_comments("Simple text editor on GTK3!")
    
    dialogus.set_website("https://progwi0.github.io/")
    dialogus.set_authors(["progwi0", "chicken banana", "sigma"])
    
    dialogus.set_license_type(Gtk.License.GPL_3_0)
    
    dialogus.run()
    dialogus.destroy()

exp = Gtk.Popover()

menus = Gtk.Box(spacing=1, orientation=Gtk.Orientation.VERTICAL)

newwindows = Gtk.Button(label = "New window")
newwindows.connect("clicked", lambda newwindow:os.system("fifi"))
menus.pack_start(newwindows, True, True, 0)

savus = Gtk.Button(label = "Save")
savus.connect("clicked", save)
menus.pack_start(savus, True, True, 0)

openus = Gtk.Button(label = "Open")
openus.connect("clicked", openf)
menus.pack_start(openus, True, True, 0)

mysite = Gtk.Button(label = "My site")
mysite.connect("clicked", lambda mysite:webbrowser.open("https://progwi0.github.io/"))
menus.pack_start(mysite, True, True, 0)

abouts = Gtk.Button(label = "About Fifi")
abouts.connect("clicked", about)
menus.pack_start(abouts, True, True, 0)

exp.add(menus)
fififeather.set_popover(exp)

fifi.set_titlebar(header)

fifi.add(ui)

fifi.connect("destroy", Gtk.main_quit)
fifi.show_all()

Gtk.main()

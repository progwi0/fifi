import gi
gi.require_version("Gtk", "3.0")
gi.require_version("GdkPixbuf", "2.0")
from gi.repository import Gtk, GdkPixbuf
import os

fifi = Gtk.Window(title = "Kreka")
fifi.set_default_size(1280, 960)
fifi.set_icon_from_file("/usr/share/icons/fifi.png")
ui = Gtk.ScrolledWindow()

header = Gtk.HeaderBar(title = "Fifi", subtitle = "d")
header.set_show_close_button(True)

fififeather = Gtk.Button()
fififeather.set_hexpand(True)
fififeather.connect("clicked", lambda fififeather:menu.popup(None, None, None, None, 0, Gtk.get_current_event_time()))

fifiimg = Gtk.Image.new_from_icon_name("emoji-symbols-symbolic", Gtk.IconSize.BUTTON)
fififeather.set_image(fifiimg)

header.set_custom_title(fififeather)

entry = Gtk.TextView()
entry.set_hexpand(True)
entry.set_vexpand(True)

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
            f.write(entry.get_text("1.0", "end-1c"))
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
        
savus = Gtk.MenuItem(label = "Save")
savus.connect("activate", save)
menu.append(savus)

openus = Gtk.MenuItem(label = "Open")
openus.connect("activate", openf)
menu.append(openus)

mysite = Gtk.MenuItem(label = "My site")
mysite.connect("activate", lambda mysite:webbrowser.open("https://progwi0.github.io/"))
menu.append(mysite)

def about(widget):
    dialogus = Gtk.AboutDialog()
    
    dialogus.set_program_name("Fifi")
    dialogus.set_version("7.0")
    dialogus.set_copyright("© 2025 progwi0")
    dialogus.set_comments("Simple text editor on GTK3!")
    
    iconus = GdkPixbuf.Pixbuf.new_from_file_at_size("/usr/share/icons/fifi.png", 64, 64)
    dialogus.set_logo(iconus)
    
    dialogus.set_website("https://progwi0.github.io/")
    dialogus.set_authors(["progwi0", "chicken banana", "sigma"])
    
    dialogus.set_license_type(Gtk.License.GPL_3_0)
    
    dialogus.run()
    dialogus.destroy()

abouts = Gtk.MenuItem(label = "About Fifi")
abouts.connect("activate", about)
menu.append(abouts)

menu.show_all()

fifi.set_titlebar(header)

fifi.add(ui)

fifi.connect("destroy", Gtk.main_quit)
fifi.show_all()

Gtk.main()

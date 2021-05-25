import tkinter as tk
import spectrum_finder.gui.guifunc as guif
from tkinter import messagebox


mwin = guif.Window1()

grid_rc = [[50,100,100,100,100],[50,80,80,100,100,100]]
guif.configure_grid(mwin, grid_rc)

guif.create_display1(mwin,tk,messagebox)

mwin.mainloop()

grav,metal,temp,interp = mwin.getvar(name="user_grav"),mwin.getvar(name="user_metal"),mwin.getvar(name="user_temp"),mwin.getvar(name="user_interp")
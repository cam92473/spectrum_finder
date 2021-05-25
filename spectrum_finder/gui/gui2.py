import tkinter as tk
import spectrum_finder.gui.guifunc as guif
from tkinter import messagebox
from spectrum_finder.calculations.search import grav,metal,temp,grav_lo_N,metal_lo,temp_lo_N,grav_hi_N,metal_hi,temp_hi_N,interp_par,swim_dict


mwin = guif.Window2()

guif.create_display2(mwin,tk,grav,metal,temp,grav_lo_N,metal_lo,temp_lo_N,grav_hi_N,metal_hi,temp_hi_N,interp_par,swim_dict)

mwin.mainloop()


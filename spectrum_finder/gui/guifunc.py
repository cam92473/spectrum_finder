from PIL import Image, ImageTk
import tkinter as tk
import ctypes
import os
from math import sqrt

class Window1(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("SpectroSearch")
        self.geometry("620x420+450+200")
        self.configure(bg="gray85")


class Window2(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Results")
        self.geometry("1700x800+100+80")
        self.configure(bg="gray85")

def configure_grid(mwin, grid_rc):
    for row in range(0,len(grid_rc[0])):
        mwin.rowconfigure(row,minsize=grid_rc[0][row])
    for column in range(0,len(grid_rc[1])):
        mwin.columnconfigure(column,minsize=grid_rc[1][column])

def get_image(filepath,dimx,dimy):
    image = Image.open(f"{filepath}")
    image_rsize = image.resize((dimx,dimy))
    image_rsize_conv = ImageTk.PhotoImage(image_rsize)
    return image_rsize_conv

def get_images_combine(bgfilepath,bgdimx,bgdimy,fgfilepath,fgdimx,fgdimy,sdfilepath,sddimx,sddimy,x,y,sdx,sdy):
    Bgimage = Image.open(f"{bgfilepath}")
    Bgimage_copy = Bgimage.copy()
    Bgimage_copy_rsize = Bgimage_copy.resize((bgdimx,bgdimy))

    Fgimage = Image.open(f"{fgfilepath}")
    Fgimage_copy = Fgimage.copy()
    Fgimage_copy_rsize = Fgimage_copy.resize((fgdimx,fgdimy))

    Sdimage = Image.open(f"{sdfilepath}")
    Sdimage_copy = Sdimage.copy()
    Sdimage_copy_rsize = Sdimage_copy.resize((sddimx,sddimy))

    Bgimage_copy_rsize.paste(Sdimage_copy_rsize,(sdx,sdy))
    Bgimage_copy_rsize.save("comb1Img.png")
    Combimage1 = Image.open("comb1Img.png")
    Combimage1.paste(Fgimage_copy_rsize,(x,y))
    Combimage1.save("comb2Img.png")
    Combimage2 = Image.open("comb2Img.png")

    Finalimage = ImageTk.PhotoImage(Combimage2)
    os.remove("comb1Img.png")
    os.remove("comb2Img.png")
    return Finalimage

def create_frames(mwin,tk):

    frame12 = tk.Frame(mwin)
    frame12.grid(row=1, column=2)

    frame22 = tk.Frame(mwin)
    frame22.grid(row=2, column=2)

    frame32 = tk.Frame(mwin)
    frame32.grid(row=3, column=2)

    frame14 = tk.Frame(mwin)
    frame14.grid(row=1, column=4)

    return frame12,frame22,frame32,frame14

def create_display1(mwin,tk,messagebox):

    #ctypes.windll.shcore.SetProcessDpiAwareness(1)

    def getinfoclose(mwin,tk,messagebox):

        try:
            user_grav = float(entrybox1.get())
            user_metal = float(entrybox2.get())
            user_temp = float(entrybox3.get())
            user_interp = selected_method.get()
        except:
            tk.messagebox.showinfo('Error', 'Please enter numbers')
        else:
            if user_grav < 0 or user_grav > 5:
                tk.messagebox.showinfo('Error', 'Please enter a value from 0 to 5')
            elif user_metal < -2.5 or user_metal > 0.5:
                tk.messagebox.showinfo('Error', 'Please enter a value from -2.5 to 0.5')
            elif user_temp < 3500 or user_temp > 50000:
                tk.messagebox.showinfo('Error', 'Please enter a value from 3500 to 50000')
            elif user_interp == "                                 ":
                tk.messagebox.showinfo('Error', 'Please select an interpolation method')
            else:
                mwin.destroy()
                mwin.setvar(name="user_grav",value=user_grav)
                mwin.setvar(name="user_metal", value=user_metal)
                mwin.setvar(name="user_temp", value=user_temp)
                mwin.setvar(name="user_interp", value=user_interp)

    frame12, frame22, frame32, frame14 = create_frames(mwin, tk)

    apple = get_image("spectrum_finder/images/apple.png", 40, 40)
    mwin.apple = apple
    carbon = get_image("spectrum_finder/images/carbon_red.png", 40, 40)
    mwin.carbon = carbon
    thermom = get_image("spectrum_finder/images/thermometer.png", 40, 40)
    mwin.thermom = thermom

    img_label1 = tk.Label(mwin, image=apple, borderwidth=0).grid(row=1, column=1, padx=0)
    img_label2 = tk.Label(mwin, image=carbon, borderwidth=0).grid(row=2, column=1, padx=0)
    img_label3 = tk.Label(mwin, image=thermom, borderwidth=0).grid(row=3, column=1, padx=0)

    text_label1 = tk.Label(frame12, text="Log of surface gravity", bd=4, relief=tk.GROOVE, padx=10, bg="white").pack(padx=0,pady=0)
    text_label2 = tk.Label(frame22, text="Abundance ratio", bd=4, relief=tk.GROOVE, padx=23, bg="white").pack(padx=0,pady=0)
    text_label3 = tk.Label(frame32, text="Temperature", bd=4, relief=tk.GROOVE, padx=34, bg="white").pack(padx=0,pady=0)

    entrybox1 = tk.Entry(frame12, width=22, bd=4, relief=tk.SUNKEN)
    entrybox1.pack(padx=0, pady=0)
    text_label1b = tk.Label(frame12, text="(min: 0.0, max: 5.0)", padx=20, bg = "gray85").pack(padx=0, pady=0)
    entrybox2 = tk.Entry(frame22, width=22, bd=4, relief=tk.SUNKEN)
    entrybox2.pack(padx=0, pady=0)
    text_label1b = tk.Label(frame22, text="(min: -2.5, max: 0.5)", padx=18, bg="gray85").pack(padx=0,pady=0)
    entrybox3 = tk.Entry(frame32, width=22, bd=4, relief=tk.SUNKEN)
    entrybox3.pack(padx=0, pady=0)
    text_label1b = tk.Label(frame32, text="(min: 3500, max: 50000)", padx=9, bg="gray85").pack(padx=0,pady=0)

    text_label4 = tk.Label(frame14, text="Interpolation method", bd=4, relief=tk.GROOVE, padx=10, pady=4,bg="white").pack(padx=0, pady=0)
    selected_method = tk.StringVar()
    selected_method.set("                                 ")
    optionmenu = tk.OptionMenu(frame14, selected_method, "Nearest neighbour", "            Linear          ")
    optionmenu.pack()

    button1 = tk.Button(mwin, font = ("Arial",12), text="Start", bd=4, relief=tk.RAISED, command = lambda: getinfoclose(mwin,tk,messagebox),padx = 25, pady = 15)
    button1.grid(rowspan=2, row=2, column=4)

def create_display2(mwin,tk,grav,metal,temp,grav_lo_N,metal_lo,temp_lo_N,grav_hi_N,metal_hi,temp_hi_N,interp_par,swim_dict):

    ctypes.windll.shcore.SetProcessDpiAwareness(1)

    #ORIGIN 740 426
    #FACE LENGTH 288
    TEMP_SCALE_FACTOR = 288/(temp_hi_N-temp_lo_N)
    METAL_SCALE_FACTOR = 288/(metal_hi-metal_lo)
    #DIAGONAL LENGTH 136
    GRAV_SCALE_FACTOR = 136/(grav_hi_N-grav_lo_N)


    if interp_par == "linear":
        #Remember: rotated xyz coordinate system
        xyzsys_x = int(round(TEMP_SCALE_FACTOR * (temp - temp_lo_N) + 740))
        xyzsys_y = int(round(-METAL_SCALE_FACTOR*(metal-metal_lo)+426))
        xyzsys_zboost = int(round(GRAV_SCALE_FACTOR*(grav - grav_lo_N)/sqrt(2)))

        xysys_x = xyzsys_x-xyzsys_zboost
        xysys_y = xyzsys_y+xyzsys_zboost

        xysys_sdx = xysys_x+1
        xysys_sdy = xyzsys_zboost+431

        dotlabel = tk.Label(mwin,font=("Arial",12),text="({}, {}, {})".format(grav,temp,metal),padx=10,pady=5)
        dotlabel.place(x=950,y=680)


    grav_switch,temp_switch,metal_switch = grav,temp,metal

    if interp_par == "nearest":
        if grav-grav_lo_N < (grav_hi_N-grav_lo_N)/2:
            xyzsys_zboost = 0
            grav_switch = grav_lo_N

        elif grav-grav_lo_N >= (grav_hi_N-grav_lo_N)/2:
            xyzsys_zboost = 96
            grav_switch = grav_hi_N

        if temp-temp_lo_N < (temp_hi_N-temp_lo_N)/2:
            xyzsys_x = 740
            temp_switch = temp_lo_N

        elif temp-temp_lo_N >= (temp_hi_N-temp_lo_N)/2:
            xyzsys_x = 1028
            temp_switch = temp_hi_N

        if metal-metal_lo < (metal_hi-metal_lo)/2:
            xyzsys_y = 426
            metal_switch = metal_lo

        elif metal-metal_lo >= (metal_hi-metal_lo)/2:
            xyzsys_y = 138
            metal_switch = metal_hi

        xysys_x = xyzsys_x-xyzsys_zboost
        xysys_y = xyzsys_y+xyzsys_zboost

        xysys_sdx = xysys_x+1
        xysys_sdy = xyzsys_zboost+431

    cubedot = get_images_combine("spectrum_finder/images/cube.PNG",1211,702,"spectrum_finder/images/dot.PNG",20,20,"spectrum_finder/images/shadow.PNG",18,10,xysys_x,xysys_y,xysys_sdx,xysys_sdy)
    mwin.cubedot = cubedot

    cubedotlabel = tk.Label(mwin, image = cubedot, borderwidth = 0, highlightthickness = 0)
    cubedotlabel.place(x=400,y= 50)

    dotlabel = tk.Label(mwin, font=("Arial", 12), text="({}, {}, {})".format(grav_switch, temp_switch, metal_switch),padx=10, pady=5)
    dotlabel.place(x=950, y=680)

    grav_axis_text = tk.Label(mwin,font=("Arial",12), text="Log of surface gravity", bd=4)
    grav_axis_text.place(x=300, y=735)
    temp_axis_text = tk.Label(mwin,font=("Arial",12), text="Temperature",bd=4)
    temp_axis_text.place(x=725, y=628)
    metal_axis_text = tk.Label(mwin,font=("Arial",12), text="Abundance ratio",bd=4)
    metal_axis_text.place(x=425, y=380)

    gl_tl_ml = tk.Label(mwin,font=("Arial",12),text="({})".format(list(swim_dict.values())[0]),padx=10,pady=5)
    gl_tl_ml.place(x=894,y=468)
    gh_tl_ml = tk.Label(mwin,font=("Arial",12),text="({})".format(list(swim_dict.values())[1]),padx=10,pady=5)
    gh_tl_ml.place(x=955,y=596)

    gl_th_ml = tk.Label(mwin,font=("Arial",12),text="({})".format(list(swim_dict.values())[2]),padx=10,pady=5)
    gl_th_ml.place(x=1447,y=468)
    gh_th_ml = tk.Label(mwin,font=("Arial",12),text="({})".format(list(swim_dict.values())[3]),padx=10,pady=5)
    gh_th_ml.place(x=1300,y=596)

    gl_tl_mh = tk.Label(mwin,font=("Arial",12),text="({})".format(list(swim_dict.values())[4]),padx=10,pady=5)
    gl_tl_mh.place(x=1085,y=150)
    gh_tl_mh = tk.Label(mwin,font=("Arial",12),text="({})".format(list(swim_dict.values())[5]),padx=10,pady=5)
    gh_tl_mh.place(x=894,y=275)

    gl_th_mh = tk.Label(mwin,font=("Arial",12),text="({})".format(list(swim_dict.values())[6]),padx=10,pady=5)
    gl_th_mh.place(x=1385,y=150)
    gh_th_mh = tk.Label(mwin,font=("Arial",12),text="({})".format(list(swim_dict.values())[7]),padx=10,pady=5)
    gh_th_mh.place(x=1447,y=275)

    youentered1 = tk.Label(mwin,relief = tk.RIDGE, font=("Arial",12),text="Inputs\n\nLog of surface gravity: {}\n\nAbundance ratio: {}\n\nTemperature: {}\n\nInterpolation method: {}".format(grav,metal,temp,interp_par),padx=10,pady=5)
    youentered1.place(x=50,y=450)


    yetanotherlabel = tk.Label(text = "------------------------------Search results------------------------------",bd=4, font=("Arial",11),pady=5)
    yetanotherlabel.place(x=185,y=50)

    count = 3
    for entry in swim_dict:
        if swim_dict[entry] == entry:
            reportlabel = tk.Label(text="Cube coordinate ({}) found.".format(entry),font=("Arial",9))
            reportlabel.place(x=90,y=50+count*20)
            count += 1
        elif swim_dict[entry] != entry:
            reportlabel = tk.Label(text = "Cube coordinate ({}) not found. Used nearest (non-overlapping) existing coordinate at ({})".format(entry,swim_dict[entry]),font=("Arial",9))
            reportlabel.place(x=90, y=50+count*20)
            count += 1

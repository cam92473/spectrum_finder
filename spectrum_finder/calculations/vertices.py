import math
from spectrum_finder.gui.gui1 import grav,metal,temp,interp


interp = interp

if grav%0.5 != 0 and grav != 5:
    grav_lo = math.floor(2*grav)/2
    grav_hi = math.ceil(2*grav)/2
elif grav%0.5 == 0 and grav != 5:
    grav_lo = grav
    grav_hi = grav+0.5
elif grav == 5:
    grav_lo = 4.5
    grav_hi = 5

if metal < 0:
    if metal % 0.5 != 0:
        metal_lo = math.floor(2 * metal) / 2
        metal_hi = math.ceil(2 * metal) / 2
    elif metal % 0.5 == 0:
        metal_lo = metal
        metal_hi = metal + 0.5
elif metal >= 0 and metal < 0.2:
    metal_lo = 0
    metal_hi = 0.2
elif metal >= 0.2 and metal <= 0.5:
    metal_lo = 0.2
    metal_hi = 0.5

if temp%250 != 0 and temp != 50000:
    temp_lo = math.floor(4 / 1000 * temp) / 4 * 1000
    temp_hi = math.ceil(4 / 1000 * temp) / 4 * 1000
elif temp%250 == 0 and temp != 50000:
    temp_lo = temp
    temp_hi = temp+250
elif temp == 50000:
    temp_lo = 47500
    temp_hi = 50000

#####

def grav_lo_str(grav_lo):
    return "g" + str(grav_lo).replace(".", "")

def grav_hi_str(grav_hi):
    return "g" + str(grav_hi).replace(".", "")

def metal_lo_str(metal_lo):
    if metal_lo == 0:
        return "p00"
    elif str(metal_lo).find("-") != -1:
        return str(metal_lo).replace(".", "").replace("-", "m")
    else:
        return "p"+str(metal_lo).replace(".", "")

def metal_hi_str(metal_hi):
    if metal_hi == 0:
        return "p00"
    elif str(metal_hi).find("-") != -1:
        return str(metal_hi).replace(".", "").replace("-", "m")
    else:
        return "p"+str(metal_hi).replace(".", "")

def temp_lo_str(temp_lo):
    return str(int(temp_lo))

def temp_hi_str(temp_hi):
    return str(int(temp_hi))

if interp == "            Linear          ":
    interp_par = "linear"

elif interp == "Nearest neighbour":
    interp_par = "nearest"


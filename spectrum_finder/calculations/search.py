from astropy.io import fits
from spectrum_finder.calculations.vertices import grav,metal,temp,grav_lo,metal_lo,temp_lo,grav_hi,metal_hi,temp_hi,grav_lo_str,grav_hi_str,temp_lo_str,temp_hi_str,metal_lo_str,metal_hi_str,interp_par


# --------------
# To interpolate, we must split our spectra at each corner, resulting in 1221 cubes with a single wavelength at each corner.
# We can find the list of wavelengths on each cube by looking at the columns of the array of spectra, or
# the rows of the transposed array of spectra
# --------------


def search_for_corner(metal_func,metal_in,temp_func,temp_in,grav_func,grav_in,indicator,swim_dir_t,swim_dir_g):

    #print("searching {}, swimming {} in temp and {} in grav".format(indicator,swim_dir_t,swim_dir_g))

    temp_swimming = True
    grav_swimming = True
    i = 0
    j = 0

    while temp_swimming is True:

        if temp_swimming is True and swim_dir_t == "up":
            try:
                with fits.open("fits_library/ck{}/ck{}_{}.fits".format(metal_func(metal_in), metal_func(metal_in),temp_func(temp_in+i))) as hdul:
                    #print("Found temp after swimming up {} miles in temp".format(i/250))
                    temp_out = temp_in+i
                    temp_swimming = False
                    while grav_swimming is True:
                        if grav_swimming is True and swim_dir_g == "up":
                            try:
                                spectrum = hdul[1].data["{}".format(grav_func(grav_in+j))]
                                #print("Found grav after swimming {} miles in grav".format(j/0.5))
                                grav_out = grav_in+j
                                grav_swimming = False
                            except:
                                pass
                        if grav_swimming is True and swim_dir_g == "down":
                            try:
                                spectrum = hdul[1].data["{}".format(grav_func(grav_in-j))]
                                #print("Found grav after swimming {} miles in grav".format(j/0.5))
                                grav_out = grav_in-j
                                grav_swimming = False
                            except:
                                pass
                        j+=0.5
            except:
                pass

        if temp_swimming is True and swim_dir_t == "down":
            try:
                with fits.open("fits_library/ck{}/ck{}_{}.fits".format(metal_func(metal_in), metal_func(metal_in),temp_func(temp_in-i))) as hdul:
                    #print("Found temp after swimming down {} miles in temp".format(i/250))
                    temp_out = temp_in-i
                    temp_swimming = False
                    while grav_swimming is True:
                        if grav_swimming is True and swim_dir_g == "up":
                            try:
                                spectrum = hdul[1].data["{}".format(grav_func(grav_in+j))]
                                #print("Found grav after swimming {} miles in grav".format(j/0.5))
                                grav_out = grav_in+j
                                grav_swimming = False
                            except:
                                pass
                        if grav_swimming is True and swim_dir_g == "down":
                            try:
                                spectrum = hdul[1].data["{}".format(grav_func(grav_in-j))]
                                #print("Found grav after swimming {} miles in grav".format(j/0.5))
                                grav_out = grav_in-j
                                grav_swimming = False
                            except:
                                pass
                        j+=0.5
            except:
                pass

        i += 250

    return spectrum,grav_out,temp_out

####

spec_ml_tl_gl,g_mltlgl,t_mltlgl = search_for_corner(metal_lo_str,metal_lo,temp_lo_str,temp_lo,grav_lo_str,grav_lo, "corner mltlgl","down","down")
spec_ml_tl_gh,g_mltlgh,t_mltlgh = search_for_corner(metal_lo_str,metal_lo,temp_lo_str,temp_lo,grav_hi_str,grav_hi, "corner mltlgh","down","up")
spec_ml_th_gl,g_mlthgl,t_mlthgl = search_for_corner(metal_lo_str,metal_lo,temp_hi_str,temp_hi,grav_lo_str,grav_lo, "corner mlthgl","up","down")
spec_ml_th_gh,g_mlthgh,t_mlthgh = search_for_corner(metal_lo_str,metal_lo,temp_hi_str,temp_hi,grav_hi_str,grav_hi, "corner mlthgh","up","up")
spec_mh_tl_gl,g_mhtlgl,t_mhtlgl = search_for_corner(metal_hi_str,metal_hi,temp_lo_str,temp_lo,grav_lo_str,grav_lo, "corner mhtlgl","down","down")
spec_mh_tl_gh,g_mhtlgh,t_mhtlgh = search_for_corner(metal_hi_str,metal_hi,temp_lo_str,temp_lo,grav_hi_str,grav_hi, "corner mhtlgh","down","up")
spec_mh_th_gl,g_mhthgl,t_mhthgl = search_for_corner(metal_hi_str,metal_hi,temp_hi_str,temp_hi,grav_lo_str,grav_lo, "corner mhthgl","up","down")
spec_mh_th_gh,g_mhthgh,t_mhthgh = search_for_corner(metal_hi_str,metal_hi,temp_hi_str,temp_hi,grav_hi_str,grav_hi, "corner mhthgh","up","up")

#### DEBUG ROUTINE

if g_mltlgl == g_mlthgl == g_mhtlgl == g_mhthgl:
    #print("lower g consistent")
    #print(g_mltlgl," ",g_mlthgl," ",g_mhtlgl," ",g_mhthgl)
    grav_lo_consistent = True
else:
    #print("lower g not consistent")
    #print(g_mltlgl," ",g_mlthgl," ",g_mhtlgl," ",g_mhthgl)
    grav_lo_consistent = False

if g_mltlgh == g_mlthgh == g_mhtlgh == g_mhthgh:
    #print("upper g consistent")
    #print(g_mltlgh," ",g_mlthgh," ",g_mhtlgh," ",g_mhthgh)
    grav_hi_consistent = True
else:
    #print("upper g not consistent")
    #print(g_mltlgh," ",g_mlthgh," ",g_mhtlgh," ",g_mhthgh)
    grav_hi_consistent = False

if t_mltlgl == t_mltlgh == t_mhtlgl == t_mhtlgh:
    #print("lower t consistent")
    #print(t_mltlgl," ",t_mltlgh," ",t_mhtlgl," ",t_mhtlgh)
    temp_lo_consistent = True
else:
    #print("lower t not consistent")
    #print(t_mltlgl," ",t_mltlgh," ",t_mhtlgl," ",t_mhtlgh)
    temp_lo_consistent = False

if t_mlthgl == t_mlthgh == t_mhthgl == t_mhthgh:
    #print("upper t consistent")
    #print(t_mlthgl," ",t_mlthgh," ",t_mhthgl," ",t_mhthgh)
    temp_hi_consistent = True
else:
    #print("upper t not consistent")
    #print(t_mlthgl," ",t_mlthgh," ",t_mhthgl," ",t_mhthgh)
    temp_hi_consistent = False

####
if grav_lo_consistent == True:
    grav_lo_N = g_mltlgl
else:
    quit()

if grav_hi_consistent == True:
    grav_hi_N = g_mltlgh
else:
    quit()

if temp_lo_consistent == True:
    temp_lo_N = t_mltlgl
else:
    quit()

if temp_hi_consistent == True:
    temp_hi_N = t_mlthgl
else:
    quit()

grav,metal,temp,metal_lo,metal_hi,interp_par = grav,metal,temp,metal_lo,metal_hi,interp_par

swim_dict = {"{},{},{}".format(grav_lo,temp_lo,metal_lo):"{},{},{}".format(g_mltlgl,t_mltlgl,metal_lo),
             "{},{},{}".format(grav_hi,temp_lo,metal_lo):"{},{},{}".format(g_mltlgh,t_mltlgh,metal_lo),
             "{},{},{}".format(grav_lo,temp_hi,metal_lo):"{},{},{}".format(g_mlthgl,t_mlthgl,metal_lo),
             "{},{},{}".format(grav_hi,temp_hi,metal_lo):"{},{},{}".format(g_mlthgh,t_mlthgh,metal_lo),
             "{},{},{}".format(grav_lo,temp_lo,metal_hi):"{},{},{}".format(g_mhtlgl,t_mhtlgl,metal_hi),
             "{},{},{}".format(grav_hi,temp_lo,metal_hi):"{},{},{}".format(g_mhtlgh,t_mhtlgh,metal_hi),
             "{},{},{}".format(grav_lo,temp_hi,metal_hi):"{},{},{}".format(g_mhthgl,t_mhthgl,metal_hi),
             "{},{},{}".format(grav_hi,temp_hi,metal_hi):"{},{},{}".format(g_mhthgh,t_mhthgh,metal_hi)}
import numpy as np
from astropy.io import fits
import csv

from spectrum_finder.calculations.interpolate import final_wave_list,grav,temp,metal,interp_par

with fits.open("fits_library/ckm05/ckm05_3500.fits") as hdul:
    wavelabels = hdul[1].data["WAVELENGTH"]

outputarray = np.array([wavelabels,final_wave_list])

with open("output_g{}_t{},_a{}_{}.csv".format(grav,temp,metal,interp_par),"w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["WAVELENGTH","FLUX"])

with open("output_g{}_t{},_a{}_{}.csv".format(grav,temp,metal,interp_par),"a", newline="") as f:
    writer = csv.writer(f)
    for row in outputarray.T:
        writer.writerow(row)

import gui2

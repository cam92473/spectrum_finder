import xarray as xr
import numpy as np
import scipy
from spectrum_finder.calculations.search import spec_ml_tl_gl,spec_ml_tl_gh,spec_ml_th_gl,spec_ml_th_gh,spec_mh_tl_gl,spec_mh_tl_gh,spec_mh_th_gl,spec_mh_th_gh,grav,temp,metal,grav_lo_N,grav_hi_N,temp_lo_N,temp_hi_N,metal_lo,metal_hi,interp_par



spectra_array = np.array([spec_ml_tl_gl,spec_ml_tl_gh,spec_ml_th_gl,spec_ml_th_gh,spec_mh_tl_gl,spec_mh_tl_gh,spec_mh_th_gl,spec_mh_th_gh])
#print("Spectra Array: ",spectra_array)

wavecubes = spectra_array.T
#print("Wavecubes: ",wavecubes)

def data_array_builder(wc,metal_lo,metal_hi,temp_lo_N,temp_hi_N,grav_lo_N,grav_hi_N,metal,temp,grav,interp_par):

    final_wave_list=[]

    for i in range(0,wc.shape[0]):
        cubedata = np.array([[[wc[i][0],wc[i][1]],[wc[i][2],wc[i][3]]],[[wc[i][4],wc[i][5]],[wc[i][6],wc[i][7]]]])
        da = xr.DataArray(cubedata,[("abundance_ratio", [metal_lo,metal_hi]),("temperature", [temp_lo_N,temp_hi_N]),
                                    ("log_of_surface_gravity", [grav_lo_N,grav_hi_N])])

        interpolated = da.interp(abundance_ratio = metal, temperature = temp, log_of_surface_gravity = grav, method = interp_par)

        #print("INTERPOLATED row {}: {}".format(i,interpolated))

        final_wave_list.append(float(interpolated.data))

    return(final_wave_list)

final_wave_list = data_array_builder(wavecubes,metal_lo,metal_hi,temp_lo_N,temp_hi_N,grav_lo_N,grav_hi_N,metal,temp,grav,interp_par)
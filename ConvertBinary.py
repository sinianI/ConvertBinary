import numpy as np
import flopy

print("Running ConvertBinary!")
# open the binary file
fpth = 'model.sbs'
sobj = flopy.utils.HeadFile(fpth, text='Z DISPLACEMENT')

# get all of the available times in the file
times = sobj.get_times()

# layer number
nlay=1

# all vertical displacement data from the binary file
zd = sobj.get_alldata(mflay=0)

# save the z-displacement for the first layer (layer 0) to an ascii file
# zd is a 3D numpy array with a shape of (nlay, nrow, ncol)
# since np.savetxt choke on > 2D array, so we slice the  3D array into 2D

with open('sub.txt', 'w') as outfile:
    for slice_2d in zd:
        np.savetxt(outfile, slice_2d)

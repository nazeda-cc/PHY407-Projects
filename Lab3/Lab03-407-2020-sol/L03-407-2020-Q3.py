# Answer to Q3, Lab 03, PHY407, 2018
# Author: Nicolas Grisouard, University of Toronto
# Timing the mulitiplication of two matrices with two different methods

import matplotlib.pyplot as plt
import numpy as np
import struct  # for reading binary files

# %% Q3a: pseudo-code --------------------------------------------------------|
# import struct and other relevant modules

# define npt = 1201, number of cells in each direction and illumination angle
# and h = 420 m.
# open file
# create empty array of values, NxN: w = empty(npt, npt)
# for each latitude (row)
#  for each longitude (column)
#   read two bytes from file: f.read(2)
#   use struct to unpack those two bytes into the next value of val, for this
#   longitude.
#   remember that the latitude values are written from north to south, but that
#   the actual latitude goes from South to North => read latitudes backward

# Loops to calculate gradients using central differences for interior points
# fx[1:-1] = (f[i+1]-f[i-1])/2h
# fy[1:-1] = (f[j+1]-f[j-1])/2h
# Use forward difference for Southern and Western boundaries.
# dfdx[0]=(f[1]-f[0])/h, similarly for dfdy
# Use backward difference for Northern and Eastern boundaries.

# Calculate intensity I using formula from Lab.
# Plot map of elevation
# Plot relief map.
# Plot dwdx at the E and W border, as well as the first interior points. If
# they are close, that the borders are treated correctly.
# Same for dwdy

# %% Load the file -----------------------------------------------------------|
h = 83.  # the grid spacing in m. Nice number!
phi = np.pi/6  # where Sun shines from; 0 is from W, pi/2 from S, pi from E

# loading the elevations file
npt = 1201  # number of points in each direction
w = np.empty((npt, npt))   # elevations to be filled
fid = open('N46E006.hgt', 'rb')


for lat in range(npt):  # the index from northernmost to southernmost
    for lon in range(npt):  # the index from westernmost to easternmost
        buf = fid.read(2)  # read two bytes
        w[lon, npt - 1 - lat] = struct.unpack('>h', buf)[0]
# Note: what I did above is not very cautious. There is no test, and I
# completely trust that the format of the files will always be the same,
# without errors.

plt.figure(1)
cbax = plt.imshow(w.T, vmin=373., vmax=3000., cmap='gist_earth',
                  aspect='equal', origin='lower', extent=[6, 7, 46, 47])
plt.xlabel('longitude ($^\circ$E)')
plt.ylabel('latitude ($^\circ$N)')
plt.colorbar(cbax)
plt.title('Elevation above sea level (in m)')
plt.savefig('Elevation.png', dpi=150)

# %% Compute slopes ----------------------------------------------------------|
dwdx = 0*w
dwdy = 0*w

# first, we do the western- and eastern-most x-slopes
for lat in range(npt):  # we scan from N to S
    dwdx[0, lat] = (w[1, lat] - w[0, lat])/h  # fwd diff for W-most column
    dwdx[-1, lat] = (w[-1, lat] - w[-2, lat])/h  # bwd diff for E-most column

# then, we do the northern- and southern-most y-slopes
for lon in range(npt):  # we scan from W to E
    dwdy[lon, 0] = (w[lon, 1] - w[lon, 0])/h  # fwd diff for S-most row
    dwdy[lon, -1] = (w[lon, -1] - w[lon, -2])/h  # bwd diff for N-most row

# then, we do the x-slopes for interior points with central differences
for lat in range(1, npt-1):  # S to N scan
    for lon in range(1, npt-1):  # W to E scan
        dwdy[lon, lat] = (w[lon, lat+1] - w[lon, lat-1])/(2*h)
        dwdx[lon, lat] = (w[lon+1, lat] - w[lon-1, lat])/(2*h)

# Finally, we compute the intensity
II = (np.cos(phi)*dwdx + np.sin(phi)*dwdy)/np.sqrt(dwdx**2 + dwdy**2 + 1)

Imax = 0.03
plt.figure(2)  # poltting the light intensity
plt.imshow(II.T, aspect='equal', cmap='gray', vmin=-Imax,
           vmax=Imax, origin='lower', extent=[6, 7, 46, 47])
plt.title('Light intensity')
plt.xlabel('longitude ($^\circ$E)')
plt.ylabel('latitude ($^\circ$N)')
plt.savefig('Light.png', dpi=150)

plt.figure(3)  # check that dwdx is correct
cbax3 = plt.imshow(dwdx.T, aspect='equal', cmap='gray', vmin=-
                   Imax, vmax=Imax, origin='lower', extent=[6, 7, 46, 47])
plt.colorbar(cbax3)
plt.title('$\partial w/\partial x$')
plt.xlabel('longitude ($^\circ$E)')
plt.ylabel('latitude ($^\circ$N)')
plt.savefig('dwdx.png', dpi=150)

plt.figure(4)  # check that dwdy is correct
cbax4 = plt.imshow(dwdy.T, aspect='equal', cmap='gray', vmin=-
                   Imax, vmax=Imax, origin='lower', extent=[6, 7, 46, 47])
plt.colorbar(cbax4)
plt.title('$\partial w/\partial y$')
plt.xlabel('longitude ($^\circ$E)')
plt.ylabel('latitude ($^\circ$N)')
plt.savefig('dwdy.png', dpi=150)

plt.figure(5)  # checks about borders
plt.subplot(221)
plt.plot(dwdy[:, 0])
plt.plot(dwdy[:, 1])
plt.title('$\partial w/\partial y$ along the S border')
plt.subplot(222)
plt.plot(dwdy[:, -1])
plt.plot(dwdy[:, -2])
plt.title('$\partial w/\partial y$ along the N border')
plt.subplot(223)
plt.plot(dwdx[0, :])
plt.plot(dwdx[1, :])
plt.title('$\partial w/\partial x$ along the W border')
plt.xlabel('index')
plt.subplot(224)
plt.plot(dwdx[-1, :])
plt.plot(dwdx[-2, :])
plt.title('$\partial w/\partial x$ along the E border')
plt.xlabel('index')


plt.tight_layout()
plt.savefig('check_borders.png', dpi=150)

CERN_lon = 6 + 3./60 + 17./3600  # longitude 06o03'17"
CERN_lat = 46 + 14./60 + 0./3600  # longitude 46o14'00"

print(CERN_lon, CERN_lat)

plt.figure(6)  # zoom around city of Geneva
plt.imshow(II[:300, 120:420].T, aspect='equal',
           cmap='gray', vmin=-Imax, vmax=Imax, origin='lower',
           extent=[6, 6.25, 46.1, 46.35])
plt.plot(CERN_lon, CERN_lat, 'r+')
plt.annotate('CERN', xy=(CERN_lon, CERN_lat),
             xytext=(CERN_lon+0.02, CERN_lat+0.02),
             arrowprops={'arrowstyle': '->', 'color': 'r'},
             color='r', fontsize=14)
plt.xlabel('longitude ($^\circ$E)')
plt.ylabel('latitude ($^\circ$N)')
plt.title("City of Geneva")
plt.savefig('Geneva.png', dpi=150)

# plt.figure()
# plt.hist(II)

plt.show()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize
from pycbc.detector import Detector
from astropy.time import Time
import cartopy.crs as ccrs
import cartopy.util as cutil

def plot_antenna_pattern(detector_name):

    # need a GPS time for reference, but it's factored out in the end --- 
    # results should be independent of this.
    GPS = 1736267618

    nlon = 120
    nlat = 60
    lon_degrees = np.linspace(0, 360., nlon)
    lat_degrees = np.linspace(-90., 90., nlat)

    lon = np.deg2rad(lon_degrees)
    lat = np.deg2rad(lat_degrees)

    lon2d, lat2d = np.meshgrid(lon, lat)

    det = Detector(detector_name)
    ra = det.gmst_estimate(GPS) + lon2d

    fplus = np.zeros_like(lat2d)
    fcross = np.zeros_like(lat2d)
    for (i, j), value in np.ndenumerate(ra):
        fplus[i, j], fcross[i, j] = det.antenna_pattern(ra[i, j], lat2d[i, j], 0, GPS)

    fmean = np.sqrt(fplus**2 + fcross**2)

    fig = plt.figure(figsize=(10, 5))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.Mollweide())
    ax.set_global()
    ax.coastlines()

    cmap = plt.get_cmap('inferno')
    normalization = Normalize(0., 1.)
    mappable = ax.contourf(
        lon_degrees, 
        lat_degrees, 
        fmean, 
        cmap = cmap,
        levels=50,
        norm=normalization,
        transform = ccrs.PlateCarree(),
    )

    plt.colorbar(
        ScalarMappable(cmap=cmap, norm=normalization), 
        ax=ax,
        label='$\\sqrt{F_{+}^2+F_{\\times}^2}$')
    
    # uncomment to overplot a star corresponding to the detector location
    # ax.scatter(np.rad2deg(det.longitude), np.rad2deg(det.latitude), c='blue', marker='*', s=400, transform=ccrs.PlateCarree())
    
    plt.show()
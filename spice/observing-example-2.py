import numpy as np
#import matplotlib.pyplot as plt
from astropy import units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz# get_sun
import pdb
#supress the warning about vector transforms so as not to clutter the doc build log
import warnings
warnings.filterwarnings('ignore',module='astropy.coordinates.baseframe')

m33 = SkyCoord(ra=23.4621*u.deg, dec=30.6599417*u.deg) # same as SkyCoord.from_name('M33'): use the explicit coordinates to allow building doc plots w/o internet
bear_mountain = EarthLocation(lat=41.3*u.deg, lon=-74*u.deg, height=390*u.m)
utcoffset = -4*u.hour  # Eastern Daylight Time
midnight = Time('2012-7-13 00:00:00') #- utcoffset

delta_midnight =midnight #np.linspace(-12, 12, 1000)*u.hour
times = midnight #+ delta_midnight
#pdb.set_trace()
altazframe = AltAz(obstime=times, location=bear_mountain)
#sunaltazs = get_sun(times).transform_to(altazframe)
m33altazs = m33.transform_to(altazframe)
pdb.set_trace()

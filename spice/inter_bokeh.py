#!/usr/bin/python
import numpy as np
import SpiceyPy as spi
import datetime
import time
import pdb
import os
#Imports from bokeh
from bokeh.models import HoverTool
from bokeh.plotting import figure, output_file, show
#Import from astropy
from astropy import units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz#, get_sun
import warnings
warnings.filterwarnings('ignore',module='astropy.coordinates.baseframe')

def main():
	neo="2000433.bsp"
        N=200
	ini="Apr 24 2016 0:00:00"
	fin="Apr 25 2016 0:00:00"
        ALT=390	
	LAT=40.123
	LONG=-3.70
        obser=EarthLocation(lat=LAT*u.deg,lon=LONG*u.deg,height=ALT*u.m)
#===================================================
        epoch2000=datetime.datetime.strptime("01-01-2000 00:00","%d-%m-%Y %H:%M")
        epoch2000=time.mktime(epoch2000.timetuple())
#===================================================
	spi.kclear() 
	spi.furnsh("./meta.fgl")
	spi.furnsh("./../kernels/neos/"+neo)
	tiempos=spi.str2et([ini,fin])
	tiempos=np.linspace(tiempos[0],tiempos[1],N) 
	alt_list=list()
        times_list=list()
        for k in tiempos:
		temp=spi.spkez(int(neo.split(".")[0]),k,"J2000","LT+S",399)
                temp2=spi.recrad(temp[0][0:3])
		ar=(temp2[1]*(180/np.pi))
		dec=(temp2[2]*(180/np.pi))
                aux=datetime.datetime.utcfromtimestamp(k+epoch2000)
                fechas_aux=((str(aux.year)+"-"+str(aux.month).zfill(2)+"-"+str(aux.day).zfill(2)+" "+str(aux.hour).zfill(2)+":"+str(aux.minute).zfill(2)+":"+str(aux.second).zfill(2)+"."+str(aux.microsecond)))
                times_list.append(aux)
                fechas_aux=Time(fechas_aux)
                frames_loc=AltAz(obstime=fechas_aux,location=obser)
                #pdb.set_trace()
                alt_list.append((SkyCoord(ra=ar*u.deg,dec=dec*u.deg,frame='icrs')).transform_to(frames_loc).alt.value)

        #pdb.set_trace()
        
	output_file("spice.html",title="NEO SOURCE")
        p=figure(title="NEO Visual",x_axis_label="Time",tools="pan,box_zoom,reset,save,hover",y_axis_label="Elevation (deg)")
	p.line(times_list,alt_list,legend=neo)
        hover=p.select_one(HoverTool)
        hover.point_policy="follow_mouse"

	show(p)

	

if __name__=="__main__":
	main()

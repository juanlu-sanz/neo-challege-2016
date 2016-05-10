#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np
import SpiceyPy as spi
import pdb
from mpl_toolkits.mplot3d import Axes3D
import datetime

def main():
	antes=datetime.datetime.now()
	N=100 #Precision 
	spi.kclear() #Limpiamos el pool de los kernels.
	#MetaKernel con los datos.
	spi.furnsh("./meta.fgl")
	#tiempos=spi.str2et(["Jun 20 2004","Dec 1, 2005"])
	ini="Apr 20 2016 0:00:00"
	fin="Apr 20 2017 0:00:00"
	
	tiempos=spi.str2et([ini,fin])
	
	tiempos=np.linspace(tiempos[0],tiempos[1],N) 
	#tiempos=spi.str2et(["Apr 20 2016 0:00:00"])
	#pdb.set_trace()		
	#pdb.set_trace() #Esto es lo mas fino que he llegado: 
	#try:
	a=list()
	#Chapuza metida tras sacar velocidad
	#=====================================
	x=list()
	y=list()
	z=list()
	dx=list()
	dy=list()
	dz=list()
	#=============
	#Test para spaceapps
	#colat=list()
	#longi=list()
	#radio=list()
	ar=list()
	dec=list()
	radio=list()
	ayuda=list()
	#Test para spaceapps (end)
	for k in tiempos:
		#temp=spi.spkez(2000433,k,"IAU_EARTH","LT+S",399)
		temp=spi.spkez(2000433,k,"J2000","LT+S",399)
		#temp2=spi.xfmsta(temp[0],'RECTANGULAR','SPHERICAL',399)
		temp2=spi.recrad(temp[0][0:3])

		#radio.append(temp2[0])
		#colat.append(temp2[1])
		#longi.append(temp2[2])
		radio.append(temp2[0])
		ayuda.append(temp2)
		ar.append(temp2[1]*(180/np.pi))
		dec.append(temp2[2]*(180/np.pi))
		x.append(temp[0][0]) #Este ya devuelve el vector completo
		y.append(temp[0][1])
		z.append(temp[0][2])		
		dx.append(temp[0][3]) #Este ya devuelve el vector completo
		dy.append(temp[0][4])
		dz.append(temp[0][5])
		
	despues=datetime.datetime.now()
	
	#spi.xfmtsta(temp[0],'RECTANGULAR','SPHERICAL',399)
	pdb.set_trace() # despues-antes
	x=np.array(x)
	y=np.array(y)
	z=np.array(z)
	dx=np.array(dx)
	dy=np.array(dy)
	dz=np.array(dz)
	mdscc=station(0)
	#===========================	====	
	print "Geocentric position for MDSCC:"	
	print "----------------------------------"
	print mdscc
	print "----------------------------------"
	if False:
		a=np.array(a)
		x=list()
		y=list()
		z=list()
		for k in a[0]:
			x.append(k[0])
			y.append(k[1])
			z.append(k[2])

	#Tenia el dato referedio al centro de masas de la Tierra. Ahora lo refiero a MDSCC.
	x=x-mdscc[0]
	y=y-mdscc[1]
	z=z-mdscc[2]

	#data2=list()	
	#for k in range(len(x)):
	#	data2.append(spi.recrad([x[k],y[k],z[k]]))
	#data2=np.array(data2)
	pdb.set_trace()
	plt.figure()
	plt.subplot(211)
	plt.plot(x,y)
	plt.xlabel("x [Km]")
	plt.ylabel("y [Km]")
	plt.subplot(212)
	plt.plot(y,z)
	plt.xlabel("y Km")
	plt.ylabel("z Km")
	plt.figure()
	plt.plot(dist(dx,dy,dz))
	frase="Relative speed as seen from Robledo to Eros from %s to %s"%(ini,fin)
	plt.title(frase)
	plt.ylabel("Kilometers")
	plt.xlabel("Samples")
	plt.grid()
	fig=plt.figure()
	ax=fig.add_subplot(111,projection='3d')
	frase="Distance from Eros to Robledo. Starting: %s End: %s"%(ini,fin)
	ax.plot(x,y,z,label=frase)
	plt.legend()
	plt.show()

def station(dat):
	if dat==0: #Robledo
		longi=4+(14/60)+(53/3600) #W (-1)
		lati=40+(25/60)+(54/3600) #N
		longi= -longi*(np.pi/180)
		lati=lati*(np.pi/180)
		alti=720/1000 #Va con Km
		# Datos de WGS84:
		#=====================================
		RE= 6378137.0/1000#Semieje mayor
		f=1/298.257223563 #Achatamiento Tierra
		#=====================================
	return spi.georec(longi,lati,alti,RE,f)
	
		

def dist(x,y,z):
	x=np.array(x)
	y=np.array(y)
	z=np.array(z)
	return np.sqrt((x**2)+(y**2)+(z**2))
if __name__=="__main__":	
	main()

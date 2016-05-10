#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np
import SpiceyPy as spi
import pdb
from mpl_toolkits.mplot3d import Axes3D

def main():
	N=1000#1000 #Precision 
	spi.kclear() #Limpiamos el pool de los kernels.
	#MetaKernel con los datos.
	spi.furnsh("./meta.fgl")
	#tiempos=spi.str2et(["Jun 20 2004","Dec 1, 2005"])
	tiempos=spi.str2et(["Jun 20 2004","Feb 1, 2005"])	
	tiempos=np.linspace(tiempos[0],tiempos[1],N) 

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
	for k in tiempos:
		#temp=spi.spkez(-82,k,"IAU_EARTH","None",399)
		temp=spi.spkez(2000433,k,"IAU_EARTH","None",399)
		x.append(temp[0][0]) #Este ya devuelve el vector completo
		y.append(temp[0][1])
		z.append(temp[0][2])		
		dx.append(temp[0][3]) #Este ya devuelve el vector completo
		dy.append(temp[0][4])
		dz.append(temp[0][5])

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
	plt.title("Relative speed as seen from Robledo to Eros")
	plt.ylabel("Kilometers")
	plt.xlabel("Samples")
	plt.grid()
	fig=plt.figure()
	ax=fig.add_subplot(111,projection='3d')
	ax.plot(x,y,z,label="Eros to Robledo de Chavela")
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

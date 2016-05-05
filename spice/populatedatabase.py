#!/usr/bin/python
import numpy as np
import SpiceyPy as spi
import datetime
import pdb
import os
from pymongo import MongoClient
import datetime
import time

def main():
        client=MongoClient('server')
        client.neodb.authenticate('user','password',mechanism='SCRAM-SHA-1')
        db=client.neodb

	for root,folders,files in os.walk("./kernels/neos/"):
		for p in files:
			calc_spice("Apr 24 2016 0:00:00","Jun 20 2016 0:00:00",p,2880,db)




def calc_spice(initi,final,neo,puntos,db):
	N=puntos#2880 #Precision 
	spi.kclear() #Limpiamos el pool de los kernels.
	#MetaKernel con los datos genericos menos el neo.
	spi.furnsh("./meta.fgl")
	spi.furnsh("./kernels/neos/"+neo)
	#tiempos=spi.str2et(["Jun 20 2004","Dec 1, 2005"])
	ini=initi#"Apr 24 2016 0:00:00"
	fin=final#"Jun 20 2016 0:00:00"
        #Fran: It would be better to directly put the number of seconds of J2000 instead of this shit...
        epoch2000=datetime.datetime.strptime("01-01-2000 00:00","%d-%m-%Y %H:%M")
	epoch2000=time.mktime(epoch2000.timetuple())
        tiempos=spi.str2et([ini,fin])
	tiempos=np.linspace(tiempos[0],tiempos[1],N) 
	ar=list()
	dec=list()
        #pdb.set_trace()
	for k in tiempos:
		temp=spi.spkez(int(neo.split(".")[0]),k,"J2000","LT+S",399)
                temp2=spi.recrad(temp[0][0:3])
		ar.append(temp2[1]*(180/np.pi))
		dec.append(temp2[2]*(180/np.pi))
        for k in range(len(tiempos)):
            document={"spkid":neo.split(".")[0],"name":neo.split(".")[0],"ra":ar[k],"dec":dec[k],"date":datetime.datetime.fromtimestamp(int(tiempos[k])+epoch2000)}
            day=str(document["date"].day).zfill(2)+str(document["date"].month).zfill(2)+str(document["date"].year)
            day="d"+day
            exec("db.%s.insert_one(document)"%day)
            #print "procesado %s en %s"%(neo,day)
if __name__=="__main__":	
	main()

from flask import Flask
from flask.ext.cors import CORS
from flask import request
from pymongo import MongoClient
import json
import numpy as np
import dateutil.parser
from astropy.coordinates import SkyCoord
from astropy.coordinates import EarthLocation
from astropy.coordinates import AltAz
from astropy.time import Time
import datetime
import time
import SpiceyPy as spi
import pdb
import ephem
import math
from OpenSSL import SSL
from bokeh.models import HoverTool
from bokeh.plotting import figure, output_file, show


app = Flask(__name__)
CORS(app)

# Methods below


@app.route("/")
def hello(): 
    data = {"api": "rest :)"}

    return json.dumps(data)


@app.route('/visible', methods=['GET'])
def get_visible_neos(): 
    start_date = request.args.get('start')
    lat = request.args.get('lat')
    lon = request.args.get('lon')

    dateobject = dateutil.parser.parse(start_date)

    colname = 'd' + dateobject.date().strftime('%d%m%Y')

    client = MongoClient('host','port')
    client.neodb.authenticate('user', 'password', mechanism='SCRAM-SHA-1')

    db = client.neodb
    
    pipeline = [{'$project': {'_id': 0, 'name': 1, 'spkid': 1, 'ra': 1, 'dec': 1}}, {'$match': {'ra': {'$gt': 358}}}, {'$group': {'_id':  {'spkid': '$spkid'}, 'name': {'$addToSet': '$name'}}}]
    
    return json.dumps(list(db[colname].aggregate(pipeline)))

@app.route('/details',methods=['GET'])
def inter_bokeh():
    epoch2000=datetime.datetime.strptime("01-01-2000 00:00","%d-%m-%Y %H:%M")
    epoch2000=time.mktime(epoch2000.timetuple())
    lat=request.args.get('lat')
    long=request.args.get('lon')
    spkid=request.args.get('spkid')
    inicio=request.args.get('start')
    neo=spkid+".bsp"
    N=200
    spi.kclear()
    spi.furnsh("/home/cristobal/horizons_iterface/github/neo-challege-2016/spice/meta.fgl")
    spi.furnsh("/home/cristobal/horizons_iterface/github/neo-challege-2016/spice/kernels/neos/"+neo)
    inicio=inicio.replace("Z","").replace("T"," ")
    final= dateutil.parser.parse(inicio)+datetime.timedelta(days=0.5)
    final=str(final.year)+"-"+str(final.month).zfill(2)+"-"+str(final.day).zfill(2)+" "+str(final.hour).zfill(2)+":"+str(final.minute).zfill(2)+":"+str(final.second).zfill(2)+"."+str(final.microsecond)
    tiempos=spi.str2et([inicio,final])
    tiempos=np.linspace(tiempos[0],tiempos[1],N)
    ar=list()
    dec=list()
    times_list=list()
    for k in tiempos:
            temp=spi.spkez(int(neo.split(".")[0]),k,"J2000","LT+S",399)
            temp2=spi.recrad(temp[0][0:3])
            ar.append(temp2[1]*(180/np.pi))
            dec.append(temp2[2]*(180/np.pi))
            times_list.append(datetime.datetime.utcfromtimestamp(k+epoch2000))
    [altura,times_list]=conversion(ar,dec,times_list,lat,long)
    json.dumps(altura)
    bokeh_pinta(altura,list,neo)
    return app.send_static_file('spice.html')

def bokeh_pinta(alt_list,times_list,neo):
    neo=neo.split(".")[0]
    #pdb.set_trace()
    output_file("spice.html",title="NEO SOURCE")
    p=figure(title="NEO Visual",x_axis_label="Time",tools="pan,box_zoom,reset,save,hover")
    p.line(range(len(alt_list)),alt_list,legend=neo)
    hover=p.select_one(HoverTool)
    hover.point_policy="follow_mouse"
    try:
        show(p)
    except:
        pass




def conversion(ar,dec,times_list,lat,lon):
    lat=float(lat)
    lon=float(lon)
    obs=ephem.Observer()
    obs.long=lon
    alt=list()
    #pdb.set_trace()
    for k in range(len(times_list)):
        obs.date=times_list[k]#dateutil.parser.parse(times_list[k])
        LST=math.degrees(obs.sidereal_time())
        HA = ar[k] - LST
        x = math.cos(HA) * math.cos(dec[k])
        y = math.sin(HA) * math.cos(dec[k])
        z = math.sin(dec[k])
        zhor = x * math.sin(90 - lat) + z * math.cos(90 - lat)
        alt.append(math.asin(zhor))
    return [alt,times_list]






if __name__ == "__main__":
    context = ('cert.pem', 'privkey.pem')
    app.run(host='0.0.0.0', debug=True, port=8888, ssl_context=context)


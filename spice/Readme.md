## How to obtain the NEO binary Kernels of all NEOS

ObtenIDs.py will download all the SPK Kernels from the NEOs SPKIDs in NEO_results.csv (from small bodies DB) in ./kernels/neos 
(YOU SHOULD CREATE THE FOLDER!, we deleted it and the current content as it did not make sense to upload the current 14K Binary SPKs).

## How to populate the database after running ObtenIDs.py

populatedatabase.py will populate the mongodb database (you should create the database yourself and change the 'user','url' and 'password' properly)

## How allow NEOFIT to update its dabases on a frequent basis:

Both python programs (ObtenIDs.py and populatedatabase.py) should be included in the Crontab of your system.

## Rest API

Rest api will provide with a REST API that will interact with BOKEH and SPICE.
Don't forget to keep running restapi.py in order to provide the web system with the JPL SPICE NEO results.

## NEOs SPKID

As for now if you want to have all new NEO you should download from the JPL Small Bodies database a CSV with the SPKID in the first column and overwrite the current file. 
You may want to put that into a script and added it to the crontab.

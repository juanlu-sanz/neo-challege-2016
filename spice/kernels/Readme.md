
## NEOs SPK folder

A folder called "neos" should be created here:This folder will be populated everytime "obtenIDs.py" is run (crontab in order to populate it 
on a frequent basis).
It will read NEO_results.csv (extracted from small bodies DB) first column and then download the SPKs from Horizons for the 
60 days time span 
####(BTW: we reduced the time window a couple of days becuase we found a bug in the Spice version we used).

## What is the content of this folder

This folder contains Leap seconds kernels (tls), Earth binary kernels and so on (Some Cassini spacecraft kernels are there, but are not necessary for NEOFIT). An automatic script should be run to update this data in order to provide users with accurate results. 


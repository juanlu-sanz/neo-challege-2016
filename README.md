# NEO Challenge 2016: NEOFIT


## Intro

Say you feel like going stargazing (I mean, who doesn't) and feel a bit curious about Near Earth Objects... they are so close... they must be easy to see!. You get your trusty telescope, jacket and get ready to leave for the mountains, only to realize that since they are so close, they also happen to move so much faster! how are you going to pinpoint their location?
Here is where NEOFIT comes in! We have developed a tool just for that. You'd just have to input your current location (on this planet!) and the date you are going stargazing. We will then show you all the NEOs that are visible in your local sky and if you choose to select one we will show you all sorts of information about that specific one: magnitude, apparent size, range and radial speed (among others!)

Now you know everything about your skies and are ready to go! the day (well, night) is saved!

## KEY FEATURES
  Exhaustive list of visible NEOs from a given position and time span, including all available information about each object.
 
  Professional quality: thanks to the accuracy of the JPL Spice calculations, the user will know exactly where and when to point the telescope.
  
  Automatic object detection in images: the PCA algorithm calculates the base image from a set of pictures and then looks for high variance values (i.e: moving sources).
  
  False positive rejection, by matching the results with known sources (e.g: SIMBAD catalog) and man made spacecrafts (e.g: satellites, ISS... (from NORAD & UCS DDBB))
  
  Final NEO Identification: By means of the NEOFIT internal database (SPICE detailed simulation results) the resulting NEO candidates in the astronomical images are matched with the NASA Identified NEOs
  
### HOW DOES IT WORK?

Our application supports amateur and professional astronomers while observing NEOs including results analysis based on data mining dimensionality reduction methods.

An embedded JPL SPICE core performs the necessary high accuracy calculations on the NEO orbits for the requested time span and provides the astronomer with elevation curves of the visible NEOs at any observatory on Earth for the user requested timestamp. It also provides the user with a list of visible NEOs at that observatory for a particular date. This helps a lot during the observation planning.

In order to provide users with this tailored data a MongoDB database is populated with coarse Spice simulation results with a sliding window of 60 days. On a frequent basis the system automatically retrieves from the JPL small body database a list of detected NEOs and retrieves all the binary Spice kernels to perform the necessary high accuracy calculations. Thanks to the embedded Spice Kernel we can provide users with high accuracy data with great level of detail (eg: AR,DEC,AZ,EL, Range and Radial speed between the observer and the NEO, among many others). Astronomical optical aberration is of course taken into account by the system.

The second part of the system allows the user to upload astrometric calibrated data (in FITs format). Then a PCA algorithm is applied to the image sequence allowing discarding those elements without remarkable proper motion (in fast processing mode). Then, several queries to well known astronomical databases (eg: Simbad and NED) allows discarding known sources that were not discarded in the first step. After that, by using the NEOFIT internal database for the FITs data time span, an assessment on what possible NEOs are present in the image is performed.

## SYSTEM ARCHITECTURE

Our application consists of three different layers:

A presentation layer for the user to interact with the system. This is an ASP.NET5 web application running on a Linux Machine.

A logic layer, based on Python, that includes the JPL Spice core for accurate calculations; the updater system, that retrieves the latest SPKs and updates the list of known NEOs; Bokeh, used for plotting, and a REST API which serves the web interface with all the necessary data.

A storage layer, with an SPK repository and a MongoDB with roughly 50 million documents that is updated daily.

## SPACE APPS EXPERIENCE
This project was conceived in the Madrid SpaceApps hackathon, where firstly we studied the feasibility of the idea and then we implemented a proof of concept during two intense days (and nights) of hard work.
## RESOURCES USED
Technologies: JPL Horizons server, JPL spice, Flask, Bokeh, ASP.NET5, MVC6, MongoDB
Programming languages: python, C# (.NET), Javascript, SASS
Software and tools: Apache, LetsEncrypt, npm, gulp

# geocosmo
These are iPython notebooks and python codes developed during my internship at the company

There are three main sets of python codes:

(1) Earthquake Catalog (earthquakes.ipynb)
I have gone on the ANSS website http://quake.geo.berkeley.edu/anss/catalog-search.html
and performed queries to generate 3 CSV files:

alleq_mag5.csv - all earthquakes worldwide of magnitude > 5.0
alleq_mag4.csv - all earthquakes worldwide of magnitude > 4.0
alleq_mag3.csv - all earthquakes worldwide of magnitude > 3.0

The notebook contains codes to:
- better understand the data
- convert datetime to UNIX timestamp
- convert headerless csv files to csv files with headers
- and so on

(2) Alaska Dataset (alaska_predictors.ipynb)
The notebook works on csv files containing data that have been collected at 5 stations on Kodiak Island, Alaska. 
The quality of these data is rather spotty.

(3) Cosmetecor MultiElectrode EMF Dataset (cosmetecor_dev.ipynb and cosmetecor_production.ipynb)
These two notebooks contain development and production code to:
- Automatically extracting .LOG files from the FTP site
- Gluing these .LOG files into yearly .csv files
- Creating a HDF5 file with the years as the groups, and timestamp and EMF as datasets under these groups

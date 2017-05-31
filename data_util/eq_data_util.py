import calendar
import time
import csv


def extract_eq_data(input, output, timewindow=(-2256681600,1454457600),
                    latlong=((90.0,180.0),(-90.0,-180.0))):
  """
  Given the name of a CVS file, the function returns the number of rows of data.

  Inputs:
  - input: name of CVS file as input
  - output: name of CVS file as output
  - time: time window to extract (default to 6-28-1898 til 2-3-2016)
  - latlong: a tuple containing 2 tuples that defines a box:
      - First tuple - lat and long of upper left of the box; default to (90,180)
      - Second tuple - lat and long of lower right of the box; default to (-90,-180)

  Returns:
  The number of rows of data extracted
  """
  start = 0
  end = 0

  f1 = file(input, 'rb')
  f2 = file(output, 'wb')

  c1 = csv.DictReader(f1)
  fieldnames = c1.fieldnames  # extract fieldnames from input

  c2 = csv.DictWriter(f2, fieldnames=fieldnames) #transfer fieldnames to output
  c2.writeheader()
 
  # define the time window  
  start = min(timewindow)
  end = max(timewindow)

  # define the lat and long window
  lat_1,long_1 = latlong[0]
  lat_2,long_2 = latlong[1]

  lat_north = max([lat_1,lat_2])
  lat_south = min((lat_1,lat_2))
  long_east = max((long_1,long_2))
  long_west = min((long_1,long_2))  
    
  rows = 0  
  for row in c1:
    
    # Step 1 - filter wrt time
    time = int(row['timestamp'])
    if time >= start and time <= end:   
        
        # Step 2 -  filter wrt latitude and longtidude
        lat = float(row['lat'])
        long = float(row['long'])
        
        if (lat <= lat_north) and (lat >= lat_south) and (long <= long_east) and (long >= long_west):
            c2.writerow(row)
            rows += 1

  f1.close()
  f2.close() 

  return rows
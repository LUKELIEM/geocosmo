import calendar
import time
import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d


def datatime_2_timestamp(date_time, utc=True):

  # Convert datetime to UNIX timestamp
  if utc is True:
      timestamp = calendar.timegm(date_time.timetuple())  # UTC (Greenwich Time)
  else:
      timestamp = time.mktime(date_time.timetuple())   # Local time
    
  return timestamp


def clean_data(row, name):
  """
  This function assumes that a row of data contains either '' or string representation of a number.
  For an indexed value in the row, the function:
    - returns 0 if the indexed value is ''
    - returns the number if the indexed value is the string representation of a number (e.g. '234').

  Inputs:
  - row: array of data
  - num: index

  Returns:
  Either 0 or the number
  """
  if row[name] == '':
        content = 0
  else:
        content = float(row[name])  # convert from string to float
    
  return content

def fill_missing_data(x):
  """
  This function assumes that a row of data contains numbers and zeros, where a zero denotes missing data.
  It will fill in the missing data using linear interpolation.

  Inputs:
  - row: array of data

  Returns:
  an array of data with missing data filled
  """
  not_zero = np.nonzero(x)
  indices = np.arange(len(x))
  interp = interp1d(indices[not_zero], x[not_zero])
  y=interp(indices)

  return y


def num_datapoints(filename, dict=True):
  """
  Given the name of a CVS file, the function returns the number of rows of data.

  Inputs:
  - filename: name of CVS file
  - dict: If true, the first row is the header, and the file has to be read with cvs.DictReader
          If false, there is no header and file has to be read with cvs.reader

  Returns:
  The number of rows of data
  """
  
  with open(filename, 'rb') as f:
    if dict is True:
        reader = csv.DictReader(f)
    else:
        reader = csv.reader(f, delimiter='\t')
        
    row_count = sum(1 for row in reader)
  f.close()

  return row_count

def plot_predictor(x, y, xlabel, ylabel, ylimit=None, title='Data Title'):
  """
  This function does a scatter plot of the predictor data. 

  Inputs:
  - x, y
  - x_label, y_label
  - ylimit is [min,max]
  - title

  Returns:
  fig
  """
    
  plt.figure(figsize=(10.0, 3.0))  
  plt.scatter(x, y, marker = '.')
  plt.title(title)
  plt.xlabel(xlabel)
  plt.ylabel(ylabel)
  if not (ylimit is None):
      # Set limit along the y-axis  
      axes = plt.gca() # Grab the axes
      axes.set_ylim(ylimit)  
  fig = plt.gcf()  # Grab the current figure before showing it
  plt.show()
    
  return fig  # return the figure

def plot_pred_n_eq(x, y, earthquakes, xlabel, ylabel, eqlabel, ylimit=None, title='Data Title', window=(1450000000,50,20)):
  """
  This function does a scatter plot of the predictor data, then overlay earthquake timeline
  over it.

  Inputs:
  - x, y
  - earthquakes
  - timeline is a tuple with 3 values to define a time window to zoom into the plot:
       - the value is the UNIX timestamp of the event (earthquake)
       - the second value is the number of days before the event
       - the third value is the number of days after the event
  - x_label, y_label
  - title

  Returns:
  fig
  """
  
  # Create the time window  
  event, days_before, days_after = window  
  start = event-days_before*86400
  end = event+days_after*86400

  idx = (x > start) & (x < end)  # generate Boolean index
    
  plt.figure(figsize=(10.0, 6.0))  
  plt.scatter(x[idx], y[idx], marker = '.')
  plt.title(title)
  plt.xlabel(xlabel)
  plt.ylabel(ylabel)

  for quake in earthquakes:
      # Plot a line for an earthquake if it is in the window
      if (quake > start) & (quake < end):  
          plt.axvline(x=quake, label=eqlabel)  
        
  if not (ylimit is None):
      # Set limit along the y-axis
      axes = plt.gca() # Grab the axes
      axes.set_ylim(ylimit) 
        
  fig = plt.gcf()  # Grab the current figure before showing it
  plt.show()
    
  return fig  # return the figure


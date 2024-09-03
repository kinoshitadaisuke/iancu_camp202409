#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/09/03 13:30:33 (UT+8) daisuke>
#

# data file name
file_data = 'sample.data'

# making an empty list for storing data
list_column1 = []

# opening file
with open (file_data, 'r') as fh_in:
    # reading file line-by-line
    for line in fh_in:
        # if the line starts with "#", then skip
        if (line[0] == '#'):
            continue
        # splitting line
        data = line.split ()
        # first column data
        column1_str = data[0]
        # conversion of string into float
        try:
            column1_float = float (column1_str)
        except:
            # printing message
            print (f'# WARNING:')
            print (f'# WARNING: cannot convert "{column1_str}" into float!')
            print (f'# WARNING:')
            # skipping
            continue
        # appending data to the list
        list_column1.append (column1_float)

# initialisation of variable "total"
total = 0.0

# initialisation of variable "sqtotal"
sqtotal = 0.0

# number of data
ndata = len (list_column1)

# calculation of mean and standard deviation
for i in range (ndata):
    total   += list_column1[i]
    sqtotal += list_column1[i]**2
mean   = total / ndata
var    = sqtotal / ndata - mean**2
stddev = var**0.5

# printing results
print (f'results of calculations:')
print (f'  mean   = {mean:7.3f}')
print (f'  stddev = {stddev:7.3f}')

# importing
import numpy

# making numpy array
array_column1 = numpy.array (list_column1)

# calculation of mean and standard deviation
mean   = numpy.mean (array_column1)
stddev = numpy.std (array_column1)

# printing results
print (f'calculations using Numpy:')
print (f'  mean   = {mean:7.3f}')
print (f'  stddev = {stddev:7.3f}')

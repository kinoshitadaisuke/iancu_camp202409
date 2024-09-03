#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/09/03 13:30:47 (UT+8) daisuke>
#

# data file name
file_data = 'sample.data'

# output file name
file_output = 'result.data'

# making an empty list for storing data
list_column3 = []

# opening file
with open (file_data, 'r') as fh_in:
    # reading file line-by-line
    for line in fh_in:
        # if the line starts with "#", then skip
        if (line[0] == '#'):
            continue
        # splitting line
        data = line.split ()
        # third column data
        column3_str = data[2]
        # conversion of string into float
        try:
            column3_float = float (column3_str)
        except:
            # printing message
            print (f'# WARNING:')
            print (f'# WARNING: cannot convert "{column3_str}" into float!')
            print (f'# WARNING:')
            # skipping
            continue
        # appending data to the list
        list_column3.append (column3_float)

# initialisation of variable "total"
total = 0.0

# initialisation of variable "sqtotal"
sqtotal = 0.0

# number of data
ndata = len (list_column3)

# calculation of mean and standard deviation
for i in range (ndata):
    total   += list_column3[i]
    sqtotal += list_column3[i]**2
mean   = total / ndata
var    = sqtotal / ndata - mean**2
stddev = var**0.5

# writing results of calculations into file
with open (file_output, 'w') as fh_out:
    fh_out.write (f'results of calculations:\n')
    fh_out.write (f'  mean   = {mean:7.3f}\n')
    fh_out.write (f'  stddev = {stddev:7.3f}\n')

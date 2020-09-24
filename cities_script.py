# Importing required libraries:
import csv
import operator
import copy
from token import EQUAL
from builtins import sorted

# Reading csv file (with comma as a delimiter) to get the Cities' data from the absolute path:
reader = csv.reader(open('C:\\Users\\heta2\\Desktop\\GitHub_Projects\\Power-Up-with-MicrosoftPowerBI\\US Cities Growing Population\\LargestCitiesUS.csv'), delimiter = ",")

# Initializing variables for columns in csv:
col1 = 'State-City'
col2 = 'Year'
col3 = 'Population'
col4 = 'Rank-Population'

# Code counter variables:
rows_so_far = 0
c = 0

# making an empty 2D data array for rows and columns:
pool = []
pool.append([])

# iterating over each row in csv file:
for row in reader:
    # if it's a header row
	if rows_so_far == 0:
		rows_so_far += 1
		header = row
        #populating headers
		for j in range (0,4):
			if j == 0:
				pool.append([])
				pool[0].append(col1)
			if j == 1:
				pool[0].append(col2)
			if j == 2:
				pool[0].append(col3)
			if j == 3:
				pool[0].append(col4)
    
    # if it's a data row (not header)
	else:
		for i in range(len(row)-2):
			n = len(pool)
			if not row == []:
				if i == 0 or i >= 1:
					item = copy.deepcopy(row)
					r = copy.deepcopy(row)
					for j in range (0,4):
						if item[i+2] is not '':
							if j == 0:
								r[0] = item[j+1]+' - '+item[j]
								pool.append([])
								pool[n-1].append(r[0])
							if j == 1:
								pool[n-1].append(int(header[i+2]))
							if j == 2:
								if item [i+2] == '':
									pool[n-1].append(int(0))
								else:
									pool[n-1].append(int(item[i+2]))
							if j == 3:
								pool[n-1].append(int(0))
rows_so_far += 1

# verify number of rows
n = len(pool)

# don't copy header as data
output = pool[1:n-1]

# descending sort data in csv according to Year and Population
output.sort(key = lambda d: (d[1],d[2]), reverse = True)

# make an empty 2D array for rows and columns
outdata = []
outdata.append([])
outdata[0] = pool[0]
outdata[1:n-1] = output[0:n-2]

# Writing formatted data to csv file for use in MS Power BI:
mycsv = csv.writer(open('C:\\Users\\heta2\\Desktop\\GitHub_Projects\\Power-Up-with-MicrosoftPowerBI\\US Cities Growing Population\\FinalList.csv', 'w', newline=''))
for row in outdata:
	e = outdata.index(row)
	if row[1] != c and e != 0:
		v = 1
		c = row[1]
		row[3] = v
	else:
		if row[1] == c and e != 0:
			v += 1
			row[3] = v
	
	mycsv.writerow(row)
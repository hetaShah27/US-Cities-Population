# US-Cities-Population_1790-1990
Data from the 1790 Census thru 1990 Census is used for the analysis of Population Growth in the US Cities. The data is taken from a non-formatted CSV file, formatted using Python scripting, and visualized using MS Power BI to depict the population growth trend.

**LongestCitiesUS.csv**:  
The csv contains data about ~250 US cities, states and population recorded over 20 years, ranging from 1790 to 1990. Snapshot of the original csv and the file itself is available for download (US-Cities-Population_1790-1990 repository). However, the data is not formatted well. To make the data easier to read and understand, I use Python scripting for data formatting.  

**Data Formatting using Python Script**:  
- The script will merge the “Place” and “State” columns into 1 column with the title “State-City”.
- Transpose data about years from the header row to 1 column called “Year”.
- Transpose the data about population from the content rows to 1 column titled “Population”.
- Add a new column called “Rank-Population” to rank the cities according to the population.
The script (cities_script.py) is available for download.  

**Visualization using MS Power BI**:  
Once the script runs and the formatted "FinalList.csv" is created, I visualized the clean data using MS Power BI. The detailed steps for creating the visualization are explained in the report. The resulting visualization looks as follows:

![Most Crowded US Cities 1790_1990](https://github.com/hetaShah27/US-Cities-Population_1790-1990/blob/master/Snapshots/mostCrowdedUSCitiesViz.png)

You can also check out a video of the visualization working ![here](https://github.com/hetaShah27/US-Cities-Population_1790-1990/blob/master/US%20Cities%20Population%20Growth%20Analysis.webm)  

**Analyses**:  
- The average population (indicated by the dashed blue line) of these US cities is ~0.5 million people
- New York City’s population has been only growing between 1790 – 1990. Since then, it is also called “The city that never sleeps”, “The Center of the Universe” and “The Big Apple”
- The beginning of the 20th century marked an increase in the population of most US cities since World War 1 ended. This flourished a lot of commerce and culture, hence, attracting more crowd and attention
- Other cities that saw an increase in population by 1990 belonged to the states of California, Texas and Illinois. These states supported a large growth in business.
- Mortality rates were growing in the cities of Baltimore (MD), Boston (MA), New Orleans (LA) and Philadelphia (PA) due to pneumonia, tuberculosis (TB) and diarrhea in the 19th and the 20th century.  

You can checkout snapshots of the visualization analyses ![here](https://github.com/hetaShah27/US-Cities-Population_1790-1990/tree/master/Snapshots)

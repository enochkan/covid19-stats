# covid19-stats
Python wrapper functions for retrieving real-time and past information from JHU CSSE database

Download the latest release ```pip install --upgrade covid19-stats```

Sample usage:
~~~~{.python}
# import library
import covid19-stats as cs

# get latest information, returns a pandas dataframe
cs.get_latest()

# get past data with date (mm-dd-yyyy), throws error if file does not exist
cs.get_past_data('02-29-2020')

# get time series representation of all dates, three types: 'confirmed', 'deaths', 'recovered'
cs.get_time_series('deaths')
~~~~


## Versions
0.0.1

## Todo
- [ ] GIS mapping
- [ ] plotting 

## Author
Chi Nok Enoch Kan/ [@chinokenochkan](https://github.com/chinokenochkan)

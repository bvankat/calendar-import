
"""
This file is an exmaple for running the conversion script
"""

import sys
# Yeah this is a hack
sys.path.append('.')
sys.path.append('../')

from convert import Convert
from datetime import datetime, timedelta

convert = Convert()
convert.CSV_FILE_LOCATION = 'home/mwynn/csv.csv'
convert.SAVE_LOCATION = 'home/mwynn/calendar-converted.ics'

convert.read_csv()


convert.make_ical()
convert.save_ical()

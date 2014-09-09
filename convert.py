import csv
from icalendar import Calendar, Event
import datetime

class Convert():
    # Initialize some configs
    def __init__(self):
        self.CSV_FILE_LOCATION = None
        self.SAVE_LOCATION = None
        self.HEADER_COLUMNS_TO_SKIP = 0
        
        # The variables below refer to the column indexes in the CSV
        self.NAME = 0
        self.START_DATE = 1
        self.END_DATE = 2
        self.DESCRIPTION = 3
        self.LOCATION = 4
        
        self.csv_data = []
        self.cal = Calendar()
        
    # Read the csv file
    #
    def read_csv(self):
        csv_reader = csv.reader(open(self.CSV_FILE_LOCATION, 'rb'), delimiter='\t')
        for row in csv_reader:
            self.csv_data.append(row)
            print self.csv_data
            print row

    # Make iCal entries
    #
    def make_ical(self):
        print "I made it to make_ical"
        print self.csv_data
        for row in self.csv_data:
            event = Event()
            event.add('summary', row[self.NAME])
#            event.add('dtstart', datetime.datetime.strptime(row[self.START_DATE], '%n/%j/%Y %H:%i:%s').date())
#            event.add('dtend',  row[self.END_DATE])
            event.add('description', row[self.DESCRIPTION])
            event.add('location', row[self.LOCATION])
            self.cal.add_component(event)
        return self.cal
        
    # Save the calendar instance to a file
    #
    def save_ical(self):
        print "I'm saving"
        print self.cal
        f = open(self.SAVE_LOCATION, 'wb')
        f.write(self.cal.to_ical())
        f.close()

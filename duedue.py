import datefinder
import os
from icalendar import Calendar, Event
from datetime import datetime, timedelta
import PyPDF2

# Read the contract file
def read_contract():
    contract_files = os.listdir('contract_to_calendar/contracts')
    data = ''
    for file in contract_files:
        if file.endswith('.pdf'):
            with open(f'contract_to_calendar/contracts/{file}', 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                for page in range(len(reader.pages)):
                    data += reader.pages[page].extract_text()
        elif file.endswith('.txt'):
            with open(f'contract_to_calendar/contracts/{file}', 'r') as f:
                data += f.read().replace('\n', '')
    return data

# Extract dates from the contract
def extract_dates(contract):
    matches = datefinder.find_dates(contract)
    return [match for match in matches]

# Add dates to calendar
def add_to_calendar(dates):
    cal = Calendar()
    for date in dates:
        event = Event()
        event.add('dtstart', date)
        event.add('dtend', date)
        event.add('summary', 'Contract start date')
        cal.add_component(event)
        event = Event()
        event.add('dtstart', date + timedelta(days=14))
        event.add('dtend', date + timedelta(days=14))
        event.add('summary', 'Contract end date')
        cal.add_component(event)
        event = Event()
        event.add('dtstart', date - timedelta(days=14))
        event.add('dtend', date - timedelta(days=14))
        event.add('summary', '14 day reminder')
        cal.add_component(event)
    with open('contract_to_calendar/duedue.ics', 'wb') as f:
        f.write(cal.to_ical())

# Main function
def main():
    contract = read_contract()
    dates = extract_dates(contract)
    add_to_calendar(dates)

if __name__ == '__main__':
    main()
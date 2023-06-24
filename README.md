# DueDue: Contract Date Tracker

DueDue is a Python script that helps you keep track of contract dates. It reads contracts, extracts date information from them, and then adds those dates to an iCalendar file.

## Usage

1. Place the `duedue.py` script and the `contract_to_calendar` directory within a directory named `black_code`.

2. Add your contract files to the `black_code/contract_to_calendar/contracts` directory. DueDue currently supports `.pdf` and `.txt` files.

3. Run the script with the command `python duedue.py` from within the `black_code` directory.

This will generate an iCalendar file named `duedue.ics` in the `black_code/contract_to_calendar` directory. The iCalendar file will contain an event for each date found in the contract files, along with two additional events set for two weeks before and two weeks after each date.

## Events

For each date found in the contract files, three events are added to the iCalendar:

- The date itself, with the summary "Contract start date".
- Fourteen days after the date, with the summary "Contract end date".
- Fourteen days before the date, with the summary "14 day reminder".

## Requirements

DueDue requires the following Python modules:

- datefinder
- icalendar
- PyPDF2

These can be installed with pip:

```bash
pip install datefinder icalendar PyPDF2


bash
Copy code
pip install datefinder icalendar PyPDF2
Please note that this README assumes the user is familiar with running Python scripts and installing Python modules. For a more detailed guide, you might want to include instructions on how to install Python and set up the script's environment. Also, it's worth mentioning that the script currently hardcodes the directory paths, so the user needs to place the duedue.py file and the contract_to_calendar directory in the correct locations

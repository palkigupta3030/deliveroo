# Cron Expression Parser

This is a simple command-line application in Python to parse and expand a cron expression.

### Requirements

- Python 3.6 or higher

### Installation

1. Clone the repository:

```bash
git clone <repository_url>
cd <repository_directory>

2. to run the application :
python cron_parser.py "*/15 0 1,15 * 1-5 /usr/bin/find"

output will be something like:
minute        0 15 30 45
hour          0
day of month  1 15
month         1 2 3 4 5 6 7 8 9 10 11 12
day of week   1 2 3 4 5
command       /usr/bin/find


Development Environment: 

1. create a virtual environment 
python3 -m venv cron_parser_env
2. Activate the virtual environment
source cron_parser_env/bin/activate
3. save 'cron_parser.py' file in your directory
4. run the script

To run tests :
python -m unittest test_cron_parser.py


Create and activate a virtual environment:

python3 -m venv cron_parser_env
source cron_parser_env/bin/activate

1. Run the script:
python cron_parser.py "*/15 0 1,15 * 1-5 /usr/bin/find"

2. To run the unit tests:
python -m unittest test_cron_parser.py

Cron Expression Format
The cron expression should have five time fields (minute, hour, day of month, month, and day of week) plus a command.
Minute: 0-59 or *
Hour: 0-23 or *
Day of Month: 1-31 or *
Month: 1-12 or *
Day of Week: 0-6 (0 and 6 represent Sunday) or *
Command: The command to be executed


Examples
Input:
python cron_parser.py "*/15 0 1,15 * 1-5 /usr/bin/find"
Output:
sql
Copy code
minute        0 15 30 45
hour          0
day of month  1 15
month         1 2 3 4 5 6 7 8 9 10 11 12
day of week   1 2 3 4 5
command       /usr/bin/find

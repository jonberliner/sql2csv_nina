# Example of how to use your new and improved csv downloader!
# run "python example_sql2csv_nina.py" to execute
# Author: Jon Berliner 12.1.15

import sql2csv_nina as sql2csv

DB_URL = 'sqlite:///participants.db'  # works with mySQL and sqlite
TABLE_NAME = 'turkdemo'  # table name of data in the db
# what you want to call the output.
# sql2csv makes 3 files: [CSV_HEADER]_trialdata.csv, [CSV_HEADER]_eventdata.csv, and [CSV_HEADER]_questiondata.csv
# remember that this name can include a path to whereever you want to save, eg:
#   CSV_HEADER = '/home/nina/results/omgJBYouDaBes' will save to the folder /home/nina/results/
CSV_HEADER = 'example_for_nina'  
# **note that this version also tags every row of all three csvs with id information about the subject.
# **feel free to change the idFields list in sql2csv_nina.py too add/drop idFields
sql2csv.sql2csv(DB_URL, TABLE_NAME, CSV_HEADER)

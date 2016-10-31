# CricSmser

CricSmser sends you cricket scores on your mobile for a specified team using twilio account.

If you have not installed twilio package, install it using commandline:
    
    pip install twilio
    
Before running any script, update details.py according to your twilio credentials

To get scores, run main.py. It will prompt the user to input a team whose scores the want to view. Input team name in short format (eg: WI, PAK, IND etc)

the it will prompt the user to enter the number of minutes after which scores are to be periodically sent (eg: enter 15 for 15 minutes)

Now you are ready to go! Scores for the specified time will be sent to the number provided (in details.py) periodically.

note: Make sure you are connected to internet before running main.py as it scraps www.cricbuzz.com to get scores.

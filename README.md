# UOCIS322 - Project 4 #

# Author: Jaryd Davis, jcsdavis@gmail.com

An ACP brevet time calculator. 

Dockerfile included for ease of use with docker build and docker run. 

Distances input as miles are converted to kilometers then floored. Distances input as kilometers are rounded to the nearest digit.

Kilometer distances are converted to opening and closing times following the minimum and maximum speeds listed here: https://rusa.org/pages/acp-brevet-control-times-calculator 

Opening and closing times are added to the user entered starting time. 

Negative distances return null values and an error message. Distances 20% longer than the brevet distance include an error message.

acp_times calculates the opening and closing times and returns an arrow object

flask_brevets pulls km, brevet distance and starting time from the client, then returns the opening and closing times.

javascript updates the page asynchonrasly via AJAX and jQuery.

Test calculations included for debugging. Run with nosetests. Edit tests/test_brev.py for further testing. 

# Algorithm:

After pulling the km, brevet distance and starting time from the client, flask_brevets.py calls open_time and close_time in acp_times.py to calculate the open and close times.

The four max and min speeds are stored as variables incase of future rules changes.

Open_time:

If the distance is negative, None is returned and an error message is added in flask_brevets.py.

The control distance is first rounded. If it is greater than the total brevet distance, it is changed to be equal to the total brevet distance. 

Hours and minutes, stored as h and m, are intalizied to 0.

Starting from the bracket with the longest lowerbound distance shorter than the control distance, the difference between the control distance and that bracket's lowerbound is stored as 'above'. This is the value that this bracket's min and maximum speeds will be applied to. This distance mod the max speed for the bracket is stored as 'remainder'. The hours this distance adds to the opening time is then calculated by subtracting 'remainder' from 'above' and dividng by the bracket's max speed. This allows us to find the largest integer that is evenly divisible by the bracket's max speed. To find minutes we divide 'remainder' by the bracket's max speed and multiply by 60. 

This processes is repeated for every subsequent bracket.

The minutes are rounded to the nearest interget, then the start time is converted to an arrow object, shifted by the number of hours and minutes the algoirith calcuated, then returned. 

Close_time:

Close_time is similar to open_time except there is a seperate algoritihim for distances equal to or under 60 km. There are also hard coded times for distances equal to or greater than the control distance. 


## Credits

Michal Young, Ram Durairajan, Steven Walton, Joe Istas, Ali Hassani
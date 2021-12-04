Class Description
The AdventCalendar class is a very simple and basic class for making a virtual advent calendars. It mainly serves as a skeleton 
for others trying to make virtual advent calendars. Feel free to add on to it as it is lacking a lot of fuctionality currently and
certain aspects could be much better optimized. If you want to change the calendar make sure you keep images for all 25 days in a 
folder and make sure that each image is name its number and is a jpg.

Class and data variables

_total_days:
This variable simply holds the total amout of days within all advent calendars.

_day:
This variable holds the current day the advent calendar is set to

_assets:
This variable holds the current pathway for where the img assets of the advent calendar are saved. If you want to change it set it to the
pathway where your folder of assets are located ex. C:\Users\natha\Documents\Coding Stuff\assign_10_1\assets if not changed it will use
the default pathway provided by the program

Methods

get_day():
Simple getter method for what the current day of the calendar is set to

set_day():
Simple set method to set the current day of the calendar

get_assets():
Simple get method to get the current file path where the calendar images are

set_assets():
Simple set method to set the file path 

update_day():
This increments the day by 1 if you want to use this method in some type of gui or something to make the calendar more user friendly

view():
This creates the picture in which the calendar is viewable

Demo program documentation 
Description: The demo program mainly just goes over the current fuctionality of the class and shows how you can use it in it's current
	     state. Most of the information about what it is doing is contained within the print statements given by the demo.

Instructions: IMPORTANT! Before running the demo program make sure that you have python 3.9 installed and working. Also make sure that 
	      pygame is installed. This can be done by running the command:python3 -m pip install -U pygame --user
	      If you want to test to make sure it is installed run the command:python3 -m pygame.examples.aliens
	      Finally please make sure that the assets folder is stored in the same directory as the program or else errors might occur
	      If everything is installed correctly just simply run the class file in an interpretor either by opening it with python 3.9
	      or by running the Terminal command in the directory where it is saved:python3 customClass.py


#Following the completion of their program (or completion of Optional Practical Training/Academic
#Training), F students have a 60 day grace period while those in J status have a 30 day grace period.
#During this grace period you may NOT work or attend school.  This grace period simply provides you
#the opportunity to prepare for departing or traveling within the U.S., or applying to change to
#another status.

import datetime

date = raw_input("Enter work authorization end date (YYYY-MM-DD): ")
status = raw_input("Enter status (F/J): ")

u = datetime.datetime.strptime(date,"%Y-%m-%d")
if status == 'F' or status == 'f':
    d = datetime.timedelta(days=60)
elif status == 'J' or status == 'j':
    d = datetime.timedelta(days=30)

t = str(u + d)

print "Your grace period ends on %s." % t
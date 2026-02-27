# Shop opened from 9am to 12pm, 1pm to 6pm

# time hour?
#If hour is (between 9 and 11) or between (1 and 5)
# else
#   => display shop is open
#   => display shop is closed

hour = 11

if (hour >= 9 and hour <= 11) or (hour >=13 and hour <=17):
    print("Shop is open")
    
else:
    print("Shop is closed")
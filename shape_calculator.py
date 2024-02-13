def add_time(start, duration, day="0"):
 time = start.split()[0].split(":")
 hour = time[0]
 minutes = time[1] 
 dayKey = ["Monday", "Tuesday","Wednesday","Thursday", "Friday","Saturday","Sunday"]
 message = ""

 match day.lower():
    case "monday":
         day = 1
    case "tuesday":
         day = 2
    case "wednesday":
         day = 3
    case "thursday":
         day = 4   
    case "friday":
         day = 5
    case "saturday":
         day = 6
    case "sunday":
         day = 7
    case _ :
        day = 0     
         
 AM =    True if start.split()[1] == "AM" else False

 
#Separate Hours and minutes
 duration = duration.split()[0].split(":")
 durationHour = duration[0]
 durationMinutes = duration[1]  
 extraHour = 0
 dayspassed = 0
 
 totalMinutes = (int(minutes) +  int(durationMinutes))
 if(totalMinutes>59):
      extraHour = int(totalMinutes/60)     
      totalMinutes = (int(minutes) +  int(durationMinutes))%60
 totalHour =   int(hour) + int(durationHour) + int(extraHour)
 
 if(totalHour>=12):
     #print("TotalHourBefore Format {}".format(totalHour))
     dayspassed = totalHour/24 
     if(dayspassed - int(dayspassed)>=0.5 and not AM):
         dayspassed = int(dayspassed) + 1
     if(totalHour!=12 ):
        totalHour = totalHour%12
     if(totalHour>=12 and not AM):
         dayspassed += 1
      
     if(int(durationHour)%24!=0 or (int(durationHour) + int(extraHour))%24>0 ):  
              AM = not AM
           
 if(totalHour==0):
     totalHour=12
#if Day is given calculated days
 if(day!=0):
    day = (day + dayspassed)%7
  
 dayspassed = int(dayspassed) 

 if(dayspassed==0 and day!=0):
     message =  ", {}".format(dayKey[int(day)-1])
 
 if(dayspassed==1):     
    message = " (next day)" if day == 0 else  ", {} (next day)".format(dayKey[int(day)-1])
 elif(dayspassed>1):
    if(day==0):
        message = " ({} days later)".format(dayspassed)
    elif(day>0):
        message =  ", {} ({} days later)".format(dayKey[int(day)-1],dayspassed)


 return(str(totalHour) + ":" + str(totalMinutes).rjust(2,"0") + (" AM" if AM==True else " PM" ) + message )
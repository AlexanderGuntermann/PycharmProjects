distanceKM = 10

distanceInMile = (distanceKM * (1.0 / 1.61)) # there are 1.61 miles in 1.0 km = 16.1 miles


totalSeconds = ((60.0 * 60.0) + (5.0 * 60) + 42.0) # convert hours and minutes to seconds. total is 3942

totalHour = (65.7 / 60)  # 1 hour = 60 mins, 5 minutes = 5 minutes, 42 seconds = .70 of a minute

timePerMile = totalSeconds/distanceInMile

convertToMins = timePerMile/60 # equals 10.5777

roundedMinutes = 10

convertSeconds = .5777 * 60 # since we want minutes and seconds separate, I have to multiply the .577 by 60
                            # to get it back to seconds

averageSpeed = distanceInMile/totalHour

print('The time per mile in minutes and seconds is: ' + str(roundedMinutes)+' minutes' +" and " + str(convertSeconds)+' seconds')


print('The average speed in miles per hour is '+ str(averageSpeed) + ' miles per hour')








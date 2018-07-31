print('You leave the house at 7:30 AM')

startHour = 07
startMinutes = 30
startSec = 0

firstMileMin = startMinutes + 8
firstMileSec = startSec + 15

nextThreeMilesMin = firstMileMin + (7 * 3)
nextThreeMilesSec = firstMileSec + (12 * 3)
AM = 'AM'


print("You walk 4 miles in 29 minutes and 51 seconds")


print('You arrive at the house at: '+str(startHour)+':'+str(nextThreeMilesMin)+':'+str(nextThreeMilesSec)+' AM')


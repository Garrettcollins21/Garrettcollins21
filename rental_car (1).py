import sys
'''
Section 1: Collect customer input
'''
rentalCode = input("(B)udget, (D)aily, or (W)eekly rental?\n")
if rentalCode == "B" or rentalCode == "D":
  rentalPeriod = input("Number of Days Rented:\n")
elif rentalCode == "W":
  rentalPeriod = input("Number of Weeks Rented:\n")
print(rentalCode)
print(rentalPeriod)
print('Starting Odometer Reading:')
odoStart = input()
print('Ending Odometer Reading:')
odoEnd = input()
totalMiles = int(odoEnd) - int(odoStart)
print(odoStart)
print(odoEnd)
print(totalMiles)
budgetCharge = 40.00
dailyCharge = 60.00
weeklyCharge = 190.00
if rentalCode == 'B':
  baseCharge = int(rentalPeriod) * float(budgetCharge)
elif rentalCode == 'D':
  baseCharge = int(rentalPeriod) * float(dailyCharge)
elif rentalCode == 'W':
  baseCharge = int(rentalPeriod) * float(weeklyCharge)
print("%.2f" % baseCharge)

#Unsure as to why calculating charges part 2 did not work
#received an error stating that my totalMiles was incorrect 
#it was not converting the odoEnd and odoStart strings to integers
#However, I simply used the same code as the previous section and it converted properly
totalCharge = 0 
if rentalCode == 'B':
  totalCharge = baseCharge + (totalmiles * .25)
elif rentalCode == 'D':
  averageDayMiles = totalMiles/daysRented
  if averageDayMiles <= 100:
    totalCharge = baseCharge
  else:
    extraMiles = totalMiles - 100
    totalCharge = baseCharge + (extraMiles * .25)
elif rentalCode == 'W':
  averageWeekMiles = totalMiles/weeksRented
  if averageWeekMiles <= 900:
    totalCharge = baseCharge
  else:
    totalCharge = baseCharge + (weeksRented * 100)
print(totalCharge)
#Rental Summary?
print(RentalPeriod)
print(odoStart)
print(odoEnd)
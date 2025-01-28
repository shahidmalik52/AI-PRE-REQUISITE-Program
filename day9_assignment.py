# Author: Shahid Malik

# Parking Lot Fee Manager
# Description:
# Develop a program to calculate parking fees for vehicles based on the hours parked. 
# The user inputs the number of cars parked each day and the hours parked for each car.
# Using nested loops, the program calculates the fee for each car, the total fee for the day,
# and displays a summary for all days. The fee is determined based on a fixed rate per hour.

total_earning = 0
rate_per_hour = int(input('Enter the parking rate per hour: '))                 # Input rate of parking per hour
days = int(input('Enter the number of days: '))                                 # Input the number of days you want to use
for day in range(1, days + 1):
    total_earning_per_day = 0
    cars_parked = int(input(f'Enter the number of cars parked on Day{day}: '))     # Input the number of cars parked each day
    print('**********************************')
    print(f'********** Day{day} summary **********')
    for car in range(1, cars_parked+1):
        hours = int(input(f'Enter the number of hours Car{car} was parked: '))
        charges = rate_per_hour * hours                                         # calculates the fee for each car on particular day
        total_earning_per_day += charges                                                    # calculates the total fee for the day
        
        print(f'The car{car} was charged {charges} PKR')
    print(f'For Day{day} the total earning was {total_earning_per_day} PKR')    
    total_earning += total_earning_per_day
    print('______________________________')
print(f'The total earning for {days} Days is {total_earning} PKR')
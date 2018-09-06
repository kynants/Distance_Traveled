# The distance a vehicle travels can be calculated as follows:
#
#                   Distance = Speed * Time
#
# For example, if a train travels 40 mph for three hours, the distance traveled
# is 120 miles. Design a program that asks the user for the speed of a vehicle
# (in mph) and how many hours it has traveled. It should then use a loop to
# display the distance the vehicle has traveled for each hour of that time
# period. Here is an example of the output:
#
# What is the speed of the vehicle in mph? 40[Enter]
# How many hours has it traveled? 3[Enter]
# Hour          Distance Traveled
# 1             40
# 2             80
# 3             120

# Prompts
speed = int(input('What is the speed of the vehicle in mph? '))
hrs = int(input('How many hours has it traveled? '))

# Initialized Variables
count = 1
hr_num = 1
dist_trav = speed * hr_num

# While loop counts to however many hours user inputted
while count < hrs:
    # While loop automates the hour number and distance traveled in relation to
    # the speed and hours inputted by the user
    while hr_num <= hrs or dist_trav <= (hrs * speed):
        print('Hour:', hr_num)
        hr_num += 1
        print('Distance traveled:', dist_trav)
        dist_trav = speed * hr_num
    count += 1
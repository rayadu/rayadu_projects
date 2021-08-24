#Imagine you’re working in a transportation company, 
# and you’re boss asked you to prepare a status report. 
# This should include the total number of buses, 
# space in each bus, 
# number of drivers, 
# the number of passengers, 
# buses that are not used, 
# buses used, 
# the total buses capacity, 
# and the average passengers per bus.

buses = 100
print("total buses are" + str(buses))
space_in_a_bus = 20.0
drivers = 30
passengers = 130

#here if we didnt convert buses_not_driven into str in print statement it would throw error because we cannot combines two different types ( string and number)
buses_not_driven =buses-drivers
print("The no of buses_not_driven_are" + str(buses_not_driven))

buses_driven =buses-buses_not_driven
print("The no of buses that are driven are"+ str(buses_driven))

total_capacity =buses_driven*space_in_a_bus
print("The total capacity for buses that are running is " + str(total_capacity))

average_passengers_per_bus =passengers/buses_driven
print('the average passengers per bus are'+ str(average_passengers_per_bus))

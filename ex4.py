cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, " cars available.")
print("There are only", drivers, "drivers today.")
print("There will be", cars_not_driven, "cars not driven today.")
print("We can transfort", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We Need to put about", average_passengers_per_car, 
"person in each car today.")
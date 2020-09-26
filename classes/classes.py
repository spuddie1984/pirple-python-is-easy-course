"""
Homework Assignment #9: Classes

Details:
 
Create a class called "Vehicle" and methods that allow you to set the "Make", "Model", "Year,", and "Weight".

The class should also contain a "NeedsMaintenance" boolean that defaults to False, and and "TripsSinceMaintenance" Integer that defaults to 0.

Next an inheritance classes from Vehicle called "Cars".

The Cars class should contain a method called "Drive" that sets the state of a boolean isDriving to True.  It should have another method called "Stop" that sets the value of isDriving to false.

Switching isDriving from true to false should increment the "TripsSinceMaintenance" counter. And when TripsSinceMaintenance exceeds 100, then the NeedsMaintenance boolean should be set to true.

Add a "Repair" method to either class that resets the TripsSinceMaintenance to zero, and NeedsMaintenance to false.

Create 3 different cars, using your Cars class, and drive them all a different number of times. Then print out their values for Make, Model, Year, Weight, NeedsMaintenance, and TripsSinceMaintenance

Extra Credit:

Create a Planes class that is also an inheritance class from Vehicle. Add methods to the Planes class for Flying and Landing (similar to Driving and Stopping), but different in one respect: Once the NeedsMaintenance boolean gets set to true, any attempt at flight should be rejected (return false), and an error message should be printed saying that the plane can't fly until it's repaired.
"""


class Vehicle:
    
    # Make attributes private meaning they can only be accessed via a method, not directly
    def __init__(self,make,model,year,weight,needsMaintenance,tripsSinceMaintenance):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__weight = weight
        self.needsMaintenance = needsMaintenance
        self.tripsSinceMaintenance = tripsSinceMaintenance

    # Use the common getter setter convention
    def setMake(self,setMake):
        self.__make = setMake

    def setModel(self,setModel):
        self.__model = setModel

    def setYear(self,setYear):
        self.__year = setYear

    def setWeight(self,setWeight):
        self.__weight = setWeight

    def getMake(self):
        return self.__make

    def getModel(self):
        return self.__model

    def getYear(self):
        return self.__year

    def getWeight(self):
        return self.__weight

# Inherits from the Vehicle Class
class Cars(Vehicle):
    def __init__(self,make,model,year,weight,needsMaintenance=False,tripsSinceMaintenance=0):
        Vehicle.__init__(self,make,model,year,weight,needsMaintenance,tripsSinceMaintenance)
        self.isDriving = False
        self.tripCounter = 0

    def drive(self):
        self.isDriving = True

    def stop(self):
        self.isDriving = False
        self.tripsSinceMaintenance += 1
        if self.tripsSinceMaintenance == 100:
            self.needsMaintenance = True
        
    def repair(self):
        self.needsMaintenance = False
        self.tripsSinceMaintenance = 0

    def trips(self):
        self.tripCounter += 1

    def getTrips(self):
        return self.tripCounter
    
    # This will return the string below if the instantiated object is printed 
    def __str__(self):
        return f'{self.getMake()} {self.getModel()} {self.getYear()} Model whick weights {self.getWeight()} has done {self.getTrips()} Trips. The Needs Maintenance Variable is set to {self.needsMaintenance}. Your Car has travelled {self.tripsSinceMaintenance} times since its last maintenance'

Car1 = Cars("Toyota","Corolla","2020","1365kg")
Car2 = Cars("Peugeot","308","2020","1122kg")
Car3 = Cars("Hyundai","Tucson","2020","1467kg")


for trip in range(100):
    Car1.drive()
    Car1.stop()
    if Car1.needsMaintenance:
        Car1.repair()
    Car1.trips()

for trip in range(50):
    Car2.drive()
    Car2.stop()
    if Car2.needsMaintenance:
        Car2.repair()
    Car2.trips()

for trip in range(200):
    Car3.drive()
    Car3.stop()
    if Car3.needsMaintenance:
        Car3.repair()
    Car3.trips()

# Printing the object will invoke the __str__ method on the Cars class
print(Car1)   
print(Car2)
print(Car3)
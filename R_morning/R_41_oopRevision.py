Revision


class PowerPlant():
    pass


a = PowerPlant()
a.location = "Nagpur"
print(a.location)     #Nagpur


a.location = "Thane"
print(a.location)    #Thane




class PowerPlant():
    country = "India"  # class Attribute

    def __init__(self, location, capacity):
        self.location = location  # obj attribute
        self.capacity = capacity

    def __str__(self):
        return f"Power plant at {self.location} of capacity {self.capacity} MW"


p1 = PowerPlant("Nagpur", 33)
p2 = PowerPlant("Thane", 33)

print(p1)    #Power plant at Nagpur of capacity 33 MW

print(p1.country)     # India
p1.country = "Nepal"
print(p1.country)       #Nepal
print(PowerPlant.country)    #India
print(p2.country)        # India

PowerPlant.country = "Bhutan"
print(p2.country)     #Bhutan

print(p1.location)      # Nagpur
p1.location = "Beed"
print(p1.location)      #Beed






class PowerPlant():
    country = "India"  # class Attribute

    def __init__(self, location, capacity):
        self.__location = location  # obj attribute
        self.capacity = capacity

    def __str__(self):
        return f"Power plant at {self.__location} of capacity {self.capacity} MW"


p1 = PowerPlant("Nagpur", 33)
p2 = PowerPlant("Thane", 33)

print(p1)     #Power plant at Nagpur of capacity 33 MW

print(p1.country)    #India
p1.country = "Nepal"
print(p1.country)      #Nepal
print(PowerPlant.country)     # India
print(p2.country)       #India

PowerPlant.country = "Bhutan"
print(p2.country)      #Bhutan

p1.__location = "Beed"
print(p1.__location)      # Beed

print(p1)          #Power plant at Nagpur of capacity 33 MW

# name mangling
p1._PowerPlant__location = "Beed"
print(p1._PowerPlant__location)       #Beed

print(p1)         #Power plant at Beed of capacity 33 MW





class PowerPlant():
    country = "India"  # class Attribute

    def __init__(self, location, capacity):
        self._location = location  # obj attribute
        self.capacity = capacity

    def __str__(self):
        return f"Power plant at {self._location} of capacity {self.capacity} MW"


p1 = PowerPlant("Nagpur", 33)
p2 = PowerPlant("Thane", 33)

print(p1)      #Power  plant at Nagpur of capacity 33 MW

print(p1.country)       #India
p1.country = "Nepal"
print(p1.country)       #Nepal
print(PowerPlant.country)     #India
print(p2.country)     #India

PowerPlant.country = "Bhutan"
print(p2.country)       #Bhutan

p1._location = "Beed"
print(p1._location)      #Beed

print(p1)       #Power plant at Beed of capacity 33 MW




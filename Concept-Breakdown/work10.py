class Car:
    size = 10
    year = 2008

    def drive(self):
        move0 = (self.size) - 5
        return move0

    def stop(self):
        move1 = (self.size) - 10
        return move1

    def back(self):
        move2 = (self.size) - 15
        return move2
    
    def get(self):
        return self.drive()
    
myCar = Car()
print(myCar.get())

# to set the properties/attributes of the class
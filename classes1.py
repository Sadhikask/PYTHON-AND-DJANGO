class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    def add_passenger(self, name):
        if not self.open_seats():
            return False 
        self.passengers.append(name)
        return True 
    def open_seats(self):
        return self.capacity - len(self.passengers)
flight = Flight(3)
people = ["Alice", "Bob", "Charlie", "David"]
for person in people: 
    success = flight.add_passenger(person)
    if success:
        print(f"{person} added to flight successfully.")
    else:
        print(f"{person} could not be added to flight.")
class Ticekts_Method:
    standard_fare = 50.0
    index = 0

    def __init__(self):
        self.name = []
        self.type_passenger = []
        self.final_fare = []

    def ask_name(self):
        self.name = input('Whats is your name: ')
        return self.name

    def ask_type(self):
        self.type_passenger = input('Type of customer: ').lower()
        return self.type_passenger

    def calculate_fare(self, the_type):
        if the_type == "senior":
            self.final_fare = self.standard_fare - (self.standard_fare * .20)
            return self.final_fare
        elif the_type == "student":
            self.final_fare = self.standard_fare - (self.standard_fare * .15)
            return self.final_fare
        else:
            return self.standard_fare

    def display_passenger(self, NAME, TYPE, FARE):
        for i in range(2):
            print('Name: ', NAME[i], 'Passenger type: ', TYPE[i], 'Fare: ', FARE[i])


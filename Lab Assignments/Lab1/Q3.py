import random


class Flight:
    def __init__(self, flightName, flightNumber):  # Initializing Flight class variables
        self.airline_name = flightName
        self.flight_number = flightNumber

    def flight_display(self):  # Displaying flight details
        print('Airlines : ', self.airline_name)
        print('Flight number : ', self.flight_number)


class employee:
    def __init__(self, empId, empName, empAge, empSex, empAddress):  # Initializing employee class variables
        self.__empId = empId
        self.empName = empName
        self.empAge = empAge
        self.empSex = empSex
        self.empAddress = empAddress

    def e_display(self):  # Displaying employee details
        print("Name of employee: ", self.empName)
        print('employee id: ', self.__empId)
        print('employee age: ', self.empAge)
        print('employee gender: ', self.empSex)
        print('employee Address: ', self.empAddress)


class Passenger:

    def __init__(self):  # Initializing Passenger class variables
        Passenger.pName = input('Enter passenger name: ')
        Passenger.age = input('Enter age : ')
        Passenger.gender = input('Enter gender: ')
        Passenger.baggage = input("Enter number of baggage's: ")
        Passenger.class_type = input('Select business or economy class: ')


class Baggage:
    bag_fare = 0

    def __init__(self):
        self.checkIn_bags = int(Passenger.baggage)
        if self.checkIn_bags > 2:    # checking for number of baggage's and calculating price
            self.bag_fare = 50 * (self.checkIn_bags - 2)
        print("Number of baggage's: ", self.checkIn_bags, "baggage fare: ", self.bag_fare)


class Fare(Baggage):
    online = random.randint(110, 200)  # price is randomly taken
    totalFare = 0

    def __init__(self):
        super().__init__()
        x = input('Do you want to proceed? Y/N ')   # calculating total price after user wants to continue
        if x == 'Y' or x == 'y':
            Fare.totalFare = (self.online + self.bag_fare)
        else:
            pass


class Ticket(Passenger):
    def __init__(self):
        super().__init__()   # Initializing super class and calling Passenger class
        fare1 = Fare()    # calling Fare class
        if fare1.totalFare != 0:
            print("Passenger name:", self.pName)  # Accessing parent class variable
            if Passenger.class_type == "business":
                fare1.totalFare += 100
                print("Passenger class type:", self.class_type)
                print("your Total price:", fare1.totalFare)
                print("===============flight details================")   # calling flight class for displaying details
                flight = Flight('American Airlines', 6789)
                flight.flight_display()
                # details
                emp = employee('e1', 'e_Anu', 21, 'F', "4838 Paseo")
                emp.e_display()
                print('\n')
                print("****You successfully booked the ticket****")
            else:
                pass
        else:
            pass


if __name__ == "__main__":
    t = Ticket()

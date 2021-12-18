class Train:
    Booking= 'Indian Railways'
    def __init__(self,name,fare,seats):
        self.name= name
        self.fare= fare
        self.seats= seats

    def greet(self):
        print(f"Welcome to the {self.Booking}: ")
    def Method(self):
        print('Steps for booking:')
        print("Open the booking website and click on book")
        print("Enter the number of seats and following requitred informations")
        print("To confirm click on Yes Confirm")
    def Fare(self):
        print('Prices:')
        print(f"The price of seats in {self.name} is {self.fare}")
    def Status(self):
        print('Vacancy:')
        print(f"Total number of seats in {self.name} are 200")
        print(f"No of seats left in {self.name} are {self.seats}")
    def Seats(self):
        self.number= int(input('Enter the number of seats u want to book: '))
    def Book(self):
        if (self.seats>0):
            print('Your ticket has been booked')
            self.seats= self.seats-self.number
        else:
            print(f'Sorry no seats are available, Please try Tatkal')
    def Cancel(self):
        self.ans= input('Do u want to cancel seats y/n: ')
        if(self.ans == 'y'):
            self.num= int(input('How many seats: '))
            print('Cancellation is successfull')
            self.seats= self.seats+ self.num
        elif(self.ans == 'n'):
            print('Thank u for your precious time!')
        else:
            print('Please enter y/n next time properly')

tict= Train('Rajdhani Express', 'Rs1000', 50)
tict.greet()
tict.Method()
tict.Fare()
tict.Status()
tict.Seats()
tict.Book()
tict.Cancel()
tict.Status()




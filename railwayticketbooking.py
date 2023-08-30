class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password(self, password):
        return self.password == password

class TrainInfo:
    def __init__(self, train_number, source, destination, available_seats):
        self.train_number = train_number
        self.source = source
        self.destination = destination
        self.available_seats = available_seats
    
    def display_info(self):
        print("-------------------------")
        print(f"Train Number: {self.train_number}")
        print(f"Source: {self.source}")
        print(f"Destination: {self.destination}")
        print(f"Available Seats: {self.available_seats}")
        print("--------------------------")

class passengerslist():
    def __init__(self,p_name,p_age,p_mobile):
        self.p_name = p_name
        self.p_age = p_age
        self.p_mobile = p_mobile
    
    def passengerinfo(self):
        print("-------------------")
        print("  passenger list  ")
        print("-------------------")
        print(f"passenger name: {self.p_name}")
        print(f"passenger age: {self.p_age}")
        print(f"passenger mobile: {self.p_mobile}\n")
        print("-------------------")

accounts = []
login_account = None

while True:
    print("1. Create Account\n2. Login")
    choice = int(input("Enter the choice: "))
    
    if choice == 1:
        username = input("Enter username: ")
        password = input("Enter password: ")
        accounts.append(Account(username, password))
        print("Account created successfully")

    elif choice == 2:
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        for acc in accounts:
            if acc.username == username and acc.check_password(password):
                login_account = acc
                print("Logged in as", username)
                break
                
        if login_account is None:
            print("Invalid username or password")
            
        else:
            print("Login successful")
            break
            
    else:
        print("Invalid choice")
        
print("Welcome to IRCTC")

if login_account is not None:
    trainslist = [45636,30464,34672,53992]
    trains = [
        TrainInfo(45636, "Hyderabad", "Tirupati", 125),
        TrainInfo(30464, "Vizag", "Mumbai", 400),
        TrainInfo(34672, "banglore", "delhi", 115),
        TrainInfo(53992, "Vizag", "hyderabad", 290)
        
    ]
    
    
        

while True:
    userinput = input("enter 1 to see train details, enter 2 to exit /n ")
    if int(userinput) == 1:
        for train in trains:
            train.display_info()
        train_numbers = int(input("Enter Train number: "))
        for i in range(len(trains)):
            if train_numbers == trains[i].train_number:
                print("availabale tickets for this train:", trains[i].available_seats)

                tickets = int(input("enter number of tickets :"))
                if tickets <= trains[i].available_seats:
                    p_name = input("Enter passanger name: ")
                    p_age = int(input("Enter your age: "))
                    p_mobile = int(input("Enter your mobile number: "))
                    p = passengerslist(p_name,p_age,p_mobile)
                    print(tickets,"have been booked: ")
                    p.passengerinfo()
                    trains[i].available_seats-tickets
                else:
                    print("sufficient tickets are not available")

    elif int(userinput) == 2:
        break

    else:
        print("Invalid input")





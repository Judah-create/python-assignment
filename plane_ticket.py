import random
from datetime import datetime, timedelta

# Flight destinations → duration (hours)
flight_times = {
    "PortHarcourt": 1,
    "Capetown": 10,
    "accra": 26,
    "nairobi": 5,
    "Canada": 18
}

# Base prices
base_prices = {
    "lagos": 45000,
    "abuja": 55000,
    "accra": 80000,
    "nairobi": 150000,
    "london": 380000
}

# Random weather conditions
bad_weather = ["storm", "heavy rain", "thunder", "fog"]
good_weather = ["clear", "sunny", "mild clouds"]

# Days flights do NOT operate
no_flight_days = ["sunday"]

# Seats (rows 1–35, seats A–F)
ROWS = 35
SEATS = ["A", "B", "C", "D", "E", "F"]
available_seats = [(row, seat) for row in range(1, ROWS + 1) for seat in SEATS]

print("=== PLANE TICKET ISSUER ===")

name = input("Enter passenger name: ")
age = int(input("Enter passenger age: "))

# Minor handling
if age < 15:
    print("Passenger is under 15. Adult required.")
    guardian = int(input("Enter guardian age (18+): "))
    if guardian < 18:
        print("*** Cannot issue ticket: Guardian must be 18+ ***")
        exit()
    else:
        print("Guardian confirmed.\n")

# Destination
destination = input("Enter flight destination: ").lower()

if destination not in flight_times:
    print("*** Destination not available ***")
    exit()

# Class selection
print("\nClasses:")
print("1. First Class (+₦50,000)")
print("2. Business Class (+₦25,000)")
print("3. Economy Class (base price)\n")

class_choice = input("Enter class (first/business/economy): ").lower()

if class_choice == "first":
    travel_class = "First Class"
    class_fee = 50000
    row = random.randint(1, 5)
elif class_choice == "business":
    travel_class = "Business Class"
    class_fee = 25000
    row = random.randint(6, 15)
elif class_choice == "economy":
    travel_class = "Economy Class"
    class_fee = 0
    row = random.randint(16, 35)
else:
    print("*** Invalid class ***")
    exit()

# Seat assignment
seat = random.choice(SEATS)
available_seats.remove((row, seat))

# PET OPTION
print("\nPets allowed: dog, cat, monkey")
pet_choice = input("Are you flying with a pet? (yes/no): ").lower()

pet = None
pet_fee = 0

if pet_choice == "yes":
    pet = input("Enter pet type (dog/cat/monkey): ").lower()
    if pet not in ["dog", "cat", "monkey"]:
        print("*** Invalid pet ***")
        exit()
    pet_fee = 15000
else:
    pet = "None"

# WEATHER CHECK
today_weather = random.choice(good_weather + bad_weather)
print(f"\nCurrent weather condition: {today_weather}")

if today_weather in bad_weather:
    print("*** FLIGHT CANCELLED: Bad weather ***")
    exit()

# DAY CHECK
day = datetime.now().strftime("%A").lower()

if day in no_flight_days:
    print(f"*** NO FLIGHTS ON {day.upper()} ***")
    exit()

# Price
base = base_prices[destination]
final_price = base + class_fee + pet_fee

# Departure time
depart_input = input("\nEnter departure time (HH:MM): ")
depart_time = datetime.strptime(depart_input, "%H:%M")

# Arrival time
duration = flight_times[destination]
arrival_time = depart_time + timedelta(hours=duration)

# Print Ticket
print("\n====================================")
print("             PLANE TICKET")
print("====================================")
print(f"Passenger Name : {name}")
print(f"Age            : {age}")
print(f"Pet            : {pet}")
print(f"Destination    : {destination.title()}")
print(f"Class          : {travel_class}")
print(f"Seat           : Row {row}{seat}")
print(f"Total Price    : ₦{final_price}")
print("------------------------------------")
print(f"Departure Time : {depart_time.strftime('%H:%M')}")
print(f"Arrival Time   : {arrival_time.strftime('%H:%M')}")
print(f"Duration       : {duration} hours")
print("------------------------------------")
print(f"Weather        : {today_weather}")
print(f"Day            : {day.title()}")
print("====================================")
print("  THANK YOU FOR FLYING WITH US!")
print("====================================")

# Movie ticket booking simulation

# Predefined data: movies, showtimes, and seat/ ticket prices
movies = {
    "Wicked: For Good": {"showtimes": ["1:00 PM", "6:00 PM"], "price": 10.75},
    "Zootopia 2": {"showtimes": ["3:00 PM", "8:00 PM"], "price": 10.25},
    "Eternity": {"showtimes": ["12:00 PM", "5:00 PM"], "price": 10.25},
    "The Housemaid": {"showtimes": ["2:30 PM", "7:30 PM"], "price": 11.25}
}

total_bookings = 0
total_cost = 0.0

print("Welcome to the Movie Ticket Booking System!\n")

while True:
    print("Available Movies:\n")
    
    # Loop through the movie dictionary and display each movie
    for i, (movie, details) in enumerate(movies.items(), 1):
        print(f"{i}. {movie}")
        print(f"   Showtimes: {', '.join(details['showtimes'])}")
        print(f"   Ticket Price: ${details['price']:.2f}\n")

    # Ask user for movie name
    choice = input("Enter the movie name you want to book (or 'quit' to exit): ").strip()

    if choice.lower() == "quit":
        break

    if choice not in movies:
        print("Movie not found. Please choose from the list.\n")
        continue

    # Ask user to choose a showtime
    print(f"Available showtimes for {choice}:")
    for index, time in enumerate(movies[choice]["showtimes"], 1):
        print(f"{index}. {time}")

    # Validate showtime selection
    try:
        time_choice = int(input("Choose a showtime (enter the number): "))
        if time_choice < 1 or time_choice > len(movies[choice]["showtimes"]):
            print("Invalid showtime number.\n")
            continue
        selected_showtime = movies[choice]["showtimes"][time_choice - 1]
    except ValueError:
        print("Invalid input. Please enter a number.\n")
        continue

    # Ask how many tickets
    try:
        num_tickets = int(input(f"How many tickets for '{choice}'? "))
        if num_tickets <= 0:
            print("Please enter a valid number of tickets.\n")
            continue
    except ValueError:
        print("Invalid input. Please enter a number.\n")
        continue

    # Calculate cost
    total_price = num_tickets * movies[choice]["price"]

    # Print booking confirmation
    print(f"{num_tickets} ticket(s) booked for '{choice}' at {selected_showtime} — Total: ${total_price:.2f}\n")

    # Update total stats
    total_bookings += num_tickets
    total_cost += total_price

    # Ask if they want another booking
    another = input("Do you want to book another movie? (yes/no): ").strip().lower()
    if another != "yes":
        break

# Print summary at the end
print("\nBooking Summary")
print(f"Total Tickets Booked: {total_bookings}")
print(f"Total Amount: ${total_cost:.2f}")
print("Thank you for booking with us!")
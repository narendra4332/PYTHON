# # Creating board
# board = [" " for x in range(9)]

# # Defining print function
# def print_board():
    
#     print("-------------")
#     print(f"| {board[0]} | {board[1]} | {board[2]} |")
#     print("-------------")
#     print(f"| {board[3]} | {board[4]} | {board[5]} |")
#     print("-------------")
#     print(f"| {board[6]} | {board[7]} | {board[8]} |")
#     print("-------------")
    
# # Player move and icon allocation

# def player_move(icon):
#     if icon == "X":
#         number = 1
#     elif icon == "O":
#         number = 2
#     print("Your turn player {}".format(number))
#     choice = int(input("Enter your move (1-9): ").strip())
#     if board[choice - 1] == " ":
#         board[choice - 1] = icon
#     else:
#         print()
#         print("That space is already taken!")
        
# # result of the game        
# def is_victory(icon):
#     if (board[0] == icon and board[1] == icon and board[2] == icon) or (board[3] == icon and board[4] == icon and board[5] == icon) or (board[6] == icon and board[7] == icon and board[8] == icon) or (board[0] == icon and board[3] == icon and board[6] == icon) or (board[1] == icon and board[4] == icon and board[7] == icon) or (board[2] == icon and board[5] == icon and board[8] == icon) or (board[0] == icon and board[4] == icon and board[8] == icon) or (board[2] == icon and board[4] == icon and board[6] == icon):
#         return True
#     else:
#         return False
       
# # if draws happens    
# def is_draw():
#     if " " not in board:
#         return True
#     else:
#         return False


# # main program to execute   
# while True:
#     print_board()
#     player_move("X")
#     print_board()
#     if is_victory("X"):
#         print("X wins! Congratulations!")
#         break
#     elif is_draw():
#         print("It's a draw!")
#         break
#     player_move("O")
#     if is_victory("O"):
#         print_board()
#         print("O wins! Congratulations!")
#         break
#     elif is_draw():
#         print("It's a draw!")
#         break


# ----------------------------------------------------------------------------------------
class Bus:
    def __init__(self, bus_id, route, total_seats):
        self.bus_id = bus_id
        self.route = route
        self.total_seats = total_seats
        self.booked_seats = set()

    def is_seat_available(self, seat_number):
        return seat_number not in self.booked_seats

    def book_seat(self, seat_number):
        if self.is_seat_available(seat_number):
            self.booked_seats.add(seat_number)
            return True
        return False

    def cancel_seat(self, seat_number):
        if seat_number in self.booked_seats:
            self.booked_seats.remove(seat_number)
            return True
        return False

    def get_available_seats(self):
        return [seat for seat in range(1, self.total_seats + 1) if seat not in self.booked_seats]


def display_buses(buses):
    print("\nAvailable Buses:")
    for bus in buses:
        available_seats = bus.get_available_seats()
        print(f"Bus ID: {bus.bus_id}, Route: {bus.route}, Available Seats: {len(available_seats)}")


def book_seat(buses):
    bus_id = int(input("Enter Bus ID to book: "))
    seat_number = int(input("Enter Seat Number to book: "))
    bus = next((b for b in buses if b.bus_id == bus_id), None)
    if bus and bus.book_seat(seat_number):
        print("Seat booked successfully!")
    else:
        print("Seat not available or invalid Bus ID.")


def cancel_booking(buses):
    bus_id = int(input("Enter Bus ID to cancel booking: "))
    seat_number = int(input("Enter Seat Number to cancel: "))
    bus = next((b for b in buses if b.bus_id == bus_id), None)
    if bus and bus.cancel_seat(seat_number):
        print("Booking cancelled successfully!")
    else:
        print("No booking found or invalid Bus ID.")


def main():
    buses = [
        Bus(1, "Route A", 30),
        Bus(2, "Route B", 20)
    ]

    while True:
        print("\nMenu:")
        print("1. View Buses")
        print("2. Book Seat")
        print("3. Cancel Booking")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            display_buses(buses)
        elif choice == '2':
            book_seat(buses)
        elif choice == '3':
            cancel_booking(buses)
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
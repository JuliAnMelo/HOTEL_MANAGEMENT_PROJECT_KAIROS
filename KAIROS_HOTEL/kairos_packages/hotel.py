import time
import os

from datetime import datetime, timedelta
from kairos_packages.room import Room, Simple_Room, Double_Room, Twin_Room, Family_Room
from kairos_packages.person import Employee, Guest
from kairos_packages.exception import IntInputError

def clear_console():
    """Clears the console based on the operating system."""
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix/Linux/MacOS
        os.system('clear')

        
class Hotel():
    """
    A class to represent a hotel, containing room data, employees, and guests.

    Attributes
    
    hotel_data:
        - A tuple containing Room objects that represent the rooms of the hotel. 
        Defaults to an empty tuple.

    employees:
        - A dictionary containing Employee objects, where each key is a role (e.g., 'manager', 'staff'),
        and the value is the corresponding Employee object. Defaults to None.

    guests:
        - A dictionary containing Guest objects, where each key is a guest's unique identifier (e.g., guest ID),
        and the value is the corresponding Guest object. Defaults to None.
    """
    def __init__(self, hotel_data: tuple[Room, ...] = (), employees: dict = None, guests: dict = None):
        self._hotel_data = hotel_data
        self._employees = employees
        self._guests = guests
    

    def to_dict(self) -> dict:
        """
        Serializes the Hotel object into a dictionary format for easy storage or transfer.

        This method converts the hotel's data, including rooms, employees, and guests, into a dictionary.
        It prepares the data for serialization by calling the `to_dict` method of each individual object 
        (e.g., Room, Employee, Guest).

        Returns
            A dictionary containing the hotel's data, including:
            - 'hotel_data': A list of dictionaries representing each room's data.
            - 'employees': A dictionary where keys are employee roles and values are dictionaries 
            representing each employee's data.
            - 'guests': A dictionary where keys are room names, and values are lists of dictionaries 
            representing each guest's data (if the object is a Guest) or simplified data for employees 
            (if the object is an Employee).
        """
        return {"hotel_data": [room.to_dict() for room in self._hotel_data], 
                "employees": {role: emp.to_dict() for role, emp in self._employees.items()},
                "guests": {room_name: [guest.to_dict() if isinstance(guest, Guest) else {"employee_role": guest._employee_role} for guest in guests_list]
                           for room_name, guests_list in self._guests.items()}}
    
    @classmethod
    def from_dict(cls, data_dict: dict):
        """
        Creates a Hotel object from a dictionary of hotel data.

        This method deserializes the hotel data stored in a dictionary format and reconstructs
        the Hotel object, including its rooms, employees, and guests.

        Parameters
            A dictionary containing serialized hotel data with the following keys:
            - 'hotel_data': A list of dictionaries, each representing a room's data, including the room type.
            - 'employees': A dictionary where keys are employee roles and values are dictionaries of employee data.
            - 'guests': A dictionary where keys are room names and values are lists of either guest data 
            or employee role information (for employees staying in rooms).

        Returns
            An instance of the Hotel class with rooms, employees, and guests initialized based on the provided dictionary.

        - Room types are determined based on the "type" field in the room data and converted to the corresponding 
        Room subclass (e.g., Simple_Room, Double_Room, etc.).
        - Employees are deserialized using the `Employee.from_dict` method, and employees staying in rooms are 
        assigned to the guests list based on their role.
        - Guests are deserialized using the `Guest.from_dict` method.
        """
        room_objects = []
        for room_data in data_dict["hotel_data"]:
            room_type = room_data.pop("type")
            if room_type == "Simple_Room":
                room_objects.append(Simple_Room.from_dict(room_data))
            elif room_type == "Double_Room":
                room_objects.append(Double_Room.from_dict(room_data))
            elif room_type == "Twin_Room":
                room_objects.append(Twin_Room.from_dict(room_data))
            elif room_type == "Family_Room":
                room_objects.append(Family_Room.from_dict(room_data))
            else:
                raise ValueError(f"Unknown room type: {room_type}")
            
        employees = {role: Employee.from_dict(emp_data) for role, emp_data in data_dict.get("employees", {}).items()}
        
        guests = {}
        for room_name, guests_list in data_dict.get("guests", {}).items():
            guests[room_name] = []
            for guest_data in guests_list:
                if "employee_role" in guest_data:
                    employee = next(emp for emp in employees.values() if emp._employee_role == guest_data["employee_role"])
                    guests[room_name].append(employee)
                else:
                    guests[room_name].append(Guest.from_dict(guest_data))

        return cls(tuple(room_objects), employees, guests)


    def get_current_status(self) -> None:
        """
        Displays the current status of all rooms in the hotel and provides additional 
        details for a selected room.

        This method continuously prints the current status of each room in the hotel. Users can
        choose a room by pressing the corresponding number to view more detailed information,
        such as the room's status and the guest or employee occupying the room.

        Functionality:
        - Shows a list of all rooms with their current status and an option to select a room 
        for more information.
        - If a room is occupied, the method provides details about the occupant, whether it's a 
        guest or an employee.
        - The user can press `0` to exit the loop.

        Exceptions:

        IntInputError
            If the user inputs a number that is outside the valid range for room selection.
        ValueError
            If the user inputs anything other than a number when prompted to make a selection.

 
        - The status of each room is retrieved from its `get_current_status` method.
        - The occupant information is extracted from the `guests` dictionary, which stores a list
        of guests or employees for each room.
        - This method pauses for 1 second between printing each room's status and 2 seconds 
        before returning after displaying detailed information.
        """
        while True:
            clear_console()
            print("  ROOM       STATUS      MORE INFO")
            for room in self._hotel_data:
                print(f"{room.get_current_status()}  -->  press {(self._hotel_data.index(room)) + 1}")
                time.sleep(1)

            try:
                check = int(input("Continue                  press 0" "\n"
                                  "                         ""  -->  "))
                  
                if check > 0 and check <= len(self._hotel_data):
                    requested = self._hotel_data[check - 1]
                    returned = self._guests[requested._room_name]

                    stat_1_report = f"CURRENT STATUS  -  {requested._states[requested._current_status]}"
                    if requested._current_status > 0: 
                        if isinstance(returned[0], Guest):
                            stat_1_report += f"  -  {returned[0]._person_name[1]} {returned[0]._person_name[0]}  -  {returned[0]._person_phone}"
                        elif isinstance(returned[0], Employee):
                            stat_1_report += f"  -  {returned[0]._employee_role}  -  {returned[0]._person_name[1]} {returned[0]._person_name[0]}"    
                    else: pass

                    time.sleep(1)
                    clear_console()   
                    print(f"   {requested._room_name}\n{stat_1_report}\n")
                    time.sleep(3)
                    break

                elif check == 0: break
                else: raise IntInputError(f"Press a number between 0 and {len(self._hotel_data)}")

            except IntInputError as error: 
                print(f"\n{error}, Returning.\n\n")
                time.sleep(2)
            except ValueError: 
                print("\nPress numbers only, Returning.\n\n")
                time.sleep(2)
    

    def get_complete_status(self) -> None:
        """
        Displays the complete status of all rooms in the hotel, including the current, next, 
        and after statuses, and provides additional details for a selected room.

        This method continuously prints a table with each room's current status, next status, 
        and after status. Users can select a room by pressing the corresponding number to view
        more detailed information, such as the occupants' information at each status level.

        Functionality:
        - Displays a list of all rooms with their current, next, and after statuses.
        - Provides occupant details for each status (current, next, after), whether it's a guest 
        or an employee.
        - The user can press `0` to exit the loop.
        - When a room is selected, it prints the occupant's name and phone number or the employee's 
        role and name for each status.

        Exceptions:

        IntInputError
            If the user inputs a number outside the valid range for room selection.
        ValueError
            If the user inputs anything other than a number when prompted to make a selection.


        - The statuses (current, next, after) are retrieved from the room's `get_complete_status` method.
        - The occupants' information is taken from the `guests` dictionary, which stores a list of guests 
        or employees for each room.
        - This method includes delays (1 second and 1.5 seconds) between printing each room's status and 
        the detailed output, and a 3-second delay after printing detailed information before returning.
        """
        while True:
            clear_console()
            print("  ROOM            CURRENT STATUS                NEXT STATUS                 AFTER STATUS         MORE INFO")
            for room in self._hotel_data:
                print(f"{room.get_complete_status()}  -->  press {(self._hotel_data.index(room)) + 1}")
                time.sleep(1)

            try:
                check = int(input("Continue                                                                                          press 0""\n"
                                  "                                                                                                   -->  "))     
                
                if check > 0 and check <= len(self._hotel_data):
                    requested = self._hotel_data[check - 1]
                    returned = self._guests[requested._room_name]

                    stat_1_report = f"CURRENT STATUS  -  {requested._states[requested._current_status]}"
                    if requested._current_status > 0: 
                        if isinstance(returned[0], Guest):
                            stat_1_report += f"  -  {returned[0]._person_name[1]} {returned[0]._person_name[0]}  -  {returned[0]._person_phone}"
                        elif isinstance(returned[0], Employee):
                            stat_1_report += f"  -  {returned[0]._employee_role}  -  {returned[0]._person_name[1]} {returned[0]._person_name[0]}"    
                    else: pass

                    stat_2_report = f"NEXT STATUS     -  {requested._states[requested._next_status]}"
                    if requested._next_status > 0: 
                        if isinstance(returned[1], Guest):
                            stat_2_report += f"  -  {returned[1]._person_name[1]} {returned[1]._person_name[0]}  -  {returned[1]._person_phone}"
                        elif isinstance(returned[1], Employee):
                            stat_2_report += f"  -  {returned[1]._employee_role}  -  {returned[1]._person_name[1]} {returned[1]._person_name[0]}"
                    else: pass

                    stat_3_report = f"AFTER STATUS    -  {requested._states[requested._after_status]}"
                    if requested._after_status > 0: 
                        if isinstance(returned[2], Guest):
                            stat_3_report += f"  -  {returned[2]._person_name[1]} {returned[2]._person_name[0]}  -  {returned[2]._person_phone}"
                        elif isinstance(returned[2], Employee):
                            stat_3_report += f"  -  {returned[2]._employee_role}  -  {returned[2]._person_name[1]} {returned[2]._person_name[0]}"
                    else: pass

                    time.sleep(1.5)
                    clear_console()   
                    print(f"   {requested._room_name}\n{stat_1_report}\n{stat_2_report}\n{stat_3_report}\n")
                    time.sleep(4.5)
                    break

                elif check == 0: break
                else: raise IntInputError(f"Press a number between 0 and {len(self._hotel_data)}")

            except IntInputError as error: 
                print(f"\n{error}, Returning.\n\n")
                time.sleep(2)
            except ValueError: 
                print("\nPress numbers only, Returning.\n\n")
                time.sleep(2)


    def sunrise_protocol(self) -> None:
        """
        Executes the daily status update for all rooms in the hotel, moving rooms through 
        their lifecycle of statuses (e.g., AVAILABLE, OCCUPIED, CLEANING, MAINTENANCE) based 
        on the current, next, and after status timelines.

        The method iterates over each room and performs the following actions:
        1. Checks the current status and updates it based on the time remaining (endline).
        2. Moves statuses from "current" to "next" and from "next" to "after" when appropriate.
        3. Prompts the user for status updates when required, offering several scenarios to
        change the room's state (e.g., making it AVAILABLE, RESERVED, OCCUPIED).
        4. Automatically assigns the appropriate employee or guest to each room's state.

        Functionality:
        - If the current status has remaining time (`current_endline > 0`), the room's status 
        is printed, showing how many days are left.
        - If the current status has finished (`current_endline == 0`), the room transitions 
        to the next status, moving the guest or employee accordingly.
        - If no next status is available (`current_endline == 0` and `next_endline == 0`), 
        the user is prompted to update the room's status. The protocol provides several 
        predefined status transitions (e.g., AVAILABLE, RESERVED, OCCUPIED, CLEANING).
        - The method updates room statuses, reassigns guests or employees, and prints the 
        updated room status after each action.

        User Input:

        The method prompts the user to provide updates for rooms when no next status is predefined. 
        Possible options include:
        1. Make the room AVAILABLE.
        2. Make the room RESERVED, followed by OCCUPIED.
        3. Make the room OCCUPIED, followed by CLEANING.
        4. Make the room CLEANING, followed by AVAILABLE.
        5. Put the room in MAINTENANCE, followed by CLEANING.
        6. Disable the room.

        Exceptions:

            IntInputError: If an invalid number is entered during status update prompts (i.e., 
        numbers outside of the valid range).
            ValueError: If non-numeric input is entered when a number is expected.

        
        - Room transitions include automatic reassignment of guests and employees based on the 
        new status.
        - The method simulates delays (1.5 seconds) to mimic real-time system updates.
        """
        for room in self._hotel_data:
            status_update = f"{room._room_name}: An error has raised, please Check Room Status again.{room._slowdown}"

            if room._current_endline > 0:
                status_update = f"{room._room_name} is {room._states[room._current_status]}, {room._current_endline} days left.{room._slowdown}"


            elif room._current_endline == 0 and room._next_endline > 0:
                status_update = f"{room._room_name} went from {room._states[room._current_status]} to {room._states[room._next_status]}.{room._slowdown}"

                room._current_status, room._current_endline = room._next_status, room._next_endline
                self._guests[room._room_name][0] = self._guests[room._room_name][1]

                room._next_status, room._next_endline = room._after_status, room._after_endline
                self._guests[room._room_name][1] = self._guests[room._room_name][2]

                room._after_status, room._after_endline = 0, 0
                self._guests[room._room_name][2] = self._employees["NOINFO"] 


            elif room._current_endline == 0 and room._next_endline == 0:
                try:
                    update_notice = int(input(f"{room._room_name} finished {room._states[room._current_status]}, an update is needed:\n{room._update_board}\t\t  --> "))

                    if update_notice == 1:
                        self._guests[room._room_name][0] = self._employees["Housekeeper"]
                        room._current_status, room._current_endline = 1, 1    
                        status_update = f"{room._room_name} is now {room._states[room._current_status]}.{room._slowdown}"
                        

                    elif update_notice == 2:
                        update_person = Guest.registration()

                        schedule_update_1 = int(input(f"{room._states[2]}:  {room._schedule_message}\n  --> "))
                        room._current_status, room._current_endline = 2, schedule_update_1
                        self._guests[room._room_name][0] = update_person

                        schedule_update_2 = int(input(f"{room._states[3]}:  {room._schedule_message}\n  --> "))
                        room._next_status, room._next_endline = 3, schedule_update_2
                        self._guests[room._room_name][1] = update_person

                        status_update = f"{room._room_name} is now {room._states[room._current_status]}.{room._slowdown}"


                    elif update_notice == 3:
                        update_person = Guest.registration()    

                        schedule_update_1 = int(input(f"{room._states[3]}:  {room._schedule_message}\n  --> "))
                        room._current_status, room._current_endline = 3, schedule_update_1
                        self._guests[room._room_name][0] = update_person

                        room._next_status, room._next_endline = 4, 1
                        self._guests[room._room_name][1] = self._employees["Concierge"]

                        status_update = f"{room._room_name} is now {room._states[room._current_status]}.{room._slowdown}"


                    elif update_notice == 4:
                        room._current_status, room._current_endline = 4, 1
                        self._guests[room._room_name][0] = self._employees["Concierge"]

                        room._next_status, room._next_endline = 1, 1
                        self._guests[room._room_name][1] = self._employees["Housekeeper"]

                        status_update = f"{room._room_name} is now {room._states[room._current_status]}.{room._slowdown}"


                    elif update_notice == 5:
                        schedule_update_1 = int(input(f"{room._states[5]}:  {room._schedule_message}\n  --> "))
                        room._current_status, room._current_endline = 5, schedule_update_1
                        self._guests[room._room_name][0] = self._employees["Maintenance Worker"]

                        room._next_status, room._next_endline = 4, 1
                        self._guests[room._room_name][1] = self._employees["Concierge"]

                        status_update = f"{room._room_name} is now {room._states[room._current_status]}.{room._slowdown}"


                    elif update_notice == 6:
                        schedule_update_1 = int(input(f"{room._states[6]}:  {room._schedule_message}\n  --> "))
                        room._current_status, room._current_endline = 6, schedule_update_1
                        self._guests[room._room_name][0] = self._employees["Front Desk Manager"]

                        status_update = f"{room._room_name} becomes {room._states[room._current_status]}.{room._slowdown}"
                    
                    else: raise IntInputError("Press a number between 1 and 6.")
                
                except IntInputError as error: 
                    print(f"\n{error}")
                    time.sleep(2)
                except ValueError: 
                    print("\nPress numbers only.")
                    time.sleep(2)

            print(status_update)
            time.sleep(1.5)


    def noon_protocol(self) -> None:
        """
        This method handles room status updates based on user input for various tasks.
        It allows scheduling actions for specific rooms such as reserving, occupying, cleaning,
        maintenance, or disabling a room. Depending on the chosen action, the system updates the 
        status of the room and the assigned guests or employees.

        The process consists of several steps:
        1. The user selects a task by pressing a corresponding number (1-5).
        2. The system checks available rooms that can accommodate the chosen task.
        3. The user selects a specific room from the list.
        4. Based on the selected task, the system registers a person or employee to the room 
        and updates its status accordingly.
        
        Available tasks:
        - Reserve a Room: Press 1.
        - Occupy a Room: Press 2.
        - Schedule a Cleaning: Press 3.
        - Schedule Maintenance: Press 4.
        - Disable a Room: Press 5.
        - Return to the previous menu: Press 0.

        Errors are handled for invalid inputs or non-numeric values, ensuring smooth operation.

        Exceptions:
            IntInputError: Custom exception for incorrect integer inputs.
            ValueError: Raised when the user inputs a non-integer value.
        """
        while True:
            clear_console()
            try:
                option = int(input("\n""     SPECIFIC TASKS              TO GO" "\n"
                                "Reserve a Room                  press 1" "\n"
                                "Occupy a Room                   press 2" "\n"
                                "Schedule a Cleaning             press 3" "\n"
                                "Schedule a Maintenance          press 4" "\n"
                                "Disable a Room                  press 5" "\n"
                                "Return                          press 0" "\n"
                                "                                 -->  "))       

                if option == 0: break

                elif option > 0 and option <= 5:
                    booking_rooms = []
                    for room in self._hotel_data:
                        if room.scheduling_conditions(option) is True:
                            booking_rooms.append(room)
                        else: pass

                    if len(booking_rooms) > 0:
                        while True:
                            clear_console()
                            print("  ROOM             INFORMATION           UNTIL        TO DO")
                            for b_room in booking_rooms:
                                print(f"{b_room.scheduling_data(option)}  -->  press {(booking_rooms.index(b_room) + 1)}")
                                time.sleep(1)

                            try:
                                book = int(input("Cancel                                                press 0" "\n"
                                                "                                                       -->  "))
                                
                                if book > 0 and book <= len(booking_rooms):
                                    reg_1 = booking_rooms[book - 1]._current_status
                                    reg_2 = booking_rooms[book - 1]._next_status
                                    reg_3 = booking_rooms[book - 1]._after_status

                                    if option == 1:
                                        booking_person = Guest.registration()
                                        print(booking_rooms[book - 1].scheduling_protocol(option))
                                        if booking_rooms[book - 1]._current_status != reg_1: 
                                            self._guests[booking_rooms[book - 1]._room_name][0] = booking_person
                                        if booking_rooms[book - 1]._next_status != reg_2:
                                            self._guests[booking_rooms[book - 1]._room_name][1] = booking_person
                                        if booking_rooms[book - 1]._after_status != reg_3:
                                            self._guests[booking_rooms[book - 1]._room_name][2] = booking_person

                                    elif option == 2:
                                        booking_person = Guest.registration()
                                        print(booking_rooms[book - 1].scheduling_protocol(option))
                                        if booking_rooms[book - 1]._current_status != reg_1: 
                                            self._guests[booking_rooms[book - 1]._room_name][0] = booking_person
                                        elif booking_rooms[book - 1]._next_status != reg_2:
                                            self._guests[booking_rooms[book - 1]._room_name][1] = booking_person
                                        elif booking_rooms[book - 1]._after_status != reg_3:
                                            self._guests[booking_rooms[book - 1]._room_name][2] = booking_person

                                    elif option == 3:
                                        booking_person = self._employees["Concierge"]
                                        print(booking_rooms[book - 1].scheduling_protocol(option))
                                        if booking_rooms[book - 1]._current_status != reg_1: 
                                            self._guests[booking_rooms[book - 1]._room_name][0] = booking_person
                                        elif booking_rooms[book - 1]._next_status != reg_2:
                                            self._guests[booking_rooms[book - 1]._room_name][1] = booking_person
                                        elif booking_rooms[book - 1]._after_status != reg_3:
                                            self._guests[booking_rooms[book - 1]._room_name][2] = booking_person
                                    
                                    elif option == 4:
                                        booking_person = self._employees["Maintenance Worker"]
                                        print(booking_rooms[book - 1].scheduling_protocol(option))
                                        if booking_rooms[book - 1]._current_status != reg_1: 
                                            self._guests[booking_rooms[book - 1]._room_name][0] = booking_person
                                        elif booking_rooms[book - 1]._next_status != reg_2:
                                            self._guests[booking_rooms[book - 1]._room_name][1] = booking_person
                                        elif booking_rooms[book - 1]._after_status != reg_3:
                                            self._guests[booking_rooms[book - 1]._room_name][2] = booking_person

                                    elif option == 5:
                                        booking_person = self._employees["Front Desk Manager"]
                                        print(booking_rooms[book - 1].scheduling_protocol(option))
                                        if booking_rooms[book - 1]._current_status != reg_1: 
                                            self._guests[booking_rooms[book - 1]._room_name][0] = booking_person
                                        elif booking_rooms[book - 1]._next_status != reg_2:
                                            self._guests[booking_rooms[book - 1]._room_name][1] = booking_person
                                        elif booking_rooms[book - 1]._after_status != reg_3:
                                            self._guests[booking_rooms[book - 1]._room_name][2] = booking_person
                                    
                                    break

                                elif book == 0: break
                                else: raise IntInputError(f"Press a number between 0 and {len(booking_rooms)}, Returning.")

                            except IntInputError as error: 
                                print(f"\n{error}\n\n")
                                time.sleep(2)
                            except ValueError: 
                                print("\nPress numbers only, Returning.\n\n")
                                time.sleep(2)


                    else: 
                        print("There are no rooms available to schedule that option.")
                        time.sleep(2)

                else: raise IntInputError("Press a number between 0 and 5, Returning.")
                    
            except IntInputError as error: 
                print(f"\n{error}\n\n")
                time.sleep(2)
            except ValueError: 
                print("\nPress numbers only, Returning.\n\n")
                time.sleep(2)


    def sunset_protocol(self) -> None:
        """
        The sunset_protocol method is responsible for decrementing the 'current_endline' 
        value of each room in the hotel by one. This simulates the passage of a day, 
        updating the remaining days for the current room status.

        After updating the status for all rooms, the method waits for 2 seconds before completing execution.
        """
        for room in self._hotel_data:
            room._current_endline = room._current_endline - 1
        time.sleep(2)

    
    def midnight_protocol(self) -> None:
        """
        The method handles the manual adjustment or cancellation 
        of room statuses in the hotel based on the current, next, and after status of each room.
        It allows the user to update the room's status by interacting with specific prompts 
        for each room's state.

        The protocol iterates through all rooms and presents the current, next, and after status
        for each room. The user can choose a room to modify its status or cancel any status. 


        User Interactions:
            - Displays the rooms with their current, next, and after statuses.
            - Allows the user to select a room for status cancellation.
            - Enables the user to advance or conserve the posterior room schedule.
            - Provides detailed prompts for each status (current, next, or after) allowing for cancellation or changes.
            - The method continues until the user chooses to return or finish the modification process.

        Exceptions:
            - IntInputError: Raised if the user enters an invalid number that does not correspond 
            to a valid option.
            - ValueError: Raised if the user enters non-numeric input when a number is required.

        Effects:
            - Modifies the status of selected rooms based on user input.
            - Updates the 'guests' and 'employees' dictionaries with the appropriate person or 
            placeholder ('NOINFO') after changes in the room status.
            - Outputs information on status changes to the console and pauses for user interaction.
        """
        while True:
            clear_console()
            print("\n""  ROOM        CURRENT        NEXT        AFTER       TO CHOOSE")
            for room in self._hotel_data:                                                                                
                print(f"{room._room_name}:    {room._states[room._current_status]}  -  {room._states[room._next_status]}  -  {room._states[room._after_status]}  -->  press {(self._hotel_data.index(room)) + 1}")
                time.sleep(1)

            try:
                check = int(input("Return                                               press 0""\n"
                                   "                                                      -->  "))

                if check > 0 and check <= len(self._hotel_data):
                    requested = self._hotel_data[check - 1]
                    returned = self._guests[requested._room_name]

                    stat_1_report = f"CURRENT STATUS  -  {requested._states[requested._current_status]}"
                    if requested._current_status > 0: 
                        if isinstance(returned[0], Guest):
                            stat_1_report += f"  -  {returned[0]._person_name[1]} {returned[0]._person_name[0]}\tpress 1"
                        elif isinstance(returned[0], Employee):
                            stat_1_report += f"  -  {returned[0]._employee_role}\tpress 1"    
                    else: stat_1_report += "\t\t\tpress 1"


                    stat_2_report = f"NEXT STATUS     -  {requested._states[requested._next_status]}"
                    if requested._next_status > 0: 
                        if isinstance(returned[1], Guest):
                            stat_2_report += f"  -  {returned[1]._person_name[1]} {returned[1]._person_name[0]}\tpress 2"
                        elif isinstance(returned[1], Employee):
                            stat_2_report += f"  -  {returned[1]._employee_role}\tpress 2"
                    else: stat_2_report += "\t\t\tpress 2"


                    stat_3_report = f"AFTER STATUS    -  {requested._states[requested._after_status]}"
                    if requested._after_status > 0: 
                        if isinstance(returned[2], Guest):
                            stat_3_report += f"  -  {returned[2]._person_name[1]} {returned[2]._person_name[0]}\tpress 3"
                        elif isinstance(returned[2], Employee):
                            stat_3_report += f"  -  {returned[2]._employee_role}\tpress 3"
                    else: stat_3_report += "\t\t\tpress 3"

                    time.sleep(1.5)
                    clear_console()
                    print(f"   {requested._room_name}\n{stat_1_report}\n{stat_2_report}\n{stat_3_report}")

                    try:
                        cancel_1 = int(input("Return                                          press 0""\n"
                                           "                                                 -->  "))

                        if cancel_1 == 1:
                            status_update = f"{requested._room_name} CURRENT STATUS "

                            if requested._next_endline == 0 and requested._after_endline == 0:
                                self._guests[requested._room_name][0] = self._employees["Housekeeper"]
                                requested._current_status, requested._current_endline = 1, 1           
                                status_update += f"has been canceled.\n{requested._room_name} CURRENT STATUS is now {requested._states[requested._current_status]}.\n\n"
                            
                            else:
                                try:
                                    cancel_2 = int(input("To advance the schedule    press 1""\n"
                                                         "To conserve the schedule   press 2""\n"
                                                         "                            -->  "))

                                    if cancel_2 == 1:
                                        requested._current_status, requested._current_endline = requested._next_status, requested._next_endline
                                        self._guests[requested._room_name][0] = self._guests[requested._room_name][1]

                                        requested._next_status, requested._next_endline = requested._after_status, requested._after_endline
                                        self._guests[requested._room_name][1] = self._guests[requested._room_name][2]

                                        requested._after_status, requested._after_endline = 0, 0
                                        self._guests[requested._room_name][2] = self._employees["NOINFO"] 

                                        status_update += f"has been canceled.\n{requested._room_name} CURRENT STATUS is now {requested._states[requested._current_status]}.\n\n"
       
                                    elif cancel_2 == 2:
                                        requested._current_status = 6
                                        self._guests[requested._room_name][0] = self._employees["Front Desk Manager"]
                                        status_update += f"has been canceled.\n{requested._room_name} CURRENT STATUS is now {requested._states[requested._current_status]}.\n\n"

                                except IntInputError as error: 
                                    print(f"\n{error}, Returning.\n\n")
                                    time.sleep(2)
                                except ValueError: 
                                    print("\nPress numbers only, Returning.\n\n")
                                    time.sleep(2)


                        elif cancel_1 == 2:
                            status_update = f"{requested._room_name} NEXT STATUS "

                            if requested._after_endline == 0:
                                self._guests[requested._room_name][1] = self._employees["Housekeeper"]
                                requested._next_status, requested._next_endline = 1, 1           
                                status_update += f"has been canceled.\n{requested._room_name} NEXT STATUS is now {requested._states[requested._next_status]}.\n\n"
                            
                            else:
                                try:
                                    cancel_2 = int(input("To advance the schedule    press 1""\n"
                                                         "To conserve the schedule   press 2""\n"
                                                         "                            -->  "))

                                    if cancel_2 == 1:
                                        requested._next_status, requested._next_endline = requested._after_status, requested._after_endline
                                        self._guests[requested._room_name][1] = self._guests[requested._room_name][2]

                                        requested._after_status, requested._after_endline = 0, 0
                                        self._guests[requested._room_name][2] = self._employees["NOINFO"] 

                                        status_update += f"has been canceled.\n{requested._room_name} NEXT STATUS is now {requested._states[requested._next_status]}.\n\n"
       
                                    elif cancel_2 == 2:
                                        requested._next_status = 6
                                        self._guests[requested._room_name][1] = self._employees["Front Desk Manager"]
                                        status_update += f"has been canceled.\n{requested._room_name} NEXT STATUS is now {requested._states[requested._next_status]}.\n\n"

                                except IntInputError as error: 
                                    print(f"\n{error}, Returning.\n\n")
                                    time.sleep(2)
                                except ValueError: 
                                    print("\nPress numbers only, Returning.\n\n")
                                    time.sleep(2)


                        elif cancel_1 == 3:
                            status_update = f"{requested._room_name} AFTER STATUS "

                            self._guests[requested._room_name][2] = self._employees["Housekeeper"]
                            requested._after_status, requested._after_endline = 1, 1           
                            status_update += f"has been canceled.\n{requested._room_name} AFTER STATUS is now {requested._states[requested._after_status]}.\n\n"
                            
                        elif cancel_1 == 0: break
                        else: raise IntInputError(f"Press a number between 0 and 3")

                        print(status_update)
                        time.sleep(2)
                        break

                    except IntInputError as error: 
                        print(f"\n{error}, Returning.\n\n")
                        time.sleep(2)
                    except ValueError: 
                        print("\nPress numbers only, Returning.\n\n")
                        time.sleep(2)
                    
                elif check == 0: break
                else: raise IntInputError(f"Press a number between 0 and {len(self._hotel_data)}")
            
            except IntInputError as error: 
                print(f"\n{error}, Returning.\n\n")
                time.sleep(2)
            except ValueError: 
                print("\nPress numbers only, Returning.\n\n")
                time.sleep(2)



    def get_daily_report(self, date: datetime) -> str:
        """
        Generates a daily report for all rooms in the hotel, detailing their current, next, and after statuses
        along with the assigned guest or employee information. The report is written to a text file, which is
        named based on the provided date and includes the room status and assignment details.

        Parameters:
            date (datetime): The date for which the daily report is generated. This date is used to format 
                            the report filename and to calculate status end dates for each room.

        Returns:
            str: The filename of the generated report.

        Report Content:
            - The report starts with a hotel management solution header.
            - For each room in `hotel_data`, it includes:
                - `CURRENT STATUS`: The current status of the room, including the assigned guest or employee's 
                name, role, and phone number, as well as the expected end date of the current status.
                - `NEXT STATUS`: The next scheduled status, with similar details about the next guest or 
                employee and their expected end date.
                - `AFTER STATUS`: The subsequent status, if available, with the same details.
        
        Date Calculation:
            - For each room, the method calculates the end date of the current, next, and after statuses 
            by adding the appropriate number of days (`current_endline`, `next_endline`, `after_endline`) 
            to the provided date.

        File Structure:
            - The report is written to a text file named `KAIROS_REPORT_<YYYY_MM_DD>.txt`, where the date 
            corresponds to the provided `date` argument.
            - The file contains formatted strings for each room with the room name and status details.
        
        Example Report Structure:
            ```
            PYLONE TEAM HOTEL MANAGEMENT SOLUTION
            KAIROS HOTEL SYSTEM

            Monday, September 24, 2024
            
            Room 101
            CURRENT STATUS  -  OCCUPIED  BY  John Doe - 555-1234  UNTIL  Wed Sep 25 2024
            NEXT STATUS     -  MAINTENANCE  BY  Housekeeper - Jane Doe  UNTIL  Thu Sep 26 2024
            AFTER STATUS    -  AVAILABLE  BY  Front Desk Manager  UNTIL  Fri Sep 27 2024
            ```

        Notes:
            - Guests and employees are assigned to room statuses. If the room's current, next, or after status 
            is not occupied, the report skips the details for that status.
            - The method uses the `timedelta` function to calculate future dates based on the room's 
            endline values.
            - Statuses without an associated guest or employee will only display the status without personal details.
        """
        today_name = date.strftime("%Y_%m_%d")
        today_file = date.strftime("%A, %B %d, %Y")
        file = f"KAIROS_REPORT_{today_name}.txt"

        with open(file, 'w') as report:
            report.write(f"PYLONE TEAM HOTEL MANAGEMENT SOLUTION\nKAIROS HOTEL SYSTEM\n\n{today_file}\n")
            for room in self._hotel_data:
                endlines = [room._current_endline, room._current_endline + room._next_endline, room._current_endline + room._next_endline + room._after_endline]
                dates = [(date + timedelta(days=endline)).strftime("%a %b %d %Y") for endline in endlines]
                current_date, next_date, after_date = dates

                assigned = self._guests[room._room_name]

                stat_1_report = f"CURRENT STATUS  -  {room._states[room._current_status]}"
                if room._current_status > 0: 
                    if isinstance(assigned[0], Guest):
                        stat_1_report += f"  BY  {assigned[0]._person_name[1]} {assigned[0]._person_name[0]} - {assigned[0]._person_phone}  UNTIL  {current_date}"
                    elif isinstance(assigned[0], Employee):
                        stat_1_report += f"  BY  {assigned[0]._employee_role} - {assigned[0]._person_name[1]} {assigned[0]._person_name[0]}  UNTIL  {current_date}"    
                else: pass

                stat_2_report = f"NEXT STATUS     -  {room._states[room._next_status]}"
                if room._next_status > 0: 
                    if isinstance(assigned[1], Guest):
                        stat_2_report += f"  BY  {assigned[1]._person_name[1]} {assigned[1]._person_name[0]} - {assigned[1]._person_phone}  UNTIL  {next_date}"
                    elif isinstance(assigned[1], Employee):
                        stat_2_report += f"  BY  {assigned[1]._employee_role} - {assigned[1]._person_name[1]} {assigned[1]._person_name[0]}  UNTIL  {next_date}"
                else: pass

                stat_3_report = f"AFTER STATUS    -  {room._states[room._after_status]}"
                if room._after_status > 0: 
                    if isinstance(assigned[2], Guest):
                        stat_3_report += f"  BY  {assigned[2]._person_name[1]} {assigned[2]._person_name[0]} - {assigned[2]._person_phone}  UNTIL  {after_date}"
                    elif isinstance(assigned[2], Employee):
                        stat_3_report += f"  BY  {assigned[2]._employee_role} - {assigned[2]._person_name[1]} {assigned[2]._person_name[0]}  UNTIL  {after_date}"
                else: pass

                report.write(f"\n   {room._room_name}\n{stat_1_report}\n{stat_2_report}\n{stat_3_report}\n")

        return f"{file}, created"
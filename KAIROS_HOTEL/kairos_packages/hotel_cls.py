import time
from kairos_packages.room_cls import Room, Simple_Room, Double_Room, Twin_Room, Family_Room
from kairos_packages.person_cls import Employee, Guest
        
class Hotel():
    def __init__(self, hotel_data: tuple[Room, ...] = (), employees: dict = None, guests: dict = None):
        self.hotel_data = hotel_data
        self.employees = employees
        self.guests = guests
    
    def to_dict(self) -> dict:
        return {"hotel_data": [room.to_dict() for room in self.hotel_data], 
                "employees": {role: emp.to_dict() for role, emp in self.employees.items()},
                "guests": {room_name: [guest.to_dict() if isinstance(guest, Guest) else {"employee_role": guest.employee_role} for guest in guests_list]
                           for room_name, guests_list in self.guests.items()}}
    @classmethod
    def from_dict(cls, data_dict):
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
                    # Find the employee object by matching employee role
                    employee = next(emp for emp in employees.values() if emp.employee_role == guest_data["employee_role"])
                    guests[room_name].append(employee)
                else:
                    guests[room_name].append(Guest.from_dict(guest_data))

        return cls(tuple(room_objects), employees, guests)

    def get_current_status(self) -> None:
        #current_status of each room
        print("  ROOM            STATUS")
        for room in self.hotel_data:
            print(room.get_current_status())
            time.sleep(1)   

    def get_complete_status(self) -> None:
        #current_status, next_status and after_status and endlines of each room
        print("  ROOM            CURRENT STATUS                  NEXT STATUS                   AFTER STATUS")
        for room in self.hotel_data:
            print(room.get_complete_status())
            time.sleep(1)

    def sunrise_protocol(self) -> None:
        #this checks if current_status has finished
        for room in self.hotel_data:
            print(room.sunrise_protocol())
            time.sleep(2)

    def sunset_protocol(self) -> None:
        #current_endline decreases by one
        for room in self.hotel_data:
            room.sunset_protocol()
        time.sleep(2)

    def noon_protocol(self) -> None:
        #updates one room status, based in various conditions
        option = int(input("\n""         OPTIONS                 TO DO" "\n"
                           "Reserve a Room                  press 1" "\n"
                           "Occupy a Room                   press 2" "\n"
                           "Schedule a Cleaning             press 3" "\n"
                           "Schedule a Maintenance          press 4" "\n"
                           "Disable a Room                  press 5" "\n"
                           "Return                          press 0" "\n"
                           "                                  -->  "))       

        if option == 0: pass            #return

        if option > 0:                  #scheduling a new status
            booking_rooms = []
            for room in self.hotel_data:
                if room.scheduling_conditions(option) is True:
                    booking_rooms.append(room)
                else: pass

            if len(booking_rooms) > 0:
                print("  ROOM             INFORMATION             UNTIL      TO DO")
                for b_room in booking_rooms:
                    print(f"{b_room.scheduling_data(option)}  -->  press {(booking_rooms.index(b_room) + 1)}")
                    time.sleep(1)
                book = int(input("Cancel                                                  press 0" "\n"
                                "                                                       "" -->  "))
                if book > 0 and book <= len(booking_rooms):
                    print(booking_rooms[book - 1].scheduling_protocol(option))
                if book == 0:
                    pass

            else: print("There are no rooms available to schedule that option.")
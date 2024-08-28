from kairos_packages.person_cls import Person, Guest, Employee

class Room():
    definition: str = "A part or division of a building enclosed by walls, floor, and ceiling"
    def __init__(self, room_data: list = None):

        if room_data is None:
            room_data = ["NOINFO", 0, 0, 0, 0, 0, 0]
        self.room_name = room_data[0]
        self.current_status = room_data[1]
        self.current_endline = room_data[2]
        self.next_status = room_data[3]
        self.next_endline = room_data[4]
        self.after_status = room_data[5]
        self.after_endline = room_data[6]

        self.states = ("NOINFO", "AVAILABLE", "RESERVED", "OCCUPIED", "CLEANING", "MAINTENANCE", "DISABLED")
        self.update_board = f" STATUS          TO DO\n{self.states[1]}       press 1\n{self.states[2]}        press 2\n{self.states[3]}        press 3\n{self.states[4]}        press 4\n{self.states[5]}     press 5\n{self.states[6]}        press 6\n"
        self.schedule_message = "Write the days to schedule"
        self.slowdown = "\n\t...\t...\t...\t..."
    
    def to_dict(self) -> dict:
        return {"room_name": self.room_name,
                "current_status": self.current_status,
                "current_endline": self.current_endline,
                "next_status": self.next_status,
                "next_endline": self.next_endline,
                "after_status": self.after_status,
                "after_endline": self.after_endline}
    @classmethod
    def from_dict(cls, data_dict):
        room_data = [data_dict["room_name"],
                     data_dict["current_status"],
                     data_dict["current_endline"],
                     data_dict["next_status"],
                     data_dict["next_endline"],
                     data_dict["after_status"],
                     data_dict["after_endline"]]
        return cls(room_data)


    def get_current_status(self) -> str:   
        #current_status of the room
        return f"{self.room_name}: \t {self.states[self.current_status]}."
    def get_complete_status(self) -> str:
        #current_status, next_status and after_status and endlines of the room
        return f"{self.room_name}:    {self.states[self.current_status]}    {self.current_endline} days left  -->  {self.states[self.next_status]}    {self.next_endline} days next  -->  {self.states[self.after_status]}    {self.after_endline} days after."


    def sunrise_protocol(self) -> str:
        #this checks if current_status has finished
        status_update = f"{self.room_name}: no information was found, please check.{self.slowdown}"
        
        #returns current_status and current_endline
        if self.current_endline > 0:
            status_update = f"{self.room_name} is {self.states[self.current_status]}, {self.current_endline} days left.{self.slowdown}"

        #current_status finished and next_status exist
        elif self.current_endline == 0 and self.next_endline > 0:
            status_update = f"{self.room_name} went from {self.states[self.current_status]} to {self.states[self.next_status]}.{self.slowdown}"
            self.current_status, self.current_endline = self.next_status, self.next_endline
            self.next_status, self.next_endline = self.after_status, self.after_endline
            self.after_status, self.after_endline = 0, 0

        #current_status finished and next_state doesn't exist
        elif self.current_endline == 0 and self.next_endline == 0:
            update_notice = int(input(f"{self.room_name} finished {self.states[self.current_status]}, an update is needed:\n{self.update_board}\t\t  --> "))

            #the room becomes AVAILABLE for one day
            if update_notice == 1:
                self.current_status, self.current_endline = 1, 1
                status_update = f"{self.room_name} is now {self.states[self.current_status]}.{self.slowdown}"

            #the room becomes RESERVED, then OCCUPIED
            elif update_notice == 2:
                schedule_update_1 = int(input(f"{self.states[2]}:  {self.schedule_message}\n  --> "))
                self.current_status, self.current_endline = 2, schedule_update_1
                schedule_update_2 = int(input(f"{self.states[3]}:  {self.schedule_message}\n  --> "))
                self.next_status, self.next_endline = 3, schedule_update_2
                status_update = f"{self.room_name} is now {self.states[self.current_status]}.{self.slowdown}"

            #the room becomes OCCUPIED, then one CLEANING day
            elif update_notice == 3:
                schedule_update_1 = int(input(f"{self.states[3]}:  {self.schedule_message}\n  --> "))
                self.current_status, self.current_endline = 3, schedule_update_1
                self.next_status, self.next_endline = 4, 1
                status_update = f"{self.room_name} is now {self.states[self.current_status]}.{self.slowdown}"

            #the room has one CLEANING day, the next one day becomes AVAILABLE
            elif update_notice == 4:
                self.current_status, self.current_endline = 4, 1
                self.next_status, self.next_endline = 1, 1
                status_update = f"{self.room_name} is now {self.states[self.current_status]}.{self.slowdown}"

            #the room is now on MAINTENANCE, the next one day becomes CLEANING
            elif update_notice == 5:
                schedule_update_1 = int(input(f"{self.states[5]}:  {self.schedule_message}\n  --> "))
                self.current_status, self.current_endline = 5, schedule_update_1
                self.next_status, self.next_endline = 4, 1
                status_update = f"{self.room_name} is now {self.states[self.current_status]}.{self.slowdown}"

            #the room is now DISABLED, the following status requires an update
            elif update_notice == 6:
                schedule_update_1 = int(input(f"{self.states[6]}:  {self.schedule_message}\n  --> "))
                self.current_status, self.current_endline = 6, schedule_update_1
                update_notice = int(input(f"{self.room_name} is now {self.states[self.current_status]}, the next status needs to be updated:\n{self.update_board}"))
                schedule_update_2 = int(input(f"{self.states[update_notice]}:  {self.schedule_message}\n  --> "))
                self.next_status, self.next_endline = update_notice, schedule_update_2
                status_update = f"{self.room_name} becomes {self.states[self.current_status]}.{self.slowdown}"
                
        return status_update


    def scheduling_conditions(self, option: int) -> bool:
         #check the conditions associated with each status according to the conditional_status, in the conditions dict
        conditions = {"c_status_eq1__n_endline_eq0": self.current_status == 1 and self.next_endline == 0,
                      "c_status_geq1__n_endline_eq0": self.current_status >= 1 and self.next_endline == 0,
                      "n_status_eq1__a_endline_eq0": self.next_status == 1 and self.after_endline == 0,
                      "n_status_geq1__a_endline_eq0": self.next_status >= 1 and self.after_endline == 0,
                      "a_status_eq1": self.after_status == 1,
                      "c_status_eq3__n_endline_eq0": self.current_status == 3 and self.next_endline == 0,
                      "n_status_eq3__a_endline_eq0": self.next_status == 3 and self.after_endline == 0,
                      "c_status_neq4__a_endline_eq1": self.current_status != 4 and self.next_status == 1 and self.after_endline == 0,
                      "n_status_neq4__a_status_eq1": self.next_status != 4 and self.after_status == 1,
                      "c_status_eq5__n_endline_eq0": self.current_status == 5 and self.next_endline == 0,
                      "n_status_eq5__a_endline_eq0": self.next_status == 5 and self.after_endline == 0,
                      "c_status_eq6__n_endline_eq0": self.current_status == 6 and self.next_endline == 0,
                      "n_status_eq6__a_endline_eq0": self.next_status == 6 and self.after_endline == 0,
                      "c_status_l6__n_endline_eq0": self.current_status < 6 and self.next_endline == 0,
                      "n_status_l6__a_endline_eq0": self.next_status < 6 and self.after_endline == 0}
         
        conditional_status = [# reserve
                              ["c_status_eq1__n_endline_eq0", "c_status_geq1__n_endline_eq0", "n_status_eq1__a_endline_eq0"],
                              # occupy
                              ["c_status_eq1__n_endline_eq0", "c_status_geq1__n_endline_eq0", "n_status_eq1__a_endline_eq0", "n_status_geq1__a_endline_eq0", "a_status_eq1"],
                              # clean
                              ["c_status_eq3__n_endline_eq0", "n_status_eq3__a_endline_eq0", "c_status_eq5__n_endline_eq0", "n_status_eq5__a_endline_eq0", "c_status_eq6__n_endline_eq0", "n_status_eq6__a_endline_eq0"],
                              # maintain
                              ["c_status_eq1__n_endline_eq0", "c_status_neq4__a_endline_eq1", "n_status_neq4__a_status_eq1", "c_status_eq3__n_endline_eq0", "n_status_eq3__a_endline_eq0", "c_status_eq6__n_endline_eq0", "n_status_eq6__a_endline_eq0"],
                              # disable
                              ["c_status_eq1__n_endline_eq0", "n_status_eq1__a_endline_eq0", "a_status_eq1", "c_status_l6__n_endline_eq0", "n_status_l6__a_endline_eq0"]]

        room_conditions = conditional_status[option - 1]
        return any(conditions[c] for c in room_conditions)      


    def scheduling_data(self, option: int) -> str:
        #the different possible outputs
        schedule_type = (f"{self.room_name}: no information was found, please check", 
                         f"{self.room_name}: ({self.definition})  -->  RIGHT NOW",
                         f"{self.room_name}: ({self.definition})  -->  {self.current_endline} DAYS",
                         f"{self.room_name}: ({self.definition})  -->  {self.current_endline + self.next_endline} DAYS",
                         f"{self.room_name}:       {self.states[self.current_status]}        -->  RIGHT NOW",
                         f"{self.room_name}:       {self.states[self.current_status]}        -->  {self.current_endline} DAYS",
                         f"{self.room_name}: {self.states[self.current_status]} --- {self.states[self.next_status]}  -->  {self.current_endline + self.next_endline} DAYS")
        schedule_data = schedule_type[0]

        #dictionary, option asign a key, and the value is a list of tuples, each contain condition and output
        conditions = {1: [(self.current_status == 1 and self.next_endline == 0, schedule_type[1]),
                          (self.current_status >= 1 and self.next_endline == 0, schedule_type[2]),
                          (self.next_status == 1 and self.after_endline == 0, schedule_type[2])],
                      2: [(self.current_status == 1 and self.next_endline == 0, schedule_type[1]),
                          (self.current_status >= 1 and self.next_endline == 0, schedule_type[2]),
                          (self.next_status == 1 and self.after_endline == 0, schedule_type[2]),
                          (self.next_status >= 1 and self.after_endline == 0, schedule_type[3]),
                          (self.after_status == 1, schedule_type[3])],
                      3: [(self.current_status == 3 and self.next_endline == 0, schedule_type[5]),
                          (self.next_status == 3 and self.after_endline == 0, schedule_type[6]),
                          (self.current_status == 5 and self.next_endline == 0, schedule_type[5]),
                          (self.next_status == 5 and self.after_endline == 0, schedule_type[6]),
                          (self.current_status == 6 and self.next_endline == 0, schedule_type[5]),
                          (self.next_status == 6 and self.after_endline == 0, schedule_type[6])],
                      4: [(self.current_status == 1 and self.next_endline == 0, schedule_type[4]),
                          (self.next_status == 1 and self.after_endline == 0, schedule_type[5]),
                          (self.after_status == 1, schedule_type[6]),
                          (self.current_status == 3 and self.next_endline == 0, schedule_type[5]),
                          (self.next_status == 3 and self.after_endline == 0, schedule_type[6]),
                          (self.current_status == 6 and self.next_endline == 0, schedule_type[5]),
                          (self.next_status == 6 and self.after_endline == 0, schedule_type[6])],
                      5: [(self.current_status == 1 and self.next_endline == 0, schedule_type[4]),
                          (self.next_status == 1 and self.after_endline == 0, schedule_type[5]),
                          (self.after_status == 1, schedule_type[6]),
                          (self.current_status < 6 and self.next_endline == 0, schedule_type[5]),
                          (self.next_status < 6 and self.after_endline == 0, schedule_type[6])]}

        #checks the list of tuples asignated by the option, returns an output if the condition is True
        for condition, result in conditions.get(option, []):
            if condition:
                schedule_data = result
                break
            
        return schedule_data


    def scheduling_protocol(self, option: int) -> str:

        status_update = f"{self.room_name}: no information was found, please check.{self.slowdown}"

        if option == 1:         #RESERVE
            #updates one room with the RESERVED status and the subsequent OCCUPIED status

            schedule_update_1 = int(input(f"{self.states[2]}:  {self.schedule_message}\n  --> "))
            schedule_update_2 = int(input(f"{self.states[3]}:  {self.schedule_message}\n  --> "))

            if self.current_status == 1 and self.next_endline == 0:
                #the room is AVAILABLE right now and there is no posterior time limit
                self.current_status, self.current_endline = 2, schedule_update_1
                self.next_status, self.next_endline = 3, schedule_update_2

            elif self.current_status >= 1 and self.next_endline == 0:
                #the room is in a non-AVAILABLE state right now and there is no posterior time limit
                self.next_status, self.next_endline = 2, schedule_update_1
                self.after_status, self.after_endline = 3, schedule_update_2

            elif self.next_status == 1 and self.after_endline == 0:
                #the room will be AVAILABLE right after and there is no posterior time limit
                self.next_status, self.next_endline = 2, schedule_update_1
                self.after_status, self.after_endline = 3, schedule_update_2

            status_update = f"{self.room_name} has been {self.states[2]}.{self.slowdown}"
            

        elif option == 2:         #OCCUPY
            #updates one room with the subsequent OCCUPIED status

            schedule_update_1 = int(input(f"{self.states[3]}:  {self.schedule_message}\n  --> "))

            if self.current_status == 1 and self.next_endline == 0:
                #the room current_status is AVAILABLE and next_status has no time limit or is unexistent
                self.current_status, self.current_endline = 3, schedule_update_1

            elif self.current_status >= 1 and self.next_endline == 0:
                #the room current_status is non-AVAILABLE and next_status has no time limit or is unexistent
                self.next_status, self.next_endline = 3, schedule_update_1

            elif self.next_status == 1 and self.after_endline == 0:
                #the room next_status is AVAILABLE and after_status has no time limit or is unexistent
                self.next_status, self.next_endline = 3, schedule_update_1

            elif self.next_status >= 1 and self.after_endline == 0:
                #the room next_status is non-AVAILABLE and after_status has no time limit or is unexistent
                self.after_status, self.after_endline = 3, schedule_update_1

            elif self.after_status == 1:
                #the room after_status is AVAILABLE
                self.after_status, self.after_endline = 3, schedule_update_1

            status_update = f"{self.room_name} has been {self.states[3]}.{self.slowdown}"


        elif option == 3:         #CLEANING
            #updates one room with the CLEANING status

            schedule_update_1 = int(input(f"{self.states[4]}:  {self.schedule_message}\n  --> "))

            if self.current_status == 3 and self.next_endline == 0:
                #the room current_status is OCCUPIED and next_status has no time limit or is unexistent
                self.next_status, self.next_endline = 4, schedule_update_1

            elif self.next_status == 3 and self.after_endline == 0:
                #the room next_status is OCCUPIED and after_status has no time limit or is unexistent
                self.after_status, self.after_endline = 4, schedule_update_1

            elif self.current_status == 5 and self.next_endline == 0:
                #the room current_status is MAINTENANCE and next_status has no time limit or is unexistent
                self.next_status, self.next_endline = 4, schedule_update_1

            elif self.next_status == 5 and self.after_endline == 0:
                #the room next_status is MAINTENANCE and after_status has no time limit or is unexistent
                self.after_status, self.after_endline = 4, schedule_update_1

            elif self.current_status == 6 and self.next_endline == 0:
                #the room current_status is DISABLED and next_status has no time limit or is unexistent
                self.next_status, self.next_endline = 4, schedule_update_1

            elif self.next_status == 6 and self.after_endline == 0:
                #the room next_status is DISABLED and after_status has no time limit or is unexistent
                self.after_status, self.after_endline = 4, schedule_update_1

            status_update = f"{self.room_name} has scheduled a {self.states[4]}.{self.slowdown}"


        elif option == 4:         #MAINTENANCE
            #updates one room with the MAINTENANCE status

            schedule_update_1 = int(input(f"{self.states[5]}:  {self.schedule_message}\n  --> "))

            if self.current_status == 1 and self.next_endline == 0:
                #the room current_status is AVAILABLE and next_status has no time limit or is unexistent
                self.current_status, self.current_endline = 5, schedule_update_1

            elif self.next_status == 1 and self.after_endline == 0:
                #the room next_status is AVAILABLE and after_status has no time limit or is unexistent
                self.next_status, self.next_endline = 5, schedule_update_1

            elif self.after_status == 1:
            #the room after_status is AVAILABLE
                self.after_status, self.after_endline = 5, schedule_update_1

            elif self.current_status == 3 and self.next_endline == 0:
                #the room current_status is OCCUPIED and next_status has no time limit or is unexistent
                self.next_status, self.next_endline = 5, schedule_update_1

            elif self.next_status == 3 and self.after_endline == 0:
                #the room next_status is OCCUPIED and after_status has no time limit or is unexistent
                self.after_status, self.after_endline = 5, schedule_update_1

            elif self.current_status == 6 and self.next_endline == 0:
                #the room current_status is DISABLED and next_status has no time limit or is unexistent
                self.next_status, self.next_endline = 5, schedule_update_1

            elif self.next_status == 6 and self.after_endline == 0:
                #the room next_status is DISABLED and after_status has no time limit or is unexistent
                self.after_status, self.after_endline = 5, schedule_update_1

            status_update = f"{self.room_name} has scheduled a {self.states[5]}.{self.slowdown}"


        elif option == 5:         #DISABLED
            #updates one room with the DISABLED status

            schedule_update_1 = int(input(f"{self.states[6]}:  {self.schedule_message}\n  --> "))

            if self.current_status == 1 and self.next_endline == 0:
                #the room current_status is AVAILABLE and next_status has no time limit or is unexistent
                self.current_status, self.current_endline = 6, schedule_update_1

            elif self.next_status == 1 and self.after_endline == 0:
            #the room next_status is AVAILABLE and after_status has no time limit or is unexistent
                self.next_status, self.next_endline = 6, schedule_update_1

            elif self.after_status == 1:
            #the room after_status is AVAILABLE
                self.after_status, self.after_endline = 6, schedule_update_1

            elif self.current_status < 6 and self.next_endline == 0:
                #the room current_status is non-DISABLED and next_status has no time limit or is unexistent
                self.next_status, self.next_endline = 6, schedule_update_1

            elif self.next_status < 6 and self.after_endline == 0:
                #the room next_status is non-DISABLED and after_status has no time limit or is unexistent
                self.after_status, self.after_endline = 6, schedule_update_1


            status_update = f"{self.room_name} has been {self.states[6]}.{self.slowdown}"

        return status_update

    def sunset_protocol(self) -> None:
        #current_endline decreases by one
        self.current_endline = self.current_endline - 1


class Simple_Room(Room):
    definition: str = "Simple Bed, One Bathroom"
    def __init__(self, room_data: list = None):
        super().__init__(room_data)
    def to_dict(self) -> dict:
        base_dict = super().to_dict()
        base_dict["type"] = "Simple_Room"
        return base_dict

class Double_Room(Room):
    definition: str = "Large Bed, One Bathroom"
    def __init__(self, room_data: list = None):
        super().__init__(room_data)
    def to_dict(self) -> dict:
        base_dict = super().to_dict()
        base_dict["type"] = "Double_Room"
        return base_dict

class Twin_Room(Room):
    definition: str = "Two Beds, Two Bathrooms"
    def __init__(self, room_data: list = None):
        super().__init__(room_data)
    def to_dict(self) -> dict:
        base_dict = super().to_dict()
        base_dict["type"] = "Twin_Room"
        return base_dict

class Family_Room(Room):
    definition: str = "Three Beds, Two Bathrooms"
    def __init__(self, room_data: list = None):
        super().__init__(room_data)
    def to_dict(self) -> dict:
        base_dict = super().to_dict()
        base_dict["type"] = "Family_Room"
        return base_dict
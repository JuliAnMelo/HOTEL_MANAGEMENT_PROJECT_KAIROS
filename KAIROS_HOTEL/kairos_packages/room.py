class Room():
    """
    A class to represent a room within a Hotel object.
    """
    definition: str = "A part or division of a building enclosed by walls, floor, and ceiling"
    def __init__(self, room_data: list = None):

        if room_data is None:
            room_data = ["NOINFO", 0, 0, 0, 0, 0, 0]
        self._room_name = room_data[0]
        self._current_status = room_data[1]
        self._current_endline = room_data[2]
        self._next_status = room_data[3]
        self._next_endline = room_data[4]
        self._after_status = room_data[5]
        self._after_endline = room_data[6]

        self._states = ("NOINFO", "AVAILABLE", "RESERVED", "OCCUPIED", "CLEANING", "MAINTENANCE", "DISABLED")
        self._update_board = f"\n STATUS          TO DO\n{self._states[1]}       press 1\n{self._states[2]}        press 2\n{self._states[3]}        press 3\n{self._states[4]}        press 4\n{self._states[5]}     press 5\n{self._states[6]}        press 6\n"
        self._schedule_message = "Write the days to schedule"
        self._slowdown = "\n\t...\t...\t...\t..."
    
    def to_dict(self) -> dict:
        """
        Converts the Room object into a dictionary representation.
        """
        return {"room_name": self._room_name,
                "current_status": self._current_status,
                "current_endline": self._current_endline,
                "next_status": self._next_status,
                "next_endline": self._next_endline,
                "after_status": self._after_status,
                "after_endline": self._after_endline}
    
    @classmethod
    def from_dict(cls, data_dict: dict):
        """
        Creates a Room object from a dictionary representation.
        """
        room_data = [data_dict["room_name"],
                     data_dict["current_status"],
                     data_dict["current_endline"],
                     data_dict["next_status"],
                     data_dict["next_endline"],
                     data_dict["after_status"],
                     data_dict["after_endline"]]
        return cls(room_data)


    def get_current_status(self) -> str:   
        """
        Retrieves the current status of the room in a formatted string.

        Return
            A string indicating the name of the room along with its current status.
        """
        return f"{self._room_name}:  {self._states[self._current_status]}"
    

    def get_complete_status(self) -> str:
        """
        Retrieves the complete status of the room, including current, next, and after statuses.

        Returns
            A formatted string that provides a detailed overview of the room's status.
        """
        return f"{self._room_name}:    {self._states[self._current_status]}    {self._current_endline} days left  -  {self._states[self._next_status]}    {self._next_endline} days next  -  {self._states[self._after_status]}    {self._after_endline} days after"

    
    def scheduling_conditions(self, option: int) -> bool:
        """
        Checks if the scheduling conditions for the room are met based on the current, next, and after statuses.

        Parameters
            An integer representing the action for which scheduling conditions are being evaluated. 
            The option corresponds to specific actions like reserve, occupy, clean, maintain, or disable.

        Returns
            True if at least one of the conditions for the specified option is satisfied, 
            otherwise False.

        The method evaluates the current status of the room against predefined conditions 
        stored in a dictionary. 

        Each group contains condition keys that reference the conditions dictionary to determine 
        if the room can be scheduled for the selected action.
        """
        conditions = {"c_status_eq1__n_endline_eq0": self._current_status == 1 and self._next_endline == 0,
                      "c_status_geq1__n_endline_eq0": self._current_status >= 1 and self._next_endline == 0,
                      "n_status_eq1__a_endline_eq0": self._next_status == 1 and self._after_endline == 0,
                      "n_status_geq1__a_endline_eq0": self._next_status >= 1 and self._after_endline == 0,
                      "a_status_eq1": self._after_status == 1,
                      "c_status_eq3__n_endline_eq0": self._current_status == 3 and self._next_endline == 0,
                      "n_status_eq3__a_endline_eq0": self._next_status == 3 and self._after_endline == 0,
                      "c_status_neq4__a_endline_eq1": self._current_status != 4 and self._next_status == 1 and self._after_endline == 0,
                      "n_status_neq4__a_status_eq1": self._next_status != 4 and self._after_status == 1,
                      "c_status_eq5__n_endline_eq0": self._current_status == 5 and self._next_endline == 0,
                      "n_status_eq5__a_endline_eq0": self._next_status == 5 and self._after_endline == 0,
                      "c_status_eq6__n_endline_eq0": self._current_status == 6 and self._next_endline == 0,
                      "n_status_eq6__a_endline_eq0": self._next_status == 6 and self._after_endline == 0,
                      "c_status_l6__n_endline_eq0": self._current_status < 6 and self._next_endline == 0,
                      "n_status_l6__a_endline_eq0": self._next_status < 6 and self._after_endline == 0}
         
        conditional_status = [["c_status_eq1__n_endline_eq0", "c_status_geq1__n_endline_eq0", "n_status_eq1__a_endline_eq0"],
                              ["c_status_eq1__n_endline_eq0", "c_status_geq1__n_endline_eq0", "n_status_eq1__a_endline_eq0", "n_status_geq1__a_endline_eq0", "a_status_eq1"],
                              ["c_status_eq3__n_endline_eq0", "n_status_eq3__a_endline_eq0", "c_status_eq5__n_endline_eq0", "n_status_eq5__a_endline_eq0", "c_status_eq6__n_endline_eq0", "n_status_eq6__a_endline_eq0"],
                              ["c_status_eq1__n_endline_eq0", "c_status_neq4__a_endline_eq1", "n_status_neq4__a_status_eq1", "c_status_eq3__n_endline_eq0", "n_status_eq3__a_endline_eq0", "c_status_eq6__n_endline_eq0", "n_status_eq6__a_endline_eq0"],
                              ["c_status_eq1__n_endline_eq0", "n_status_eq1__a_endline_eq0", "a_status_eq1", "c_status_l6__n_endline_eq0", "n_status_l6__a_endline_eq0"]]

        room_conditions = conditional_status[option - 1]
        return any(conditions[c] for c in room_conditions)      


    def scheduling_data(self, option: int) -> str:
        """
        Determines and returns a formatted string that describes the scheduling data of the room based on 
        the current, next, and after statuses, along with the number of days associated with these statuses.

        Parameters
            An integer representing the type of action for which scheduling data is requested. 
            The option corresponds to specific actions like reserve, occupy, clean, maintain, or disable.

        Returns
            A formatted string that provides detailed scheduling information about the room 
            depending on its current and future statuses. The result includes descriptions of 
            the room’s condition and timeline (e.g., "RIGHT NOW", "X DAYS", etc.).

        - The method defines a tuple `schedule_type` that contains preformatted strings for various 
        conditions of the room, such as no information, current, next, and after statuses, and the 
        corresponding days left.
        - Based on the `option` passed, the method checks certain predefined conditions stored in the 
        `conditions` dictionary, evaluating the room's current and next statuses.
        - For each `option`, the method loops through condition-result pairs, returning the result when 
        the corresponding condition is met.
        """
        schedule_type = (f"{self._room_name}: no information was found, please check", 
                         f"{self._room_name}: ({self.definition})  -  RIGHT NOW",
                         f"{self._room_name}: ({self.definition})  -  {self._current_endline} DAYS",
                         f"{self._room_name}: ({self.definition})  -  {self._current_endline + self._next_endline} DAYS",
                         f"{self._room_name}:       {self._states[self._current_status]}        -  RIGHT NOW",
                         f"{self._room_name}:       {self._states[self._current_status]}        -  {self._current_endline} DAYS",
                         f"{self._room_name}: {self._states[self._current_status]} --- {self._states[self._next_status]}  -  {self._current_endline + self._next_endline} DAYS")
        schedule_data = schedule_type[0]

        conditions = {1: [(self._current_status == 1 and self._next_endline == 0, schedule_type[1]),
                          (self._current_status >= 1 and self._next_endline == 0, schedule_type[2]),
                          (self._next_status == 1 and self._after_endline == 0, schedule_type[2])],
                      2: [(self._current_status == 1 and self._next_endline == 0, schedule_type[1]),
                          (self._current_status >= 1 and self._next_endline == 0, schedule_type[2]),
                          (self._next_status == 1 and self._after_endline == 0, schedule_type[2]),
                          (self._next_status >= 1 and self._after_endline == 0, schedule_type[3]),
                          (self._after_status == 1, schedule_type[3])],
                      3: [(self._current_status == 3 and self._next_endline == 0, schedule_type[5]),
                          (self._next_status == 3 and self._after_endline == 0, schedule_type[6]),
                          (self._current_status == 5 and self._next_endline == 0, schedule_type[5]),
                          (self._next_status == 5 and self._after_endline == 0, schedule_type[6]),
                          (self._current_status == 6 and self._next_endline == 0, schedule_type[5]),
                          (self._next_status == 6 and self._after_endline == 0, schedule_type[6])],
                      4: [(self._current_status == 1 and self._next_endline == 0, schedule_type[4]),
                          (self._next_status == 1 and self._after_endline == 0, schedule_type[5]),
                          (self._after_status == 1, schedule_type[6]),
                          (self._current_status == 3 and self._next_endline == 0, schedule_type[5]),
                          (self._next_status == 3 and self._after_endline == 0, schedule_type[6]),
                          (self._current_status == 6 and self._next_endline == 0, schedule_type[5]),
                          (self._next_status == 6 and self._after_endline == 0, schedule_type[6])],
                      5: [(self._current_status == 1 and self._next_endline == 0, schedule_type[4]),
                          (self._next_status == 1 and self._after_endline == 0, schedule_type[5]),
                          (self._after_status == 1, schedule_type[6]),
                          (self._current_status < 6 and self._next_endline == 0, schedule_type[5]),
                          (self._next_status < 6 and self._after_endline == 0, schedule_type[6])]}

        for condition, result in conditions.get(option, []):
            if condition:
                schedule_data = result
                break
            
        return schedule_data


    def scheduling_protocol(self, option: int) -> str:
        """
        Updates the room's scheduling status based on the selected option and user inputs for the 
        number of days. This method updates the room's status (e.g., RESERVED, OCCUPIED, CLEANING) 
        and schedules the next relevant status depending on the current state.

        Parameters
            An integer representing the action to perform on the room's schedule. 
            The available options correspond to:
            1: Reserve the room
            2: Occupy the room
            3: Schedule cleaning for the room
            4: Schedule maintenance for the room
            5: Disable the room (mark it as unavailable)

        Returns
            A string message confirming the scheduling update or an error message 
            if the operation could not be performed.

        Notes
        - This method prompts the user to input the number of days for which a particular status should 
        be applied to the room. The input is taken via `input()` for each status update.
        - The method uses the current, next, and after statuses to apply updates. Depending on the current 
        state of the room, it updates one or more of the following:
            - `current_status`, `current_endline`
            - `next_status`, `next_endline`
            - `after_status`, `after_endline`
        - Each `option` represents a different scheduling operation. Based on the room's current schedule 
        and the option selected, this method assigns new values for the room's future statuses.

        Option 1: Reserve the Room
        - Updates the room to "RESERVED" and schedules it to be "OCCUPIED" afterward.

        Option 2: Occupy the Room
        - Directly updates the room to "OCCUPIED", taking into account any future statuses.

        Option 3: Cleaning
        - Schedules the room for cleaning after being "OCCUPIED", "MAINTENANCE", or "DISABLED".

        Option 4: Maintenance
        - Schedules the room for maintenance based on its current or future status.

        Option 5: Disable the Room
        - Marks the room as "DISABLED" and unavailable for any further reservations or usage.
        """
        status_update = f"\n{self._room_name}: An error has raised, please try again.{self._slowdown}"

        if option == 1:         
            schedule_update_1 = int(input(f"{self._states[2]}:  {self._schedule_message}\n  --> "))
            schedule_update_2 = int(input(f"{self._states[3]}:  {self._schedule_message}\n  --> "))

            if self._current_status == 1 and self._next_endline == 0:
                self._current_status, self._current_endline = 2, schedule_update_1
                self._next_status, self._next_endline = 3, schedule_update_2
                
            elif self._current_status >= 1 and self._next_endline == 0:
                self._next_status, self._next_endline = 2, schedule_update_1
                self._after_status, self._after_endline = 3, schedule_update_2

            elif self._next_status == 1 and self._after_endline == 0:
                self._next_status, self._next_endline = 2, schedule_update_1
                self._after_status, self._after_endline = 3, schedule_update_2

            status_update = f"{self._room_name} has been {self._states[2]}.{self._slowdown}"
            

        elif option == 2:
            schedule_update_1 = int(input(f"\n{self._states[3]}:  {self._schedule_message}\n  --> "))

            if self._current_status == 1 and self._next_endline == 0:
                self._current_status, self._current_endline = 3, schedule_update_1

            elif self._current_status >= 1 and self._next_endline == 0:
                self._next_status, self._next_endline = 3, schedule_update_1

            elif self._next_status == 1 and self._after_endline == 0:
                self._next_status, self._next_endline = 3, schedule_update_1

            elif self._next_status >= 1 and self._after_endline == 0:
                self._after_status, self._after_endline = 3, schedule_update_1

            elif self._after_status == 1:
                self._after_status, self._after_endline = 3, schedule_update_1

            status_update = f"{self._room_name} has been {self._states[3]}.{self._slowdown}"


        elif option == 3:
            schedule_update_1 = int(input(f"\n{self._states[4]}:  {self._schedule_message}\n  --> "))

            if self._current_status == 3 and self._next_endline == 0:
                self._next_status, self._next_endline = 4, schedule_update_1

            elif self._next_status == 3 and self._after_endline == 0:
                self._after_status, self._after_endline = 4, schedule_update_1

            elif self._current_status == 5 and self._next_endline == 0:
                self._next_status, self._next_endline = 4, schedule_update_1

            elif self._next_status == 5 and self._after_endline == 0:
                self._after_status, self._after_endline = 4, schedule_update_1

            elif self._current_status == 6 and self._next_endline == 0:
                self._next_status, self._next_endline = 4, schedule_update_1

            elif self._next_status == 6 and self._after_endline == 0:
                self._after_status, self._after_endline = 4, schedule_update_1

            status_update = f"{self._room_name} has scheduled a {self._states[4]}.{self._slowdown}"


        elif option == 4:
            schedule_update_1 = int(input(f"\n{self._states[5]}:  {self._schedule_message}\n  --> "))

            if self._current_status == 1 and self._next_endline == 0:
                self._current_status, self._current_endline = 5, schedule_update_1

            elif self._next_status == 1 and self._after_endline == 0:
                self._next_status, self._next_endline = 5, schedule_update_1

            elif self._after_status == 1:
                self._after_status, self._after_endline = 5, schedule_update_1

            elif self._current_status == 3 and self._next_endline == 0:
                self._next_status, self._next_endline = 5, schedule_update_1

            elif self._next_status == 3 and self._after_endline == 0:
                self._after_status, self._after_endline = 5, schedule_update_1

            elif self._current_status == 6 and self._next_endline == 0:
                self._next_status, self._next_endline = 5, schedule_update_1

            elif self._next_status == 6 and self._after_endline == 0:
                self._after_status, self._after_endline = 5, schedule_update_1

            status_update = f"{self._room_name} has scheduled a {self._states[5]}.{self._slowdown}"


        elif option == 5:
            schedule_update_1 = int(input(f"\n{self._states[6]}:  {self._schedule_message}\n  --> "))

            if self._current_status == 1 and self._next_endline == 0:
                self._current_status, self._current_endline = 6, schedule_update_1

            elif self._next_status == 1 and self._after_endline == 0:
                self._next_status, self._next_endline = 6, schedule_update_1

            elif self._after_status == 1:
                self._after_status, self._after_endline = 6, schedule_update_1

            elif self._current_status < 6 and self._next_endline == 0:
                self._next_status, self._next_endline = 6, schedule_update_1

            elif self._next_status < 6 and self._after_endline == 0:
                self._after_status, self._after_endline = 6, schedule_update_1

            status_update = f"{self._room_name} has been {self._states[6]}.{self._slowdown}"


        return status_update



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
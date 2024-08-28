# Object Oriented Programming Project: Kairos Hotel
## Concept
The idea raises by looking for a OOP application, an aplication with an emphasis on information management and that it was motivating for the Python coding.
This hotel idea has a focus on representing the room management concept, being represented with predetermined variables, which are condensated in the Python classes designed for that: `Room` and `Hotel`

## **The `Room` class**
### Definition
```python
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
```
As we can see, `Room`'s `__init__`  is represented by `room_data`, a `list`, this is designed like that because by the moment, is easier to ad objects to a undetermined length list than define each one at the `__init__`, so let's see what exactly is a Room in this project:

| `Room.room_data` index | `self.` Attribute | Description |
| ------------ | ------------ | ------------ |
| `room_data[0]` | `room_name` | A `str` that identifies the room |
| `room_data[1]` | `current_status` | An `int` that represents the current "activity" of the room |
| `room_data[2]` | `current_endline` | An `int` that represent the current "activity" days left to end |
| `room_data[3]` | `next_status` | An `int` that represents the "next activity" of the room |
| `room_data[4]` | `next_endline` | An `int` that represent the "next activity" days left to end |
| `room_data[5]` | `after_status` | An `int` that represents the "after activity" of the room |
| `room_data[6]` | `after_endline` | An `int` that represent the "after activity" days left to end |

You may notice the "An `int` that represents the activity of the room" quote, that refers to one of the atributes those are independent of `room_data`:

```python
self.states = ("NOINFO", "AVAILABLE", "RESERVED", "OCCUPIED", "CLEANING", "MAINTENANCE", "DISABLED")
self.update_board = f" STATUS          TO DO\n
                      {self.states[1]}       press 1\n
                      {self.states[2]}        press 2\n
                      {self.states[3]}        press 3\n
                      {self.states[4]}        press 4\n
                      {self.states[5]}     press 5\n
                      {self.states[6]}        press 6\n"
self.schedule_message = "Write the days to schedule"
self.slowdown = "\n\t...\t...\t...\t..."
```
Let's see:
| `self.` Attribute | Description |
| ------------ | ------------ |
| `states` | All three `_status` attributes refers to the `self.states` index. |
| `update_board` | Used in the methods those modifies `_status` and `_endline` attributes. |
| `schedule_message` |Used in the methods those modifies `_status` and `_endline` attributes. |
| `slowdown` | An artificial delay in the methods execution for testing quality purposes. |

### The `Room` Methods
```python
def get_current_status(self) -> str:   
    #...
    #code
       
def get_complete_status(self) -> str:
    #...
    #code

def sunrise_protocol(self) -> str:
    #...
    #code
    #...
    #more code
    #...
    #even more code
    #...

def scheduling_conditions(self, option: int) -> bool:
    #...
    #code
    #...
    #more code
    #...
    #even more code
    #...

def def scheduling_data(self, option: int) -> str:
    #...
    #code
    #...
    #more code
    #...
    #even more code
    #...

def scheduling_protocol(self, option: int) -> str:
    #...
    #code
    #...
    #more code
    #...
    #even more code
    #...

def sunset_protocol(self) -> None:
    #...
    #code
```
**The complete code is below:**

- `get_current_status(self)`
<details><summary>Details</summary>
<p>
  
  ```python
  def get_current_status(self) -> str:   
        return f"{self.room_name}: \t {self.states[self.current_status]}."
  ```
  Only returns the `current_status` of the room

</p>
</details>


- `get_complete_status(self)`
<details><summary>Details</summary>
<p>
  
  ```python
  def get_complete_status(self) -> str:   
        return f"{self.room_name}:    {self.states[self.current_status]}    {self.current_endline} days left  -->  {self.states[self.next_status]}    {self.next_endline} days next  -->  {self.states[self.after_status]}    {self.after_endline} days after."

  ```
  Returns `current_status`, `next_status`, `after_status` and `_endline`'s of the room
</p>
</details>


- `sunrise_protocol(self)`
<details><summary>Details</summary>
<p>
  
  ```python
  def sunrise_protocol(self) -> str:
        status_update = f"{self.room_name}: no information was found, please check.{self.slowdown}" 
        
        if self.current_endline > 0:                                 #returns current_status and current_endline
            status_update = f"{self.room_name} is {self.states[self.current_status]}, {self.current_endline} days left.{self.slowdown}"

        elif self.current_endline == 0 and self.next_endline > 0:    #current_status finished and next_status exist
            status_update = f"{self.room_name} went from {self.states[self.current_status]} to {self.states[self.next_status]}.{self.slowdown}"
            self.current_status, self.current_endline = self.next_status, self.next_endline
            self.next_status, self.next_endline = self.after_status, self.after_endline
            self.after_status, self.after_endline = 0, 0
      
        elif self.current_endline == 0 and self.next_endline == 0:    #current_status finished and next_state doesn't exist
            update_notice = int(input(f"{self.room_name} finished {self.states[self.current_status]}, an update is needed:\n{self.update_board}\t\t  --> "))

            if update_notice == 1:      #the room becomes AVAILABLE for one day
                self.current_status, self.current_endline = 1, 1
                status_update = f"{self.room_name} is now {self.states[self.current_status]}.{self.slowdown}"

            elif update_notice == 2:     #the room becomes RESERVED, then OCCUPIED
                schedule_update_1 = int(input(f"{self.states[2]}:  {self.schedule_message}\n  --> "))
                self.current_status, self.current_endline = 2, schedule_update_1
                schedule_update_2 = int(input(f"{self.states[3]}:  {self.schedule_message}\n  --> "))
                self.next_status, self.next_endline = 3, schedule_update_2
                status_update = f"{self.room_name} is now {self.states[self.current_status]}.{self.slowdown}"
       
            elif update_notice == 3:    #the room becomes OCCUPIED, then one CLEANING day
                schedule_update_1 = int(input(f"{self.states[3]}:  {self.schedule_message}\n  --> "))
                self.current_status, self.current_endline = 3, schedule_update_1
                self.next_status, self.next_endline = 4, 1
                status_update = f"{self.room_name} is now {self.states[self.current_status]}.{self.slowdown}"
   
            elif update_notice == 4:    #the room has one CLEANING day, the next one day becomes AVAILABLE
                self.current_status, self.current_endline = 4, 1
                self.next_status, self.next_endline = 1, 1
                status_update = f"{self.room_name} is now {self.states[self.current_status]}.{self.slowdown}"

            elif update_notice == 5:    #the room is now on MAINTENANCE, the next one day becomes CLEANING
                schedule_update_1 = int(input(f"{self.states[5]}:  {self.schedule_message}\n  --> "))
                self.current_status, self.current_endline = 5, schedule_update_1
                self.next_status, self.next_endline = 4, 1
                status_update = f"{self.room_name} is now {self.states[self.current_status]}.{self.slowdown}"
           
            elif update_notice == 6:    #the room is now DISABLED, the following status requires an update
                schedule_update_1 = int(input(f"{self.states[6]}:  {self.schedule_message}\n  --> "))
                self.current_status, self.current_endline = 6, schedule_update_1
                update_notice = int(input(f"{self.room_name} is now {self.states[self.current_status]}, the next status needs to be updated:\n{self.update_board}"))
                schedule_update_2 = int(input(f"{self.states[update_notice]}:  {self.schedule_message}\n  --> "))
                self.next_status, self.next_endline = update_notice, schedule_update_2
                status_update = f"{self.room_name} becomes {self.states[self.current_status]}.{self.slowdown}"
                
        return status_update

  ```
  This one checks if `current_status` has finished, if `next_status` doesn't exist, requires an update.
  | Variables | Description |
  | ------------ | ------------ |
  | `status_update` | Is the method's `str` return, modified by the conditionals |
  | `update_notice` | An `int(input())`, is the method's conditional |
  | `schedule_update_1` | An `int(input())`, the new `current_endline` attribute value. |
  | `schedule_update_2` | An `int(input())`, the new `next_endline` attribute value. |

</p>
</details>


- `scheduling_conditions(self, option)`
<details><summary>Details</summary>
<p>
  
  ```python
  def scheduling_conditions(self, option: int) -> bool:
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
         
        conditional_status = [["c_status_eq1__n_endline_eq0", "c_status_geq1__n_endline_eq0", "n_status_eq1__a_endline_eq0"],
                              ["c_status_eq1__n_endline_eq0", "c_status_geq1__n_endline_eq0", "n_status_eq1__a_endline_eq0", "n_status_geq1__a_endline_eq0", "a_status_eq1"],
                              ["c_status_eq3__n_endline_eq0", "n_status_eq3__a_endline_eq0", "c_status_eq5__n_endline_eq0", "n_status_eq5__a_endline_eq0", "c_status_eq6__n_endline_eq0", "n_status_eq6__a_endline_eq0"],
                              ["c_status_eq1__n_endline_eq0", "c_status_neq4__a_endline_eq1", "n_status_neq4__a_status_eq1", "c_status_eq3__n_endline_eq0", "n_status_eq3__a_endline_eq0", "c_status_eq6__n_endline_eq0", "n_status_eq6__a_endline_eq0"],
                              ["c_status_eq1__n_endline_eq0", "n_status_eq1__a_endline_eq0", "a_status_eq1", "c_status_l6__n_endline_eq0", "n_status_l6__a_endline_eq0"]]

        room_conditions = conditional_status[option - 1]
        return any(conditions[c] for c in room_conditions)
  ```
  | Objects | Description |
  | ------------ | ------------ |
  | `conditions` | A `dict`, each element is a conditional identified by a codified name  |
  | `conditional_status` | A `list`'s `list` with the `conditions[key]` those aplies to `states`' elements, excepting `AVAILABLE`  |
  | `room_conditions` | Uses the `option` `int(input())` to identify the scheduling command |

  The `any()` function and by extension, this method returns True if any conditional in `room_conditions` are true, otherwise it returns False.
  ```python
  return any(conditions[c] for c in room_conditions)
  ```

</p>
</details>


- `scheduling_data(self, option)`
<details><summary>Details</summary>
<p>
  
  ```python
  def scheduling_data(self, option: int) -> str:
        schedule_type = (f"{self.room_name}: no information was found, please check", 
                         f"{self.room_name}: ({self.definition})  -->  RIGHT NOW",
                         f"{self.room_name}: ({self.definition})  -->  {self.current_endline} DAYS",
                         f"{self.room_name}: ({self.definition})  -->  {self.current_endline + self.next_endline} DAYS",
                         f"{self.room_name}:       {self.states[self.current_status]}        -->  RIGHT NOW",
                         f"{self.room_name}:       {self.states[self.current_status]}        -->  {self.current_endline} DAYS",
                         f"{self.room_name}: {self.states[self.current_status]} --- {self.states[self.next_status]}  -->  {self.current_endline + self.next_endline} DAYS")

        schedule_data = schedule_type[0]

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

        for condition, result in conditions.get(option, []):
            if condition:
                schedule_data = result
                break
            
        return schedule_data
  ```
  | Objects | Description |
  | ------------ | ------------ |
  | `schedule_type` | A `tuple` with the posible returns |
  | `schedule_data` | Is the method's `str` return, modified by the conditionals |
  | `conditions` | A `dict`, each element relates the `option` `int(input())` values with a `list` of `tuple`: a conditional, and a `schedule_type` item |

  The `for condition, result in conditions.get(option, []):` statement checks the `list` of `tuple` asignated by `option`, returns the `schedule_type` item if the condition is `True`.
  ```python
  for condition, result in conditions.get(option, []):
      if condition:
          schedule_data = result
          break
            
  return schedule_data
  ```

</p>
</details>


- `scheduling_protocol(self, option)`
<details><summary>Details</summary>
<p>
  
  ```python
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
  ```
  | Objects | Description |
  | ------------ | ------------ |
  | `status_update` | Is the method's `str` return, modified by the conditionals |
  | `schedule_update_1` | An `int(input())`, the new `_endline` attribute value. |
  | `schedule_update_2` | An `int(input())`, the new `_endline` attribute value. |
  This method returns the updating of a room `_state` as a message, based in the same conditionals used above.
     
  This method has the structure that `scheduling_conditions()` and `scheduling_data()` used to have.

</p>
</details>


- `sunset_protocol(self)`
<details><summary>Details</summary>
<p>
  
  ```python
  def sunset_protocol(self) -> None:
        self.current_endline = self.current_endline - 1
  ```
  This method by the moment make `current_endline` decrease by one, represents the passing of a day.

</p>
</details>

### `Room`'s subclasses
```python
class Simple_Room(Room):
    definition: str = "Simple Bed, One Bathroom"
    def __init__(self, room_data: list = None):
        super().__init__(room_data)

class Double_Room(Room):
    definition: str = "Large Bed, One Bathroom"
    def __init__(self, room_data: list = None):
        super().__init__(room_data)

class Twin_Room(Room):
    definition: str = "Two Beds, Two Bathrooms"
    def __init__(self, room_data: list = None):
        super().__init__(room_data)

class Family_Room(Room):
    definition: str = "Three Beds, Two Bathrooms"
    def __init__(self, room_data: list = None):
        super().__init__(room_data)
```
For now are merely placeholders.



## **The `Hotel` class**
### Definition
```python
class Hotel():
    def __init__(self, hotel_data: tuple[Room, ...] = ()):
        self.hotel_data = hotel_data
```
Pretty simple, an `Hotel` object is composed by a `tuple` of `Room` objects by the `hotel_data` name. 

### The `Hotel` Methods
```python
def get_current_status(self) -> None:
    #...
    #code
    #... 

def get_complete_status(self) -> None:
    #...
    #code
    #... 

def sunrise_protocol(self) -> None:
    #...
    #code
    #... 

def sunset_protocol(self) -> None:
    #...
    #code
    #... 

def noon_protocol(self) -> None:
     #...
    #code
    #...
    #more code
    #...
    #even more code
    #...
```
You may notice the method's are apparently identical to the `Room` class methods, let's take a look to the complete code below:

- `get_current_status(self)`
<details><summary>Details</summary>
<p>
  
  ```python
  def get_current_status(self) -> None:
      print("  ROOM            STATUS")
      for room in self.hotel_data:
          print(room.get_current_status())
          time.sleep(1)   
  ```
  That's all, it delivers the `room.get_current_status()` for each room of the Hotel!.
  
  `time.sleep(1)` is an artificial delay in the method execution for testing quality purposes.

</p>
</details>


- `get_complete_status(self)`
<details><summary>Details</summary>
<p>
  
  ```python
  def get_complete_status(self) -> None:
      print("  ROOM            CURRENT STATUS                  NEXT STATUS                   AFTER STATUS")
      for room in self.hotel_data:
          print(room.get_complete_status())
          time.sleep(1)
  ```
  Almost the same concept as above, it delivers the `room.get_complete_status()` for each room of the Hotel.

</p>
</details>


- `sunrise_protocol(self)`
<details><summary>Details</summary>
<p>
  
  ```python
  def sunrise_protocol(self) -> None:
      for room in self.hotel_data:
          print(room.sunrise_protocol())
          time.sleep(2)
  ```
  This one deploys the `room.sunrise_protocol()` method for each room as a continuous read and write interaction.

</p>
</details>


- `noon_protocol(self)`
<details><summary>Details</summary>
<p>
  
  ```python
  def noon_protocol(self) -> None:
      option = int(input("\n""         OPTIONS                 TO DO" "\n"
                         "Reserve a Room                  press 1" "\n"
                         "Occupy a Room                   press 2" "\n"
                         "Schedule a Cleaning             press 3" "\n"
                         "Schedule a Maintenance          press 4" "\n"
                         "Disable a Room                  press 5" "\n"
                         "Return                          press 0" "\n"
                         "                                  -->  "))       

        if option == 0: pass

        if option > 0:                  
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
  ```
  This method integrates `room.scheduling_conditions()`, `room.scheduling_data()` and `room.scheduling_protocol()` in a interactive mess to update in a room one `_status`.
  
  **This is how it works:**
  ```python
  option = int(input("\n""         OPTIONS                 TO DO" "\n"
                     "Reserve a Room                  press 1" "\n"
                     "Occupy a Room                   press 2" "\n"
                     "Schedule a Cleaning             press 3" "\n"
                     "Schedule a Maintenance          press 4" "\n"
                     "Disable a Room                  press 5" "\n"
                     "Return                          press 0" "\n"
                     "                                  -->  "))       
  ```
  `option` is a `int(input())` with a whole options menu as a argument.

  ```python
  if option == 0: pass    
  ```
  `option == 0` exits the "options menu interface" and goes back to the "main menu interface", we will see it in the `main` file section.
  
  ```python
  if option > 0:                 
      booking_rooms = []
      for room in self.hotel_data:
      if room.scheduling_conditions(option) is True:
          booking_rooms.append(room)
      else: pass  
  ```
  `booking_rooms` is a `list` composed by the `Room` objects which `scheduling_conditions(option)` is `True`, those are, the rooms that can be scheduled in the status chosen by the user. 

  ```python
  if len(booking_rooms) > 0:
      print("  ROOM             INFORMATION             UNTIL      TO DO")
      for b_room in booking_rooms:
          print(f"{b_room.scheduling_data(option)}  -->  press {(booking_rooms.index(b_room) + 1)}")
          time.sleep(1)
  ```
  This section checks if `booking_rooms` has elements and shows the information provided by `room.scheduling_data(option)` as a options menu of the rooms those can be scheduled.

  ```python
  book = int(input("Cancel                                                  press 0" "\n"
                   "                                                       "" -->  "))
      if book > 0 and book <= len(booking_rooms):
          print(booking_rooms[book - 1].scheduling_protocol(option))
      if book == 0:
          pass
  ```
  `book` is the `int(input())` used to "choose" the room to schedule, consequently, shows the `_state` updating information provided by `room.scheduling_protocol(option)` for the chosen room.
  
</p>
</details>    


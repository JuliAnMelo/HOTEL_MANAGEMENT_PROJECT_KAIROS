class Person():
    """
    A class to represent a person with basic personal information.
    """
    def __init__(self, person_data: list = None):
        if person_data is None:
            person_data = [("NO_LAST_NAME", "NO_FIRST_NAME"), "id_number", "tel_number", "username@server.domain"]
        self._person_name = person_data[0]
        self._person_id = person_data[1]
        self._person_phone = person_data[2]
        self._person_email = person_data[3]



class Guest(Person):
    """
    A class to represent a guest, inheriting from the Person class.
    """
    def __init__(self, person_data: list = None):
        super().__init__(person_data)  
        if person_data is None:
            person_data = [("NO_LAST_NAME", "NO_FIRST_NAME"), "id_number", "tel_number", "username@server.domain", "guest_adress", "mm/dd/yyyy"]
        self._guest_adress = person_data[4]
        self._guest_birthday = person_data[5]


    def to_dict(self) -> dict:
        """
        Converts the Guest object into a dictionary representation.
        """
        return {"person_name": {"last": self._person_name[0],
                                "first": self._person_name[1]},
                "person_id": self._person_id,
                "person_phone": self._person_phone,
                "person_email": self._person_email,
                "guest_adress": self._guest_adress,
                "guest_birthday": self._guest_birthday}
    
    @classmethod
    def from_dict(cls, data: dict):
        """
        Creates a Guest object from a dictionary representation.
        """
        employee_data = [(data["person_name"]["last"], data["person_name"]["first"]),
                          data["person_id"],
                          data["person_phone"],
                          data["person_email"],
                          data["guest_adress"],
                          data["guest_birthday"]]
        return cls(employee_data)

    @classmethod
    def registration(cls):
        """
        Collects guest information from user input and creates a Guest object.

        It then returns an instance of the Guest class populated with the provided information.
        """
        print("Registration:")
        surname = str(input("Last Name         --> "))
        name =    str(input("First Name        --> "))
        ide =     str(input("Identification    --> "))
        phone =   str(input("Phone Number      --> "))
        email =   str(input("Email Adress      --> "))
        adress =  str(input("Home Adress       --> "))
        birth =   str(input("Birthday          --> "))
        return cls([(surname, name), ide, phone, email, adress, birth])



class Employee(Person):
    """
    A class to represent an employee, inheriting from the Person class.
    """
    def __init__(self, person_data: list = None):
        super().__init__(person_data)
        if person_data is None:
            person_data = [("NO_LAST_NAME", "NO_FIRST_NAME"), "id_number", "tel_number", "username@server.domain", "job_title", "employee_code"]
        self._employee_role = person_data[4]
        self._employee_id = person_data[5]

    def to_dict(self) -> dict:
        """
        Converts the Employee object into a dictionary representation.
        """
        return {"person_name": self._person_name,
                "person_id": self._person_id,
                "person_phone": self._person_phone,
                "person_email": self._person_email,
                "employee_role": self._employee_role,
                "employee_id": self._employee_id}
    
    @classmethod
    def from_dict(cls, data: dict):
        """
        Creates an Employee object from a dictionary representation.
        """
        employee_data = [data["person_name"],
                         data["person_id"],
                         data["person_phone"],
                         data["person_email"],
                         data["employee_role"],
                         data["employee_id"]]
        return cls(employee_data)
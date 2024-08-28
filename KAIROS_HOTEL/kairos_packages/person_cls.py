class Person():
    def __init__(self, person_data: list = None):

        if person_data is None:
            person_data = [("NO_LAST_NAME", "NO_FIRST_NAME"), "id_number", "tel_number", "username@server.domain"]
        self.person_name = person_data[0]
        self.person_id = person_data[1]
        self.person_phone = person_data[2]
        self.person_email = person_data[3]

class Guest(Person):
    def __init__(self, person_data: list = None):
        super().__init__(person_data)
        
        if person_data is None:
            person_data = [("NO_LAST_NAME", "NO_FIRST_NAME"), "id_number", "tel_number", "username@server.domain", "guest_adress", "mm/dd/yyyy"]
        self.guest_adress = person_data[4]
        self.guest_birthday = person_data[5]

    def to_dict(self) -> dict:
        return {"person_name": {"last": self.person_name[0],
                                "first": self.person_name[1]},
                "person_id": self.person_id,
                "person_phone": self.person_phone,
                "person_email": self.person_email,
                "guest_adress": self.guest_adress,
                "guest_birthday": self.guest_birthday}
    @classmethod
    def from_dict(cls, data):
        employee_data = [(data["person_name"]["last"], data["person_name"]["first"]),
                          data["person_id"],
                          data["person_phone"],
                          data["person_email"],
                          data["guest_adress"],
                          data["guest_birthday"]]
        return cls(employee_data)


class Employee(Person):
    def __init__(self, person_data: list = None):
        super().__init__(person_data)

        if person_data is None:
            person_data = [("NO_LAST_NAME", "NO_FIRST_NAME"), "id_number", "tel_number", "username@server.domain", "job_title", "employee_code"]
        self.employee_role = person_data[4]
        self.employee_id = person_data[5]

    def to_dict(self) -> dict:
        return {"person_name": self.person_name,
                "person_id": self.person_id,
                "person_phone": self.person_phone,
                "person_email": self.person_email,
                "employee_role": self.employee_role,
                "employee_id": self.employee_id}
    @classmethod
    def from_dict(cls, data):
        employee_data = [data["person_name"],
                            data["person_id"],
                            data["person_phone"],
                            data["person_email"],
                            data["employee_role"],
                            data["employee_id"]]
        return cls(employee_data)
        
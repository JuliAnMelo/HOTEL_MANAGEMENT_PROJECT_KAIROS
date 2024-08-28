####    KAIROS AS PYTHON OBJECTS    ####
"""
R101 = Simple_Room(["Room 101", 3, 1, 1, 1, 0, 0])
R102 = Simple_Room(["Room 102", 2, 2, 3, 3, 0, 0])
R103 = Double_Room(["Room 103", 4, 1, 5, 2, 0, 0])
R104 = Double_Room(["Room 104", 3, 3, 2, 1, 3, 4])

R201 = Simple_Room(["Room 201", 3, 0, 4, 1, 0, 0])
R202 = Simple_Room(["Room 202", 5, 2, 0, 0, 0, 0])
R203 = Twin_Room(["Room 203", 5, 0, 6, 2, 3, 3])
R204 = Twin_Room(["Room 204", 0, 0, 0, 0, 0, 0])

R301 = Double_Room(["Room 301", 2, 3, 3, 3, 5, 2])
R302 = Double_Room(["Room 302", 6, 2, 4, 2, 1, 1])
R303 = Family_Room(["Room 303", 4, 2, 1, 1, 0, 0])
R304 = Family_Room(["Room 304", 1, 1, 0, 0, 0, 0])

employees = {"NOINFO": Employee([("NOLASTNAME", "NOFIRSTNAME"), "0000000000", "000-0000", "username@server.domain", "NOINFO", "E000"]),
             "Receptionist": Employee([("Garcia", "Laura"), "0012345678", "555-0101", "laura.garcia@hotel.com", "Receptionist", "E001"]),
             "Housekeeper": Employee([("Smith", "John"), "0023456789", "555-0202", "john.smith@hotel.com", "Housekeeper", "E002"]),
             "Concierge": Employee([("Doe", "Jane"), "0034567890", "555-0303", "jane.doe@hotel.com", "Concierge", "E003"]),
             "Chef": Employee([("Williams", "Emily"), "0056789012", "555-0505", "emily.williams@hotel.com", "Chef", "E004"]),
             "Maintenance Worker": Employee([("Martinez", "Carlos"), "0067890123", "555-0606", "carlos.martinez@hotel.com", "Maintenance Worker", "E005"]),
             "General Manager": Employee([("Davis", "Kevin"), "0089012345", "555-0808", "kevin.davis@hotel.com", "General Manager", "E006"]),
             "Front Desk Manager": Employee([("Rodriguez", "Angela"), "0090123456", "555-0909", "angela.rodriguez@hotel.com", "Front Desk Manager", "E007"]),
             "Security Officer": Employee([("Lee", "Daniel"), "0101234567", "555-1010", "daniel.lee@hotel.com", "Security Officer", "E008"])}

guests = {"Room 101": (Guest([("Smith", "John"), "987654321", "555-9876", "john.smith@example.com", "123 Elm St", "03/25/1985"]),
                       employees["Housekeeper"],
                       employees["NOINFO"]),
          "Room 102": (Guest([("Doe", "Jane"), "123456789", "555-1234", "jane.doe@example.com", "456 Oak St", "07/14/1990"]), 
                       Guest([("Doe", "Jane"), "123456789", "555-1234", "jane.doe@example.com", "456 Oak St", "07/14/1990"]),
                       employees["NOINFO"]),
          "Room 103": (employees["Concierge"],
                       employees["Maintenance Worker"],
                       employees["NOINFO"]),
          "Room 104": (Guest([("Johnson", "Michael"), "234567891", "555-2345", "michael.johnson@example.com", "789 Pine St", "11/02/1975"]),
                       Guest([("Brown", "Emily"), "345678912", "555-3456", "emily.brown@example.com", "101 Maple St", "05/16/1982"]),
                       Guest([("Brown", "Emily"), "345678912", "555-3456", "emily.brown@example.com", "101 Maple St", "05/16/1982"])),
          "Room 201": (Guest([("Williams", "David"), "456789123", "555-4567", "david.williams@example.com", "202 Cedar St", "09/10/1988"]),
                       employees["Concierge"],
                       employees["NOINFO"]),
          "Room 202": (employees["Maintenance Worker"],
                       employees["NOINFO"],
                       employees["NOINFO"]),
          "Room 203": (employees["Maintenance Worker"],
                     employees["Front Desk Manager"],
                     Guest([("Jones", "Sarah"), "567891234", "555-5678", "sarah.jones@example.com", "303 Birch St", "12/30/1992"])),
          "Room 204": (employees["NOINFO"],
                       employees["NOINFO"],
                       employees["NOINFO"]),
          "Room 301": (Guest([("Garcia", "Carlos"), "678912345", "555-6789", "carlos.garcia@example.com", "404 Spruce St", "08/20/1983"]),
                       Guest([("Garcia", "Carlos"), "678912345", "555-6789", "carlos.garcia@example.com", "404 Spruce St", "08/20/1983"]),
                       employees["Maintenance Worker"]),
          "Room 302": (employees["Front Desk Manager"],
                       employees["Concierge"],
                       employees["Housekeeper"]),
          "Room 303": (employees["Concierge"],
                       employees["Housekeeper"],
                       employees["NOINFO"]),
          "Room 304": (employees["Housekeeper"],
                       employees["NOINFO"],
                       employees["NOINFO"])}

KAIROS = Hotel((R101, R102, R103, R104, R201, R202, R203, R204, R301, R302, R303, R304), employees, guests)
"""


####    KAIROS AS JSON STRUCTURE    ####
"""
{
    "hotel_data": [
        {
            "room_name": "Room 101",
            "current_status": 3,
            "current_endline": 1,
            "next_status": 1,
            "next_endline": 1,
            "after_status": 0,
            "after_endline": 0,
            "type": "Simple_Room"
        },
        {
            "room_name": "Room 102",
            "current_status": 2,
            "current_endline": 2,
            "next_status": 3,
            "next_endline": 3,
            "after_status": 0,
            "after_endline": 0,
            "type": "Simple_Room"
        },
        {
            "room_name": "Room 103",
            "current_status": 4,
            "current_endline": 1,
            "next_status": 5,
            "next_endline": 2,
            "after_status": 0,
            "after_endline": 0,
            "type": "Double_Room"
        },
        {
            "room_name": "Room 104",
            "current_status": 3,
            "current_endline": 3,
            "next_status": 2,
            "next_endline": 1,
            "after_status": 3,
            "after_endline": 4,
            "type": "Double_Room"
        },
        {
            "room_name": "Room 201",
            "current_status": 3,
            "current_endline": 0,
            "next_status": 4,
            "next_endline": 1,
            "after_status": 0,
            "after_endline": 0,
            "type": "Simple_Room"
        },
        {
            "room_name": "Room 202",
            "current_status": 5,
            "current_endline": 2,
            "next_status": 0,
            "next_endline": 0,
            "after_status": 0,
            "after_endline": 0,
            "type": "Simple_Room"
        },
        {
            "room_name": "Room 203",
            "current_status": 5,
            "current_endline": 0,
            "next_status": 6,
            "next_endline": 2,
            "after_status": 3,
            "after_endline": 3,
            "type": "Twin_Room"
        },
        {
            "room_name": "Room 204",
            "current_status": 0,
            "current_endline": 0,
            "next_status": 0,
            "next_endline": 0,
            "after_status": 0,
            "after_endline": 0,
            "type": "Twin_Room"
        },
        {
            "room_name": "Room 301",
            "current_status": 2,
            "current_endline": 3,
            "next_status": 3,
            "next_endline": 3,
            "after_status": 5,
            "after_endline": 2,
            "type": "Double_Room"
        },
        {
            "room_name": "Room 302",
            "current_status": 6,
            "current_endline": 2,
            "next_status": 4,
            "next_endline": 2,
            "after_status": 1,
            "after_endline": 1,
            "type": "Double_Room"
        },
        {
            "room_name": "Room 303",
            "current_status": 4,
            "current_endline": 2,
            "next_status": 1,
            "next_endline": 1,
            "after_status": 0,
            "after_endline": 0,
            "type": "Family_Room"
        },
        {
            "room_name": "Room 304",
            "current_status": 1,
            "current_endline": 1,
            "next_status": 0,
            "next_endline": 0,
            "after_status": 0,
            "after_endline": 0,
            "type": "Family_Room"
        }
    ],
    "employees": {
        "NOINFO": {
            "person_name": [
                "NOLASTNAME",
                "NOFIRSTNAME"
            ],
            "person_id": "0000000000",
            "person_phone": "000-0000",
            "person_email": "username@server.domain",
            "employee_role": "NOINFO",
            "employee_id": "E000"
        },
        "Receptionist": {
            "person_name": [
                "Garcia",
                "Laura"
            ],
            "person_id": "0012345678",
            "person_phone": "555-0101",
            "person_email": "laura.garcia@hotel.com",
            "employee_role": "Receptionist",
            "employee_id": "E001"
        },
        "Housekeeper": {
            "person_name": [
                "Smith",
                "John"
            ],
            "person_id": "0023456789",
            "person_phone": "555-0202",
            "person_email": "john.smith@hotel.com",
            "employee_role": "Housekeeper",
            "employee_id": "E002"
        },
        "Concierge": {
            "person_name": [
                "Doe",
                "Jane"
            ],
            "person_id": "0034567890",
            "person_phone": "555-0303",
            "person_email": "jane.doe@hotel.com",
            "employee_role": "Concierge",
            "employee_id": "E003"
        },
        "Chef": {
            "person_name": [
                "Williams",
                "Emily"
            ],
            "person_id": "0056789012",
            "person_phone": "555-0505",
            "person_email": "emily.williams@hotel.com",
            "employee_role": "Chef",
            "employee_id": "E004"
        },
        "Maintenance Worker": {
            "person_name": [
                "Martinez",
                "Carlos"
            ],
            "person_id": "0067890123",
            "person_phone": "555-0606",
            "person_email": "carlos.martinez@hotel.com",
            "employee_role": "Maintenance Worker",
            "employee_id": "E005"
        },
        "General Manager": {
            "person_name": [
                "Davis",
                "Kevin"
            ],
            "person_id": "0089012345",
            "person_phone": "555-0808",
            "person_email": "kevin.davis@hotel.com",
            "employee_role": "General Manager",
            "employee_id": "E006"
        },
        "Front Desk Manager": {
            "person_name": [
                "Rodriguez",
                "Angela"
            ],
            "person_id": "0090123456",
            "person_phone": "555-0909",
            "person_email": "angela.rodriguez@hotel.com",
            "employee_role": "Front Desk Manager",
            "employee_id": "E007"
        },
        "Security Officer": {
            "person_name": [
                "Lee",
                "Daniel"
            ],
            "person_id": "0101234567",
            "person_phone": "555-1010",
            "person_email": "daniel.lee@hotel.com",
            "employee_role": "Security Officer",
            "employee_id": "E008"
        }
    },
    "guests": {
        "Room 101": [
            {
                "person_name": {
                    "last": "Smith",
                    "first": "John"
                },
                "person_id": "987654321",
                "person_phone": "555-9876",
                "person_email": "john.smith@example.com",
                "guest_adress": "123 Elm St",
                "guest_birthday": "03/25/1985"
            },
            {
                "employee_role": "Housekeeper"
            },
            {
                "employee_role": "NOINFO"
            }
        ],
        "Room 102": [
            {
                "person_name": {
                    "last": "Doe",
                    "first": "Jane"
                },
                "person_id": "123456789",
                "person_phone": "555-1234",
                "person_email": "jane.doe@example.com",
                "guest_adress": "456 Oak St",
                "guest_birthday": "07/14/1990"
            },
            {
                "person_name": {
                    "last": "Doe",
                    "first": "Jane"
                },
                "person_id": "123456789",
                "person_phone": "555-1234",
                "person_email": "jane.doe@example.com",
                "guest_adress": "456 Oak St",
                "guest_birthday": "07/14/1990"
            },
            {
                "employee_role": "NOINFO"
            }
        ],
        "Room 103": [
            {
                "employee_role": "Concierge"
            },
            {
                "employee_role": "Maintenance Worker"
            },
            {
                "employee_role": "NOINFO"
            }
        ],
        "Room 104": [
            {
                "person_name": {
                    "last": "Johnson",
                    "first": "Michael"
                },
                "person_id": "234567891",
                "person_phone": "555-2345",
                "person_email": "michael.johnson@example.com",
                "guest_adress": "789 Pine St",
                "guest_birthday": "11/02/1975"
            },
            {
                "person_name": {
                    "last": "Brown",
                    "first": "Emily"
                },
                "person_id": "345678912",
                "person_phone": "555-3456",
                "person_email": "emily.brown@example.com",
                "guest_adress": "101 Maple St",
                "guest_birthday": "05/16/1982"
            },
            {
                "person_name": {
                    "last": "Brown",
                    "first": "Emily"
                },
                "person_id": "345678912",
                "person_phone": "555-3456",
                "person_email": "emily.brown@example.com",
                "guest_adress": "101 Maple St",
                "guest_birthday": "05/16/1982"
            }
        ],
        "Room 201": [
            {
                "person_name": {
                    "last": "Williams",
                    "first": "David"
                },
                "person_id": "456789123",
                "person_phone": "555-4567",
                "person_email": "david.williams@example.com",
                "guest_adress": "202 Cedar St",
                "guest_birthday": "09/10/1988"
            },
            {
                "employee_role": "Concierge"
            },
            {
                "employee_role": "NOINFO"
            }
        ],
        "Room 202": [
            {
                "employee_role": "Maintenance Worker"
            },
            {
                "employee_role": "NOINFO"
            },
            {
                "employee_role": "NOINFO"
            }
        ],
        "Room 203": [
            {
                "employee_role": "Maintenance Worker"
            },
            {
                "employee_role": "Front Desk Manager"
            },
            {
                "person_name": {
                    "last": "Jones",
                    "first": "Sarah"
                },
                "person_id": "567891234",
                "person_phone": "555-5678",
                "person_email": "sarah.jones@example.com",
                "guest_adress": "303 Birch St",
                "guest_birthday": "12/30/1992"
            }
        ],
        "Room 204": [
            {
                "employee_role": "NOINFO"
            },
            {
                "employee_role": "NOINFO"
            },
            {
                "employee_role": "NOINFO"
            }
        ],
        "Room 301": [
            {
                "person_name": {
                    "last": "Garcia",
                    "first": "Carlos"
                },
                "person_id": "678912345",
                "person_phone": "555-6789",
                "person_email": "carlos.garcia@example.com",
                "guest_adress": "404 Spruce St",
                "guest_birthday": "08/20/1983"
            },
            {
                "person_name": {
                    "last": "Garcia",
                    "first": "Carlos"
                },
                "person_id": "678912345",
                "person_phone": "555-6789",
                "person_email": "carlos.garcia@example.com",
                "guest_adress": "404 Spruce St",
                "guest_birthday": "08/20/1983"
            },
            {
                "employee_role": "Maintenance Worker"
            }
        ],
        "Room 302": [
            {
                "employee_role": "Front Desk Manager"
            },
            {
                "employee_role": "Concierge"
            },
            {
                "employee_role": "Housekeeper"
            }
        ],
        "Room 303": [
            {
                "employee_role": "Concierge"
            },
            {
                "employee_role": "Housekeeper"
            },
            {
                "employee_role": "NOINFO"
            }
        ],
        "Room 304": [
            {
                "employee_role": "Housekeeper"
            },
            {
                "employee_role": "NOINFO"
            },
            {
                "employee_role": "NOINFO"
            }
        ]
    }
}
"""


####    Guest() OBJECT BANK    ####
"""
Guest([("Smith", "John"), "987654321", "555-9876", "john.smith@example.com", "123 Elm St", "03/25/1985"])
Guest([("Doe", "Jane"), "123456789", "555-1234", "jane.doe@example.com", "456 Oak St", "07/14/1990"])
Guest([("Johnson", "Michael"), "234567891", "555-2345", "michael.johnson@example.com", "789 Pine St", "11/02/1975"])
Guest([("Brown", "Emily"), "345678912", "555-3456", "emily.brown@example.com", "101 Maple St", "05/16/1982"])
Guest([("Williams", "David"), "456789123", "555-4567", "david.williams@example.com", "202 Cedar St", "09/10/1988"])
Guest([("Jones", "Sarah"), "567891234", "555-5678", "sarah.jones@example.com", "303 Birch St", "12/30/1992"])
Guest([("Garcia", "Carlos"), "678912345", "555-6789", "carlos.garcia@example.com", "404 Spruce St", "08/20/1983"])
Guest([("Miller", "Anna"), "789123456", "555-7890", "anna.miller@example.com", "505 Willow St", "10/05/1979"])
Guest([("Martinez", "Luis"), "891234567", "555-8901", "luis.martinez@example.com", "606 Redwood St", "02/14/1986"])
Guest([("Rodriguez", "Maria"), "912345678", "555-9012", "maria.rodriguez@example.com", "707 Fir St", "04/18/1987"])
Guest([("Davis", "James"), "123098765", "555-0123", "james.davis@example.com", "808 Ash St", "06/12/1981"])
Guest([("Hernandez", "Patricia"), "234109876", "555-1234", "patricia.hernandez@example.com", "909 Poplar St", "01/22/1984"])
Guest([("Lopez", "Daniel"), "345210987", "555-2345", "daniel.lopez@example.com", "1010 Palm St", "11/17/1993"])
Guest([("Gonzalez", "Laura"), "456321098", "555-3456", "laura.gonzalez@example.com", "1111 Cypress St", "03/08/1989"])
Guest([("Wilson", "Mark"), "567432109", "555-4567", "mark.wilson@example.com", "1212 Hickory St", "12/01/1976"])
Guest([("Anderson", "Susan"), "678543210", "555-5678", "susan.anderson@example.com", "1313 Magnolia St", "09/24/1980"])
Guest([("Thomas", "Robert"), "789654321", "555-6789", "robert.thomas@example.com", "1414 Walnut St", "07/29/1978"])
Guest([("Taylor", "Jessica"), "890765432", "555-7890", "jessica.taylor@example.com", "1515 Chestnut St", "10/31/1991"])
Guest([("Moore", "Matthew"), "901876543", "555-8901", "matthew.moore@example.com", "1616 Cherry St", "04/04/1985"])
Guest([("Martin", "Sophia"), "012987654", "555-9012", "sophia.martin@example.com", "1717 Sycamore St", "08/12/1982"])
Guest([("Lee", "Kevin"), "123098764", "555-0123", "kevin.lee@example.com", "1818 Alder St", "05/07/1977"])
Guest([("Perez", "Kimberly"), "234109875", "555-1234", "kimberly.perez@example.com", "1919 Dogwood St", "06/19/1986"])
Guest([("White", "Joshua"), "345210986", "555-2345", "joshua.white@example.com", "2020 Chestnut St", "11/23/1994"])
Guest([("Clark", "Ashley"), "456321097", "555-3456", "ashley.clark@example.com", "2121 Sequoia St", "02/26/1990"])
Guest([("Lewis", "Brandon"), "567432108", "555-4567", "brandon.lewis@example.com", "2222 Willow St", "01/15/1988"])
"""
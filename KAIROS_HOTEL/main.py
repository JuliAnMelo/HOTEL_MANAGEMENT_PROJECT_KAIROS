import json
from kairos_packages.room_cls import Simple_Room, Double_Room, Twin_Room, Family_Room
from kairos_packages.hotel_cls import Hotel
from kairos_packages.person_cls import Guest, Employee

################################
#THIS VERSION TAKES THE PYTHON OBJECTS TO UPDATE THE JSON, FOR VISUALIZATION PORPUSES
#THIS VERSION DOESN'T MODIFIES THE GUESTS INFORMATION YET
################################

################################
#add comments in all of Person()
#add comments in Room() and Hotel(); to_dict() and from_dict() methods
################################

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


def main():

    print("\t""-------------------""\n""\t""KAIROS HOTEL SYSTEM""\n""\t""-------------------")
    while True:
        program = int(input("\n""         OPTIONS                 TO DO" "\n"
                            "Current Status of the Hotel     press 1" "\n"
                            "Complete Status of the Hotel    press 2" "\n"
                            "Check Room Status               press 3" "\n"
                            "Specific Tasks                  press 4" "\n"
                            "End the Day                     press 5" "\n"
                            "Exit                            press 0" "\n"
                            "\t""\t""\t""\t"" -->  "))

        if program == 0: break      #exit

        elif program == 1:            #current status of the hotel
            KAIROS.get_current_status()

        elif program == 2:            #complete status of the hotel
            KAIROS.get_complete_status()
                
        elif program == 3:            #check room status at the beginning of each "day"
            KAIROS.sunrise_protocol()

        elif program == 4:            #specific tasks
            KAIROS.noon_protocol()

        elif program == 5:            #end the "day" + JSON TEST      
            with open('KAIROS_data.json', 'r+') as json_file:          
                KAIROS_data = KAIROS.to_dict()    
                json.dump(KAIROS_data, json_file, indent=4)
                KAIROS.sunset_protocol()

if __name__ == "__main__": 
    main()
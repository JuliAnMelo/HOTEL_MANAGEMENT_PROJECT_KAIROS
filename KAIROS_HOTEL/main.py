import json
from datetime import datetime, timedelta
from kairos_packages.hotel import Hotel
from kairos_packages.exception import IntInputError

def main():
    with open('KAIROS_data.json', 'r+') as json_file:
        hotel_data = json.load(json_file)
        KAIROS = Hotel.from_dict(hotel_data)

        print("\nPYLONE TEAM HOTEL MANAGEMENT SOLUTION\nKAIROS HOTEL SYSTEM")
        date = datetime.now()
        
        while True:
            try:
                print(date.strftime("%B %d, %Y"))
                program = int(input("\n""          OPTIONS                TO GO" "\n"
                                    "Current Status of the Hotel     press 1" "\n"
                                    "Complete Status of the Hotel    press 2" "\n"
                                    "Check Room Status               press 3" "\n"
                                    "Specific Tasks                  press 4" "\n"
                                    "Cancel Scheduling               press 5" "\n"
                                    "Generate Report                 press 6" "\n"
                                    "End the Day                     press 7" "\n"
                                    "Exit                            press 0" "\n"
                                    "                                 -->  "))
                    
                if program == 0: break 

                elif program == 1:
                    KAIROS.get_current_status()

                elif program == 2:
                    KAIROS.get_complete_status()
                        
                elif program == 3:
                    KAIROS.sunrise_protocol()

                elif program == 4:
                    KAIROS.noon_protocol()

                elif program == 5:
                    KAIROS.midnight_protocol()

                elif program == 6:
                    KAIROS.get_daily_report(date)

                elif program == 7:
                    KAIROS_data = KAIROS.to_dict()    
                    json_file.seek(0)
                    json.dump(KAIROS_data, json_file, indent=4)
                    json_file.truncate()
                    KAIROS.sunset_protocol()
                    date = date + timedelta(days=1)

                else: raise IntInputError("Press a number between 0 and 6, Returning.")
                
            except IntInputError as error: print(f"\n{error}\n\n")
            except ValueError: print("\nPress numbers only, Returning.\n\n")

if __name__ == "__main__": 
    main()
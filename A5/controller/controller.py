from repository.passenger_repository import PassengerRepository
from repository.plane_repository import PlaneRepository
from repository.repository import Repository
from service.service import Service
from UI.ui import UI
from time import sleep
from tabulate import tabulate

class Controller:
    def __init__(self, service:Service, ui:UI):
        self.__service = service
        self.__ui = ui
        
    @staticmethod
    def __print_exit():
        print("Exiting program")
        
    def __print_planes(self, plane_list):
        headers = ["Index", "Plane ID", "Airline Company", "Number of Seats", "Destination"]
        table = []
        for index, plane in enumerate(plane_list):
            table.append([index, plane.get_planeID(), plane.get_airline_company(), plane.get_number_of_seats(), plane.get_destination()])
        print(tabulate(table, headers=headers, tablefmt="grid"))
        
    def __print_passengers(self, passenger_list, option):
        headers = ["Index", "First Name", "Last Name", "Passport ID", f"Plane ID\n{option}"]
        table = []
        for index, passenger in enumerate(passenger_list):
            table.append([index, passenger.get_first_name(), passenger.get_last_name(), passenger.get_passportID(), passenger.get_planeID()])
        print(tabulate(table, headers=headers, tablefmt="grid"))
        
    def __print_remaining_seats(self, plane_list):
        headers = ["Index", "Plane ID", "Remaining Seats"]
        table = []
        for index, plane in enumerate(plane_list):
            table.append([index, plane.get_planeID(), self.__service.show_remaining_seats(plane.get_planeID())])
        print(tabulate(table, headers=headers, tablefmt="grid"))

        
    def __plane_menu(self):
        while True:
            self.__ui.clear_menu()
            self.__ui.print_plane_menu()
            user_input = self.__ui.get_input()
            while user_input == None or user_input == "":
                print("Please enter an integer")
                user_input = self.__ui.get_input()
            if user_input == 0:
                self.__main_menu()
            elif user_input == 1:
                # add plane
                planeID = input("Enter planeID: ")
                airline_company = input("Enter airline company: ")
                number_of_seats = input("Enter number of seats: ")
                destination = input("Enter destination: ")
                try:
                    self.__service.add_plane(planeID, airline_company, number_of_seats, destination)
                    print("Plane added successfully")
                    sleep(1)
                except Exception as e:
                    print(e)
                    sleep(1)
            elif user_input == 2:
                # view all planes
                plane_list = self.__service.get_plane_list()
                self.__print_planes(plane_list)
                input("Press ENTER to continue")
            elif user_input == 3:
                # view plane by ID
                planeID = input("Enter planeID: ")
                try:
                    plane = self.__service.get_plane_by_planeID(planeID)
                    self.__print_planes([plane])
                    input("Press ENTER to continue")
                except Exception as e:
                    print(e)
                    sleep(1)
            elif user_input == 4:
                # view plane at Repository index
                index = input("Enter index: ")
                try:
                    plane = self.__service.get_plane_by_index(index)
                    self.__print_planes([plane])
                    input("Press ENTER to continue")
                except Exception as e:
                    print(e)
                    sleep(1)
            elif user_input == 5:
                # update a plane
                index = input("Enter index: ")
                print("Leave empty if you don't want to update the field (ENTER)")
                planeID = input("Enter planeID: ")
                airline_company = input("Enter airline company: ")
                number_of_seats = input("Enter number of seats: ")
                destination = input("Enter destination: ")
                try:
                    self.__service.update_plane(index, planeID, airline_company, number_of_seats, destination)
                    print("Plane updated successfully")
                    sleep(1)
                except Exception as e:
                    print(e)
                    sleep(1)
            elif user_input == 6:
                # delete a plane
                index = input("Enter index: ")
                try:
                    self.__service.delete_plane_by_index(index)
                    print("Plane deleted successfully")
                    sleep(1)
                except Exception as e:
                    print(e)
                    sleep(1)
            elif user_input == 8:
                # Show remaining seats in each plane
                plane_list = self.__service.get_plane_list()
                self.__print_remaining_seats(plane_list)
                input("Press ENTER to continue")
            else:
                print("Invalid input")
                sleep(1)
                
    def __passenger_menu(self):
        while True:
            self.__ui.clear_menu()
            self.__ui.print_passenger_menu()
            user_input = self.__ui.get_input()
            while(user_input == None or user_input == ""):
                print("Please enter an integer")
                user_input = self.__ui.get_input()
            if user_input == 0:
                self.__main_menu()
            elif user_input == 1:
                # add passenger
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                passportID = input("Enter passportID: ")
                planeID = input("Enter planeID: ")
                try:
                    self.__service.add_passenger(first_name, last_name, passportID, planeID)
                    print("Passenger added successfully")
                    sleep(1)
                except Exception as e:
                    print(e)
                    sleep(1)
            elif user_input == 2:
                # view all passengers
                passenger_list = self.__service.get_passenger_list()
                self.__print_passengers(passenger_list, "All")
                input("Press ENTER to continue")
            elif user_input == 3:
                # view passenger in a plane by planeID
                planeID = input("Enter planeID: ")
                try:
                    passenger_list = self.__service.get_passengers_by_planeID(planeID)
                    self.__print_passengers(passenger_list, planeID)
                    input("Press ENTER to continue")
                except Exception as e:
                    print(e)
                    sleep(1)
            elif user_input == 4:
                # search passenger with passportID
                passportID = input("Enter passportID: ")
                try:
                    passenger = self.__service.get_passenger_by_passportID(passportID)
                    self.__print_passengers([passenger])
                    input("Press ENTER to continue")
                except Exception as e:
                    print(e)
                    sleep(1)
            elif user_input == 5:
                # view all passengers with the same name
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                try:
                    passenger_list = self.__service.get_passengers_by_name(first_name, last_name)
                    self.__print_passengers(passenger_list)
                    input("Press ENTER to continue")
                except Exception as e:
                    print(e)
                    sleep(1)
            elif user_input == 6:
                # view all planes
                plane_list = self.__service.get_plane_list()
                self.__print_planes(plane_list)
                input("Press ENTER to continue")
            elif user_input == 7:
                # update a passenger
                index = input("Enter index: ")
                print("Leave empty if you don't want to update the field (ENTER)")
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                passportID = input("Enter passportID: ")
                planeID = input("Enter planeID: ")
                try:
                    self.__service.update_passenger(index, first_name, last_name, passportID, planeID)
                    print("Passenger updated successfully")
                    sleep(1)
                except Exception as e:
                    print(e)
                    sleep(1)
            elif user_input == 8:
                # delete a passenger
                index = input("Enter index: ")
                try:
                    self.__service.delete_passenger_by_index(index)
                    print("Passenger deleted successfully")
                    sleep(1)
                except Exception as e:
                    print(e)
                    sleep(1)
            else:
                print("Invalid input")
                sleep(1)
    
    def __general_menu(self):
        while(True):
            self.__ui.clear_menu()
            self.__ui.print_general_menu()
            user_input = self.__ui.get_input()
            while(user_input == None or user_input == ""):
                print("Please enter an integer")
                user_input = self.__ui.get_input()
            if user_input == 0:
                self.__main_menu()
            elif user_input == 1:
                # Sort passengers by last name
                planeID = input("Enter planeID: ")
                self.__print_planes(self.__service.sort_passengers_in_plane_by_last_name(planeID))
                input("Press ENTER to continue")
            elif user_input == 2:
                # Sort planes according to the number of passengers
                self.__print_planes(self.__service.sort_planes_by_number_of_passengers())
                input("Press ENTER to continue")
            elif user_input == 3:
                # Sort planes accordubg to the number of passengers witht he first name with given substring
                substring = input("Enter substring: ")
                self.__print_planes(self.__service.sort_planes_by_number_of_passengers_and_first_name_given_substring(substring))
                input("Press ENTER to continue")
            elif user_input == 4:
                # Sort planes according to the string obtained by concatenation of the number of passengers in the plane and the destination
                self.__print_planes(self.__service.sort_planes_by_number_of_passengers_and_destination())
                input("Press ENTER to continue")
            elif user_input == 5:
                # Identify planes that have passengers with passport numbers starting with the same 3 letters
                self.__print_planes(self.__service.get_planes_with_passengers_with_passport_starting_with_same_3_letters())
                input("Press ENTER to continue")
            elif user_input == 6:
                # Identify passengers from a given plane for which the first name or last name contatin a string given as parameter
                planeID = input("Enter planeID: ")
                string = input("First or last name: ")
                try:
                    self.__print_passengers(self.__service.passenger_from_plane_having_first_or_last_name_like_string(planeID, string), "Plane")
                    input("Press ENTER to continue")
                except Exception as e:
                    print(e)
                    sleep(1)
            elif user_input == 7:
                # Identify plane(s) where there is a passenger with a given name
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                try:
                    plane_list = self.__service.get_planes_with_passenger_name(first_name, last_name)
                    self.__print_planes(plane_list)
                    input("Press ENTER to continue")
                except Exception as e:
                    print(e)
                    sleep(1)
            elif user_input == 8:
                # Form groups of [k] passengers from the same plane but with different last names
                planeID = input("Enter planeID: ")
                k = input("Enter the number of elements in the group: ")
                try:
                    groups = self.__service.groups_of_passengers_from_same_plane(planeID, k)
                    for index, group in enumerate(groups):
                        print(f"Group {index+1}:")
                        self.__print_planes(group)
                        print("", end="\n")
                    input("Press ENTER to continue")
                except:
                    print("Invalid input")
                    sleep(1)
            elif user_input == 9:
                # Form groups of [k] planes with the same destination but belonging to different airline companies
                k = input("Enter the number of elements in the group: ")
                try:
                    groups = self.__service.groups_of_planes_with_same_destination_different_airline(k)
                    for index, group in enumerate(groups):
                        print(f"Group {index+1}:")
                        self.__print_planes(group)
                        print("", end="\n")
                    input("Press ENTER to continue")
                except:
                    print("Invalid input")
                    sleep(1)
            else:
                print("Invalid input")
                sleep(1)

    def __main_menu(self):
        self.__service.read_from_file_passenger()
        self.__ui.clear_menu()
        while True:
            self.__ui.print_main_menu()
            user_input = self.__ui.get_input()
            while(user_input == None or user_input == ""):
                print("Please enter an integer")
                user_input = self.__ui.get_input()
            if user_input == 0:
                option = input("Save data to file? (y/n): ")
                while option != "y" and option != "n":
                    print("Invalid input")
                    option = input("Save data to file? (y/n): ")
                if option == "y":
                    self.__service.write_to_file_passenger()
                self.__print_exit()
                exit()
            elif user_input == 1:
                self.__plane_menu()
            elif user_input == 2:
                self.__passenger_menu()
            elif user_input == 3:
                self.__general_menu()
            else:
                print("Invalid input")
        
    def run(self):
        self.__main_menu()
                
            
    
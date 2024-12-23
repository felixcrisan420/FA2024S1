from domain.plane import Plane
from utils.utilities import FileHandler
from constants.const import Constants as const
import os

class PlaneRepository:
    def __init__(self):
        """
        Constructor for PlaneRepository class.

        Args:
            None

        Returns:
            None
        """
        self.__plane_list = []
    
    # CRUD Operations for Plane
    # Create
    def add_plane(self, plane:Plane)->Plane:
        """
        Add a plane to the plane list.

        Args:
            plane (Plane): The plane object to be added.

        Returns:
            Plane: The plane object that was added.
        """
        self.__plane_list.append(plane)
        return plane

    # Read
    def get_plane_list(self)->list[Plane]:
        """
        Getter for the plane list.

        Args:
            None

        Returns:
            list[Plane]: The list of planes.
        """
        return self.__plane_list
    
    def get_plane_by_index(self, index:int)->Plane:
        """
        Getter for a plane by index.

        Args:
            index (int): The index of the plane.

        Returns:
            Plane: The plane object at the index.
        """
        return self.__plane_list[index]
    
    def get_index_by_plane(self, search_plane:Plane)->int:
        """
        Getter for the index of a plane.

        Args:
            search_plane (Plane): The plane object to search for.

        Returns:
            int: The index of the plane.
        """
        index=0
        for plane in self.__plane_list:
            index += 1
            if plane==search_plane:
                return index
        if index == 0 or index == len(self.__plane_list):
            return -1
        
    def get_index_by_planeID(self, planeID:str)->int:
        """
        Getter for the index of a plane by planeID.

        Args:
            planeID (str): The planeID of the plane.

        Returns:
            int: The index of the plane.
        """
        index=0
        for plane in self.__plane_list:
            index += 1
            if plane.get_planeID() == planeID:
                return index
        if index == 0 or index == len(self.__plane_list):
            return -1
        
    def get_plane_by_planeID(self, planeID:str)->Plane:
        """
        Getter for a plane by planeID.

        Args:
            planeID (str): The planeID of the plane.
        
        Returns:
            Plane: The plane object with the planeID.
        """
        for plane in self.__plane_list:
            if plane.get_planeID() == planeID:
                return plane
        return Plane(0, "Does not exist", 0, "Does not exist")
    
    def get_passenger_list(self, planeID:str)->list:
        """
        Getter for the passenger list of a plane.

        Args:
            planeID (str): The planeID of the plane.

        Returns:
            list: The list of passengers on the plane.
        """
        temp_list = []
        for plane in self.__plane_list:
            if plane.get_planeID() == planeID:
                temp_list.append(plane)
        return temp_list
        
    # Update
    def update_plane(self, index:int, plane:Plane)->Plane:
        """Update a plane in the list.

        Args:
            index (int): The index of the plane in the list.
            plane (Plane): The updated plane object.

        Returns:
            Plane: The updated plane object.
        """
        self.__plane_list[index].set_planeID(plane.get_planeID())
        self.__plane_list[index].set_airline_company(plane.get_airline_company())
        self.__plane_list[index].set_number_of_seats(plane.get_number_of_seats())
        self.__plane_list[index].set_destination(plane.get_destination())
        return self.__plane_list[index]

    # Delete
    def delete_plane_by_index(self, index:int)->Plane:
        """Delete a plane by index.

        Args:
            index (int): The index of the plane in the list.
            
        Returns:
            Plane: The plane object that was deleted.
        """
        plane = self.__plane_list[index]
        del self.__plane_list[index]
        return plane
    
    def delete_plane_by_object(self, plane:Plane)->Plane:
        """Delete a plane by object.

        Args:
            plane (Plane): The plane object to be deleted.

        Returns:
            Plane: The plane object that was deleted.
        """
        self.__plane_list.remove(plane)
        return plane
    
    def delete_plane(self, plane:Plane)->Plane:
        """Delete a plane from the list.

        Args:
            plane (Plane): The plane to be deleted.

        Returns:
            Plane: The plane that was deleted.
        """
        self.__plane_list.remove(plane)
        return plane
    
    def show_remaining_seats(self, planeID:str)->int:
        """Show the remaining seats on a plane.

        Args:
            planeID (str): The planeID of the plane.

        Returns:
            int: The number of remaining seats on the plane.
        """
        for plane in self.__plane_list:
            if plane.get_planeID() == planeID:
                return plane.get_number_of_seats() - len(self.get_passenger_list(planeID))
        return
    
    def read_from_file(self)->list[Plane]:
        """Read from file.

        Returns:
            list[Plane]: The list of planes.
        """
        for plane in FileHandler.read_from_file(const.FILE_NAME_PLANE, Plane):
            self.__plane_list.append(plane)
        return self.__plane_list
    
    def write_to_file(self)->list[Plane]:
        """Write to file.

        Returns:
            list[Plane]: The list of planes.
        """
        FileHandler.write_to_file(const.FILE_NAME_PLANE, self.__plane_list)
        return self.__plane_list

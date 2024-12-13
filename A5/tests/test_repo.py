from repository.repository import Repository
from repository.passenger_repository import PassengerRepository
from repository.plane_repository import PlaneRepository
from domain.plane import Plane
from domain.passenger import Passenger


if __name__=="__main__":
    # Test 10, and 11
    plane_repo = PlaneRepository()
    passenger_repo = PassengerRepository()
    repo = Repository(passenger_repo, plane_repo)
    plane1 = Plane("1", "Airline1", 100, "Destination1")
    plane2 = Plane("2", "Airline2", 100, "Destination1")
    plane3 = Plane("3", "Airline3", 100, "Destination1")
    plane4 = Plane("4", "Airline4", 100, "Destination2")
    plane5 = Plane("5", "Airline5", 100, "Destination2")
    plane6 = Plane("6", "Airline6", 100, "Destination2")
    plane_repo.add_plane(plane1)
    plane_repo.add_plane(plane2)
    plane_repo.add_plane(plane3)
    plane_repo.add_plane(plane4)
    plane_repo.add_plane(plane5)
    plane_repo.add_plane(plane6)
    passenger1 = Passenger("First1", "Last1", "Passport1", "1")
    passenger2 = Passenger("First2", "Last2", "Passport2", "1")
    passenger3 = Passenger("First3", "Last3", "Passport3", "1")
    passenger4 = Passenger("First4", "Last4", "Passport4", "1")
    passenger5 = Passenger("First5", "Last5", "Passport5", "1")
    passenger6 = Passenger("First6", "Last6", "Passport6", "1")
    passenger7 = Passenger("First7", "Last7", "Passport7", "1")
    passenger8 = Passenger("First8", "Last8", "Passport8", "3")
    passenger9 = Passenger("First9", "Last9", "Passport9", "3")
    passenger10 = Passenger("First10", "Last10", "Passport10", "4")
    passenger11 = Passenger("First11", "Last11", "Passport11", "4")
    passenger12 = Passenger("First12", "Last12", "Passport12", "4")
    passenger13 = Passenger("First13", "Last13", "Passport13", "1")
    passenger14 = Passenger("First14", "Last14", "Passport14", "1")
    passenger_repo.add_passenger(passenger1)
    passenger_repo.add_passenger(passenger2)
    passenger_repo.add_passenger(passenger3)
    passenger_repo.add_passenger(passenger4)
    passenger_repo.add_passenger(passenger5)
    passenger_repo.add_passenger(passenger6)
    passenger_repo.add_passenger(passenger7)
    passenger_repo.add_passenger(passenger8)
    passenger_repo.add_passenger(passenger9)
    passenger_repo.add_passenger(passenger10)
    passenger_repo.add_passenger(passenger11)
    passenger_repo.add_passenger(passenger12)
    passenger_repo.add_passenger(passenger13)
    passenger_repo.add_passenger(passenger14)
    print(repo.groups_of_passengers_from_same_plane("1", 2))
    print(repo.group_of_planes_with_same_destination_different_airline(3))
from abc import ABC, abstractmethod
from collections import defaultdict, deque
from enum import Enum
from typing import Optional


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    BIG = 3

# We will have an interface to allow us to have different logic of implementing the assigning of lots


class ParkingGarage(ABC):
    @abstractmethod
    def enter(self, car_size: Size, entry_number: int, license_plate: str) -> str:
        pass

    @abstractmethod
    def exit(self, entry_number: int, license_plate: str) -> None:
        pass

    @abstractmethod
    def get_num_spots(self) -> dict[Size, int]:
        pass


class ParkingSpot:
    def __init__(self, name: str, size: Size) -> None:
        self.name = name
        self.size = size
        self.is_vacant = True

    def allocate(self, license_plate: str):
        self.is_vacant = False
        self.allocated_license_plate = license_plate

    def vacate(self):
        self.is_vacant = True
        self.allocated_license_plate = None


class BasicParkingGarage(ParkingGarage):
    def __init__(self, num_of_parking_spots_per_type: dict[Size, int]) -> None:
        # create parking spots
        self.empty_parking_spots: defaultdict[Size,
                                              deque[ParkingSpot]] = defaultdict(deque)
        self.parked_spots: dict[str, ParkingSpot] = {}

        for type, num in num_of_parking_spots_per_type.items():
            for i in range(num):
                name = f'{type.name}_{i}'
                self.empty_parking_spots[type].append(ParkingSpot(name, type))

    def enter(self, car_size: Size, entry_number: int, license_plate: str) -> Optional[str]:
        num_spots = self.get_num_spots()
        if car_size not in num_spots:
            raise ValueError("No such parking spot size")

        if num_spots[car_size] < 1:
            return None

        if license_plate in self.parked_spots:
            raise ValueError("License plate already exist")

        # find the first vacant spot and assign car
        parking_spot = self.empty_parking_spots[car_size].popleft()
        parking_spot.allocate(license_plate)
        self.parked_spots[license_plate] = parking_spot

        return parking_spot.name

    def exit(self, entry_number: int, license_plate: str) -> None:
        if license_plate not in self.parked_spots:
            raise ValueError("License plate not found")
        parking_spot = self.parked_spots[license_plate]
        parking_spot.vacate()
        del self.parked_spots[license_plate]
        self.empty_parking_spots[parking_spot.size].append(parking_spot)

    def get_num_spots(self) -> dict[Size, int]:
        res = defaultdict(int)
        for size_member in Size:
            res[size_member] = len(self.empty_parking_spots[size_member])
        return res

'''
To allow retrieving of parking spots closest to the entry_number,

We can maintain a distance_from_entries that is a list of distances for each entry for each parking spot and then also maintain priority queues (min_heap) for each entry + size. 

Each time a car enters, we get the next parking spot from the priority queue of the size and entry_number, set the parking spot's distance to Int.MAX in ALL priority queues.
If the parking spot is not vacant, then we just return no spot

Whenever a car exits, we get the parking spot of the car, then update each priority queue with the distance from the entry.
'''
class OptimisedDistanceParkingGarage(ParkingGarage):
    def __init__(self) -> None:
        super().__init__()

    def enter(self, car_size: Size, entry_number: int, license_plate: str) -> str:
        return super().enter(car_size, entry_number, license_plate)

    def exit(self, entry_number: int, license_plate: str) -> None:
        return super().exit(entry_number, license_plate)

    def get_num_spots(self) -> dict[Size, int]:
        return super().get_num_spots()

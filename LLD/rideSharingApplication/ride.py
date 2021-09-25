from enum import Enum


class RideStatus(Enum):
    idle = "IDLE"
    created = "CREATED"
    withdraw = "WITHDRAW"
    completed = "COMPLETED"


class Ride:
    AVG_PRICE_PER_KM = 20

    def __init__(self, id=0, origin=0, destination=0, no_of_seats=0):
        self.__id = id
        self.__origin = origin
        self.__destination = destination
        self.__no_of_seats = no_of_seats
        self.__ride_status = RideStatus.idle

    def _set_destination(self, destination):
        self.__destination = destination

    def _set_origin(self, origin):
        self.__origin = origin

    def _set_seats(self, no_of_seats):
        self.__no_of_seats = no_of_seats

    def _set_ride_status(self, ride_status: RideStatus):
        self.__ride_status = ride_status

    def _set_id(self, id):
        self.__id = id

    def _get_ride_status(self):
        return self.__ride_status

    def _get_id(self):
        return self.__id

    def _calculate_fare(self, is_priority_rider):
        # print(self.__id, self.__origin, self.__destination, self.__no_of_seats)
        dist = self.__destination - self.__origin

        if self.__no_of_seats < 2:
            return dist * Ride.AVG_PRICE_PER_KM * (0.75 if is_priority_rider else 1)

        return dist * Ride.AVG_PRICE_PER_KM * (0.5 if is_priority_rider else 0.75)

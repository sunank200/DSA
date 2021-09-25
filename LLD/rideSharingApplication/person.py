# from abc import ABC, abstractmethod
from ride import Ride, RideStatus


class Person:
    def __init__(self, name):
        self.__name = name


class Driver(Person):
    def __init__(self, name):
        super().__init__(name)


class Rider(Person):
    __completed_rides = []
    __current_ride: Ride() = None

    def __init__(self, id, name):
        super().__init__(name)
        self.__id = id

    def _create_ride(self, origin, destination, no_of_seats, id):
        if origin >= destination:
            raise Exception("Wrong origin and destination.")
        self.__current_ride = Ride(id, origin, destination, no_of_seats)
        # self.__current_ride._set_destination(destination)
        # self.__current_ride._set_origin(origin)
        # self.__current_ride._set_id(id)
        # self.__current_ride._set_seats(no_of_seats)
        # self.__current_ride._set_ride_status(RideStatus.created)

    def _update_ride(self, origin, destination, no_of_seats, id):
        if self.__current_ride.__get_ride_status() == RideStatus.withdraw:
            raise Exception("Ride has been withdrawn.")

        if self.__current_ride.__get_ride_status() == RideStatus.completed:
            raise Exception("Ride has been completed.")

        if self.__current_ride.__get_id(id) != id:
            raise Exception("Ride id: {} is not active".format(id))

        self.__current_ride.__set_destination(destination)
        self.__current_ride.__set_origin(origin)
        self.__current_ride.__set_seats(no_of_seats)
        self.__current_ride.__set_ride_status(RideStatus.created)

    def _withdraw_ride(self, id):
        if self.__current_ride.__get_id() != id:
            raise Exception("Wrong id is entered.")

        if self.__current_ride.__get_ride_status() == RideStatus.created:
            raise Exception("Ride wasn't in progress.")

        self.__current_ride.__set_ride_status(RideStatus.withdraw)

    def _get_id(self):
        return self.__id

    def _close_ride(self):
        if self.__current_ride._get_ride_status() == RideStatus.created:
            raise Exception("Cannot closed the ride and it was not in progress.")

        self.__current_ride._set_ride_status(RideStatus.completed)
        self.__completed_rides.append(self.__current_ride)
        return self.__current_ride._calculate_fare(len(self.__completed_rides) >= 10)

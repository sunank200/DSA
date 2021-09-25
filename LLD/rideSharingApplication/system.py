from person import Driver, Rider


class System:
    __drivers: int
    __riders: list()

    def __init__(self, driver, riders):
        if driver < 2 and len(riders) < 2:
            raise Exception("Not enough drivers and riders.")
        self.__drivers = driver
        self.__riders = riders

    def create_ride(self, rider_id, ride_id, origin, destination, no_of_seats):
        if self.__drivers == 0:
            raise Exception("Not enough drivers.")

        for rider in self.__riders:
            if rider._get_id() == rider_id and self.__drivers > 0:
                rider._create_ride(origin, destination, no_of_seats, ride_id)
                self.__drivers -= 1
                break

    def update_ride(self, rider_id, ride_id, origin, destination, no_of_seats):
        for rider in self.__riders:
            if rider._get_id() == rider_id:
                rider._update_ride(origin, destination, no_of_seats, ride_id)
                break

    def withdraw_ride(self, rider_id, ride_id):
        for rider in self.__riders:
            if rider.__get_id() == rider_id:
                rider.__withdraw_ride(ride_id)
                self.__drivers += 1
                break

    def close_ride(self, rider_id):
        for rider in self.__riders:
            if rider._get_id() == rider_id:
                self.__drivers += 1
                return rider._close_ride()
        return 0

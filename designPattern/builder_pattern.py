"""
https://sbcode.net/python/builder/
"""
from abc import ABCMeta, abstractmethod


class IHouseBuilder(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def set_building_type(building_type):
        "Building Type"

    @staticmethod
    @abstractmethod
    def set_wall_material(wall_material):
        "Wall material"

    @staticmethod
    @abstractmethod
    def set_number_of_doors(number_of_doors):
        "Number of doors"

    @staticmethod
    @abstractmethod
    def set_number_of_windows(number_of_windows):
        "Number of Windows"

    @staticmethod
    @abstractmethod
    def get_result():
        "Return the final product"


class House:
    def __init__(
        self, wall_material="Brick", building_type="Apartment", doors=1,
            windows=1
    ):
        self.wall_matrial = wall_material
        self.building_type = building_type
        self.doors = doors
        self.windows = windows

    def construction(self):
        return "This is {} {} with {} doors and {} windows".format(
            self.wall_matrial, self.building_type, self.doors, self.windows
        )


class HouseBuilder(IHouseBuilder):
    def __init__(self):
        self.house = House()

    def set_building_type(self, building_type):
        self.house.building_type = building_type
        return self

    def set_wall_material(self, wall_material):
        self.house.wall_matrial = wall_material
        return self

    def set_number_of_doors(self, number_of_doors):
        self.house.doors = number_of_doors
        return self

    def set_number_of_windows(self, number_of_windows):
        self.house.windows = number_of_windows
        return self

    def get_result(self):
        return self.house


class IHouseDirector(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def construct():
        "Build a house"


class BoatHouseDirector(IHouseDirector):
    def __init__(self):
        self.house_builder = HouseBuilder()

    def construct(self):
        return (
            self.house_builder.set_building_type("House Boat")
            .set_number_of_windows(8)
            .set_number_of_doors(2)
            .set_wall_material("cement")
            .get_result()
        )


class CastleHouseDirector(IHouseDirector):
    def __init__(self):
        self.house_builder = HouseBuilder()

    def construct(self):
        return (
            self.house_builder.set_building_type("Castle")
            .set_wall_material("Stone")
            .set_number_of_doors(10)
            .set_number_of_windows(20)
            .get_result()
        )


if __name__ == "__main__":
    BOAT_HOUSE = BoatHouseDirector().construct()
    CASTLE = CastleHouseDirector().construct()

    print(BOAT_HOUSE.construction())
    print(CASTLE.construction())

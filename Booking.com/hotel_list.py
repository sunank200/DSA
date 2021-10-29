# Price combinations
# Given hotel blocks (room + price + features) per date (date is represented by an integer here):

# Example dataset:
# AVAILABILITY = {
#     176: [
#         {
#             'price': 120,
#             'features': [ 'breakfast', 'refundable' ],
#             'availability': 5
#         },
#       {
#         'price': 200,
#         'features': [ 'breakfast', 'refundable', 'wifi' ],
#         'availability': 3
#       }
#     ],
#     177: [
#         {
#             'price': 120,
#             'features': [ 'breakfast', 'refundable' ],
#             'availability': 1
#         },
#         {
#             'price': 130,
#             'features': [ 'wifi', 'breakfast', ],
#             'availability': 3
#         },
#         {
#             'price': 150,
#             'features': [ 'wifi', 'breakfast', 'refundable' ],
#             'availability': 7
#         }
#     ]
# }

# Example user input:
# {
#  checkin: 176,
#  checkout: 178,
#  features: [ 'breakfast' ],
#  rooms: 1
# }

# Example output:
# [
#  {
#    price: 240,
#    features: [ 'breakfast', 'refundable' ],
#    availability: 1
#  },
#  {
#    price: 250,
#    features: [ 'breakfast' ],
#    availability: 3
#  },
#  {
#    price: 270,
#    features: [ 'breakfast', 'refundable' ],
#    availability: 5
#  },
# ]

# Implement a search algorithm, that for a range of dates would return
# an array of available date/rate combinations.
# Number of combination of items [2,3,4] => 24


class Room:
    def __init__(self, availability, price, feature):
        self.availability = availability
        self.price = price
        self.feature = feature


def search(checkin: int, checkout: int, features: List[str], rooms: int) -> List[Dict]:
    for date in AVAILABILITY:
        if date >= checkin and date <= checkout:
            rooms = AVAILABILITY.get(date)
            for inidividual_room in rooms:
                room_obj_feature = inidividual_room["features"]
                room_obj_avail = inidividual_room["availability"]
                room_obj_price = inidividual_room["price"]


# this_room =    {
#      'price': 120,
#     'features': [ 'breakfast', 'refundable' ],
#     'availability': 5
# },
# that_room = {
#   {
#     'price': 150,
#     'features': [ 'wifi', 'breakfast', 'refundable' ],
#     'availability': 7
#   }
# out = {
#    price: 270,
#    features: [ 'breakfast', 'refundable' ],
#    availability: 5
#  }


def feature_check(rooms_feature, feature):
    for individual_feature in feature:
        if individual_feature not in rooms_feature:
            return False
    return True


feature_check(["wifi", "breakfast"], ["breakfast"])


def room_availability(room_aval, aval):
    return room_aval <= aval


def combine(this_room, that_room, feature, rooms):
    this_room_feature = this_room.get("features")
    this_room_availability = this_room.get("availability")
    if feature_check(this_room_feature, feature) and room_availability(
        this_room_availability, rooms
    ):
        include_this_room = True

    that_

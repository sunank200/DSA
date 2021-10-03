from enum import Enum


class ReservationStatus(Enum):
    WAITING = 1
    PENDING = 2
    CANCELED = 3
    NONE = 4
    COMPLETED = 5


class BookReservation:
    def __init__(self, creation_date, status, book_instance_barcode, member_id):
        self.__creation_date = creation_date
        self.__status = status
        self.__book_instance_barcode = book_instance_barcode
        self.__member_id = member_id

    def fetch_reservation(self, barcode):
        None


class BookLending:
    def __init__(self, creation_date, due_date, book_instance_barcode, member_id):
        self.__creation_date = creation_date
        self.__due_date = due_date
        self.__return_date = None
        self.__book_instance_barcode = book_instance_barcode
        self.__member_id = member_id

    def lend_books(self, barcode, member_id):
        None

    def fetch_lending_details(self, barcode):
        None


class Fine:
    def __init__(self, creation_date, book_instance_barcode, member_id):
        self.__creation_date = creation_date
        self.__book_instance_barcode = book_instance_barcode
        self.__member_id = member_id

    def collect_fine(self, member_id, days):
        None

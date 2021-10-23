import datetime
from abc import ABCMeta, abstractstaticmethod
from enum import Enum

from Book import BookStatus
from BookReservation import BookLending, BookReservation, Fine, ReservationStatus


class Constants:
    MAX_BOOK_ISSUED_TO_A_USER = 5
    MAX_LENDING_DAYS = 10


class AccountStatus(Enum):
    ACTIVE = 1
    CANCELED = 2
    BLACKLISTED = 3


class Account(metaclass=ABCMeta):
    def __init__(self, id, password, person, status=AccountStatus.ACTIVE):
        self.__id = id
        self.__person = person
        self.__password = password
        self.__status = status

    @abstractstaticmethod
    def reset_password(self):
        pass


class Librarian(Account):
    def __init__(self, id, password, person, status=AccountStatus.ACTIVE):
        super().__init__(id, password, person, status)

    def add_book_instance(self, book_instance):
        None

    def block_member(self, member_id):
        None

    def unblock_member(self, member_id):
        None


class Member(Account):
    def __init__(self, id, password, person, status=AccountStatus.ACTIVE):
        super().__init__(id, password, password, status)
        self.__date_of_membership = datetime.datetime.now()
        self.__total_books_checked_out = 0

    def get_id(self):
        return self.__id

    def get_total_books_checkout(self):
        return self.__total_books_checked_out

    def reserve_book_instance(self, book_instance):
        None

    def increment_total_book_checkout(self):
        None

    def renew_book_item(self, book_instance):
        None

    def checkout_book_instance(self, book_instance):
        if self.get_total_books_checkout() >= Constants.MAX_BOOK_ISSUED_TO_A_USER:
            raise Exception("Max booking lending limit reached.")

        book_reservation = BookReservation.fetch_reservation(
            book_instance.get_barcode()
        )
        if book_reservation != None and book_reservation.get_member_id != self.get_id():
            raise Exception("Reverved by others.")

        elif book_reservation != None:
            book_reservation.update_status = ReservationStatus.COMPLETED

        if not book_instance.checkout(self.get_id):
            return False

        self.increment_total_book_checkout()
        return True

    def check_for_fine(self, book_instance_barcode):
        book_lending = BookLending.fetch_lending_details(book_instance_barcode)
        due_date = book_lending.get_due_date()
        today = datetime.datetime.today()

        if today > due_date:
            diff = today - due_date
            diff_days = diff.days
            Fine.collect_fine(self.get_member_id(), diff_days)

    def return_book_instance(self, book_instance):
        self.check_for_fine(book_instance.get_barcode())
        book_reservation = BookReservation.fetch_reservation(
            book_instance.get_barcode()
        )

        if book_reservation is not None:
            book_instance.update_book_item_status(BookStatus.RESERVED)
            # book_reservation.send_notification()

        book_instance.update_book_item_status(BookStatus.AVAILABLE)

    def renew_book_instance(self, book_instance):
        self.check_for_fine(book_instance.get_barcode())
        book_reservation = BookReservation.fetch_reservation(
            book_instance.get_barcode()
        )

        if (
            book_reservation is not None
            and book_reservation.get_member_id is not self.get_id()
        ):
            book_instance.decrement_total_book_checkout()
            book_instance.update_book_item_status(BookStatus.RESERVED)
            # book_reservation.send_notification()
            return False
        elif book_reservation is not None:
            book_reservation.update_status(ReservationStatus.COMPLETED)

        BookLending.lend_books(book_instance.get_barcode(), self.get_id())
        book_instance.update_due_date(
            datetime.datetime.now().AddDays(Constants.MAX_LENDING_DAYS)
        )
        return True

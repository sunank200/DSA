from abc import ABCMeta, abstractmethod
from enum import Enum

from BookReservation import BookLending


class BookFormat(Enum):
    HARDCOVER = 1
    PAPERBACK = 2
    KINDLE = 3


class BookStatus(Enum):
    AVAILABLE = 1
    RESERVED = 2
    LOANED = 3
    LOST = 4


class Book(metaclass=ABCMeta):
    def __init__(self, ISBN, title, subject, publisher, language, number_of_pages):
        self.__ISBN = ISBN
        self.__title = title
        self.__subject = subject
        self.__publisher = publisher
        self.__language = language
        self.__number_of_pages = number_of_pages
        self.__authors = []


class BookInstance(Book):
    def __init__(
        self,
        barcode,
        is_reference_only,
        borrowed,
        due_date,
        book_format,
        status,
        date_of_purchase,
        publication_date,
        placed_at,
    ):
        self.__barcode = barcode
        self.__is_reference_only = is_reference_only
        self.__borrowed = borrowed
        self.__due_date = due_date
        self.__book_format = book_format
        self.__status = status
        self._date_of_purchase = date_of_purchase
        self.__publication_date = publication_date
        self.__placed_at = placed_at

    @property
    def is_reference_only(self):
        return self.__is_reference_only

    @is_reference_only.setter
    def is_reference_only(self, is_reference_only):
        self.__is_reference_only = is_reference_only

    def checkout(self, member_id):
        if self.is_reference_only:
            raise Exception("Book is for reference only.")
            return False

        if not BookLending.lend_books(self.get_barcode(), member_id):
            return False

        self.update_book_item_status(BookStatus.LOANED)
        return True

    def update_book_item_status(self, status):
        self.__status = status


class Rack:
    def __init__(self, number, location_identifier):
        self.__number = number
        self.__location_identifier = location_identifier

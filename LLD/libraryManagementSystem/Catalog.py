from abc import ABCMeta, abstractmethod


class Search(metaclass=ABCMeta):
    @abstractmethod
    def search_by_title(self, title):
        pass

    @abstractmethod
    def search_by_author(self, author):
        pass

    @abstractmethod
    def search_by_publisher(self, publisher):
        pass

    @abstractmethod
    def search_by_publish_date(self, publish_date):
        pass


class Catalog(Search):
    def __init__(self):
        self.__book_titles = {}
        self.__book_authors = {}
        self.__book_subjects = {}
        self.__book_publication_dates = {}

    def search_by_title(self, query):
        return self.__book_titles.get(query)

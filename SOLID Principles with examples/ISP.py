# Interface Segregation Principle
# Definition: Many client-facing interfaces are better than one general-purpose interface
# We should not force client to implement interfaces they do not use. Instead of creating one big interface we can break it down in smaller interfaces


# Consider ReferenceBook class as well which can not be checked out or reserved, just read in library and keep it back

# Bad example
from abc import ABC, abstractmethod

# Here there are many properties and methods that are either not used by Book class or Seat class
# This is a violation of the Interface Segregation Principle (ISP)
# ILibraryItem should not have methods and properties that are not relevant to all library items, such as return_due_date, pages, author, etc.

class ILibraryItem(ABC):
    library_id: int
    title: str
    total_copies: int
    available_copies: int
    pages: int
    author: str
    publisher: str
    publication_year: int
    genre: str
    return_due_date: str

    @abstractmethod
    def check_out(self):
        pass

    @abstractmethod
    def return_item(self):
        pass

    @abstractmethod
    def reserve(self):
        pass

    @abstractmethod
    def get_due_date(self):
        pass

class Book(ILibraryItem):
    def __init__(self, library_id, title, total_copies, available_copies, pages, author, publisher, publication_year, genre, return_due_date):
        self.return_due_date = return_due_date
        self.library_id = library_id
        self.title = title
        self.total_copies = total_copies
        self.available_copies = available_copies
        self.pages = pages
        self.author = author
        self.publisher = publisher
        self.publication_year = publication_year
        self.genre = genre

    def check_out(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        return False

    def return_item(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        return False

    def reserve(self):
        raise NotImplementedError("Reservation not supported for books.")

    def get_due_date(self):
        return self.return_due_date
    
class Seat(ILibraryItem):
    def __init__(self, library_id):
        self.library_id = library_id

    def check_out(self):
        raise NotImplementedError("Checkout is not supported for seats.")

    def return_item(self):
        raise NotImplementedError("Item return is not supported for seats.")

    def reserve(self):
        print("Seat reserved.")

    def get_due_date(self):
        self.return_due_date


# Good example
# Here we have separated the interfaces into smaller ones that are more specific to the type of item


class ILibraryItem(ABC):
    library_id: int
    return_due_date: str
    booking_name: str
    booking_id: int

    @abstractmethod
    def get_booking_details(self):
        pass

    @abstractmethod
    def get_due_date(self):
        pass

class Book(ILibraryItem):
    title: str
    total_copies: int
    available_copies: int
    pages: int
    author: str
    publisher: str
    publication_year: int
    def __init__(self, library_id, title, total_copies, available_copies, pages, author, publisher, publication_year, genre, return_due_date):
        self.return_due_date = return_due_date
        self.library_id = library_id
        self.title = title
        self.total_copies = total_copies
        self.available_copies = available_copies
        self.pages = pages
        self.author = author
        self.publisher = publisher
        self.publication_year = publication_year
        self.genre = genre

    def get_booking_details(self):
        return f"Book: {self.title}, Author: {self.author}, Available Copies: {self.available_copies}"

    def get_due_date(self):
        return self.return_due_date
    
    def check_out(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        return False
    
    def return_item(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        return False

class SeatReservation(ILibraryItem):
    seet_number: str
    floor: int
    zone: str
    def __init__(self, library_id, seat_number, floor, zone, return_due_date, booking_name, booking_id):
        self.booking_name = booking_name
        self.booking_id = booking_id
        self.return_due_date = return_due_date
        self.library_id = library_id
        self.seat_number = seat_number
        self.floor = floor
        self.zone = zone

    def get_booking_details(self):
        return f"Seat Number: {self.seat_number}, Floor: {self.floor}, Zone: {self.zone}, Booking Name: {self.booking_name}"

    def get_due_date(self):
        return self.return_due_date
    
    def reserve(self):
        print(f"Seat {self.seat_number} reserved for {self.booking_name}.")
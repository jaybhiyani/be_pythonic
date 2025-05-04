# Liskov Substitution Principle
# Definition: Objects in a program should be replaceable with instances of their subtypes without altering the correctness of the program
# If a program is using a Base class then the ref of Base class can be replaceable with its Derived class/type without affecting
# We can also state that Derived types are substitutable for their base types
# This principle encourrages us to use inheritance and polymorphism in a way that allows us to create flexible and reusable code
# Example: Let's say we have a class called Bird and a subclass called Penguin. The Bird class has a method fly() that allows birds to fly.
# However, penguins cannot fly. This violates the Liskov Substitution Principle because if we replace a Bird object with a Penguin object,
# the program will not work as expected.
# To fix this, we can create a new class called FlightlessBird that inherits from Bird and overrides the fly() method to raise an exception.
# Encourrages the usage of interfaces with IS-A relationship.
# Layman terms, Derived class should be able to do everything that the Base class can do.

#Bad example
from abc import ABC, abstractmethod

class BaseDatabase:
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def caching(self):
        pass

class MySQLDatabase(BaseDatabase):
    def connect(self):
        print("Connecting to MySQL database...")

    def disconnect(self):
        print("Disconnecting from MySQL database...")

    # This here violates the Liskov Substitution Principle because MySQLDatabase does not support caching.
    # This method is not applicable to MySQLDatabase and should not be part of its interface.
    # This is a violation of the Liskov Substitution Principle because if we replace BaseDatabase with MySQLDatabase,
    # the program will not work as expected when it tries to call the caching() method.
    # to fix this create an interface for caching and implement it in the classes that support caching
    def caching(self):
        raise Exception("Caching not supported in MySQLDatabase")


class PostgreSQLDatabase(BaseDatabase):
    def connect(self):
        print("Connecting to PostgreSQL database...")

    def disconnect(self):
        print("Disconnecting from PostgreSQL database...")

    def caching(self):
        print("Caching enabled in PostgreSQL database...")


class DatabaseService:
    def __init__(self, database: BaseDatabase):
        self.database = database

    def perform_operations(self):
        self.database.connect()
        self.database.caching()  # This will raise an exception if MySQLDatabase is used
        # Perform some operations
        self.database.disconnect()

# Good example

class BaseDatabase:
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

class ICachable(ABC):
    # What does mentioning ABC does to this, it makes this class an abstract class and we cannot create an instance of this class.
    # This is an interface that defines the caching method. And the class that implements this interface must provide an implementation for the caching method.
    # This is a good example of the Liskov Substitution Principle because if we replace BaseDatabase with ICachable
    # And when we do not mention ABC, we can create an instance of this class and it will not throw an error. Also we can ignore the caching method.
    @abstractmethod
    def caching(self):
        pass

class MySQLDatabase(BaseDatabase):
    def connect(self):
        print("Connecting to MySQL database...")

    def disconnect(self):
        print("Disconnecting from MySQL database...")

class PostgreSQLDatabase(BaseDatabase, ICachable):
    # This method is applicable to PostgreSQLDatabase and should be part of its interface.
    # This is a good example of the Liskov Substitution Principle because if we replace BaseDatabase with PostgreSQLDatabase,
    # the program will work as expected when it tries to call the caching() method.
    def caching(self):
        print("Caching enabled in PostgreSQL database...")

    def connect(self):
        print("Connecting to PostgreSQL database...")

    def disconnect(self):
        print("Disconnecting from PostgreSQL database...")


def main():
    # Create instances of the databases
    mysql_db = MySQLDatabase()
    postgres_db = PostgreSQLDatabase()

    # Connect to the databases
    mysql_db.connect()
    postgres_db.connect()

    # Disconnect from the databases
    mysql_db.disconnect()
    postgres_db.disconnect()

    # Caching is only applicable to PostgreSQLDatabase
    if isinstance(postgres_db, ICachable):
        postgres_db.caching()

main()
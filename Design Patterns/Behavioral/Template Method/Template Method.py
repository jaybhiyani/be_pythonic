# Template Method Pattern
# Template Method Pattern Implementation in Python with Classes and Decorators
# The Template Method pattern is a behavioral design pattern that defines the skeleton of an algorithm in a base class, 
# but lets subclasses override specific steps of the algorithm without changing its overall structure.


# Object Oriented example
from abc import ABC, abstractmethod

class DataProcessor(ABC): # template class
    def read_data(self):
        print("Reading data...")
    
    @abstractmethod
    def enrich_data(self):
        pass

    def columns_renamer(self):
        print("Renaming columns...")

    @abstractmethod
    def save_data(self):
        pass

class MSSQLDataProcessor(DataProcessor): # concrete class
    def enrich_data(self):
        print("Enriching data as per MSSQL format requirements...")

    def save_data(self):
        print("Saving data to MSSQL DB...")

class MongoDBDataProcessor(DataProcessor): # concrete class
    def enrich_data(self):
        print("Enriching data as per MongoDB format requirements...")

    def save_data(self):
        print("Saving data to MongoDB DB...")
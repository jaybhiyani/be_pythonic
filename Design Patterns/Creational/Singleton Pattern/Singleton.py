import threading
# 1  with class variable, classic method
class Singleton_Logger_Traditional:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
def main_traditional_logger():
    singleton1 = Singleton_Logger_Traditional()
    singleton2 = Singleton_Logger_Traditional()

    print(f"Singleton 1 ID: {id(singleton1)}")
    print(f"Singleton 2 ID: {id(singleton2)}")
    print(f"Are both instances the same? {singleton1 is singleton2}")


class Singleton_Logger_Traditional_Threadsafe:
    _instance = None
    _lock = threading.Lock()  # Ensures thread-safe access

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:  # Lock is acquired by one thread at a time
                if cls._instance is None:  # Double-checked locking
                    cls._instance = super().__new__(cls)
                    cls._instance.log_file = "app.log"
        return cls._instance

    def log(self, message):
        with open(self.log_file, "a") as f:
            f.write(message + "\n")
        print(f"Logged: {message}")

def main_traditional_logger_threadsafe():
    logger1 = Singleton_Logger_Traditional_Threadsafe()
    logger2 = Singleton_Logger_Traditional_Threadsafe()

    print(logger1 is logger2)  # True

    logger1.log("Starting the application")
    logger2.log("Application running")


############################################ 2 with decorator ###############################################

def singleton_decorator(cls): # this decorator ensures that only one instance of the class is created
    instances = {} # dictionary to hold the instances as we would need our decorator to work for multiple classes
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton_decorator
class Singleton_Logger_Decorator:
    logger_mode = 'print'  # default logger mode
    def __init__(self, logger_mode):
        self.logger_mode = logger_mode

    def log(self, message):
        print(f"Logged: {message}")
        pass

def main_decorator_logger():
    logger1 = Singleton_Logger_Decorator('print')
    logger2 = Singleton_Logger_Decorator('file')

    print(logger1 is logger2)  # True

    logger1.log("Starting the application")
    logger2.log("Application running")


################################################# 3 with metaclass ###############################################

class Singleton_Logger_Meta(type): # (type) -> type is a default metaclass in Python from where all classes are derived
    _instances = {}

    def __call__(cls, *args, **kwargs):
        print(f"Metaclass __call__ method called {cls.__name__}")
        if cls not in cls._instances:
            print(f"Creating a new instance of {cls.__name__} from metaclass __call__")
            instance = super().__call__(cls, *args, **kwargs)
            cls._instances[cls] = instance
        else:
            print(f"Returning existing instance of {cls.__name__} from metaclass __call__")
        return cls._instances[cls]    

class Singleton_Logger_Meta_Example(metaclass=Singleton_Logger_Meta):
    def __init__(self, logger_mode):
        self.logger_mode = logger_mode

    def log(self, message):
        print(f"Logged: {message}")

def main_meta_logger():
    logger1 = Singleton_Logger_Meta_Example('print')
    logger2 = Singleton_Logger_Meta_Example('file')

    print(logger1 is logger2)  # True

    logger1.log("Starting the application")
    logger2.log("Application running")

if __name__ == "__main__":
    # main_traditional_logger()
    # main_traditional_logger_threadsafe()
    # main_decorator_logger()
    main_meta_logger()
# Dependency Inversion Principle
# Definition: One should depend on Abstractions and not on Conretions
# Abstractions should not depend on the details, instead details should depend on Abstractions
# High-level module should not depend on low level modules
# Here in this example, we can see that the initial version, HIgh-level module (AccountOperations) is depending on Low-level modules (EmailService and Logger)
# Now if we want to change the implementation of EmailService or Logger, we need to change the AccountOperations class as well. This is a violation of DIP.
# To fix this, we can create interfaces for EmailService and Logger and make the AccountOperations class depend on these interfaces instead of the concrete 
# mplementations. This way, we can change the implementation of EmailService or Logger without affecting the AccountOperations class.

from abc import ABC, abstractmethod
# Bad Example
class EmailService:
    def send_email(self, message):
        print(f"Sending email: {message}")  # Low-level module

class Logger:
    def log(self, message):
        print(f"Logging message: {message}")  # Low-level module

class AccountOperations: # High-level module
    def __init__(self):
        self.logger = Logger() # Low-level module strictly coupled
        self.email_service = EmailService() # Low-level module strictly coupled

    def deposit(self, amount):
        # Deposit logic
        self.logger.log(f"Deposited {amount}")
        self.email_service.send_email(f"Deposited {amount}")
    

# Good Example

class EmailServiceInterface(ABC):
    @abstractmethod
    def send_email(self, message):
        pass


class LoggerInterface(ABC):
    @abstractmethod
    def log(self, message):
        pass


class EmailService(EmailServiceInterface):
    def send_email(self, message):
        print(f"Sending email: {message}")  # Low-level module


class Logger(LoggerInterface):
    def log(self, message):
        print(f"Logging message: {message}")  # Low-level module


class AccountOperations:  # High-level module
    def __init__(self, logger: LoggerInterface, email_service: EmailServiceInterface):
        self.logger = logger  # High-level module depends on abstraction
        self.email_service = email_service  # High-level module depends on abstraction

    def deposit(self, amount):
        # Deposit logic
        self.logger.log(f"Deposited {amount}")
        self.email_service.send_email(f"Deposited {amount}")

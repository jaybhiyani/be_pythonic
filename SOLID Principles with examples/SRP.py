# Definition:
# A class should have only one reason to change.
# Every module or a class should have responsibility over a single part of the functionality provided by the software, and that responsibility
# should be entirely encapsulated by the class
# Each class and module should focus on a single task at a time
# Every thing in the class should be related to that single purpose
# There can be multiple members in the class as long as they fulfil the same purpose
# This principle helps us to create classes that are easier to understand, maintain and test
# It also helps us to avoid code duplication and to create more reusable components
# It makes our code straight forrwad as classes and members do not have any hidden implememtation or functionality that is not related to 
# the purpose or the name of the class or members


# Bad example

class Account(object):
    def Add(self):
        pass

    def Update(self):
        pass

    def Delete(self):
        pass
    
    def Get(self):
        pass

    def Deposit(self, amount: float):
        pass

        # Deposit method is a problem here, breaking SRP because this class should only hold operations/functionality responsible for Account and not the
        # Transactions like Deposit or Withdraw


# Good example

class Account(object):
    def Add():
        pass

    def Update():
        pass

    def Delete():
        pass
    
    def Get():
        pass

class Transaction(object):
    def __init__(self, account: Account):
        self.account_to_perform_transaction_on = account

    def Deposit(self, amount: float):
        self.account_to_perform_transaction_on.amount += amount
        return "Amount deposited successfully"
    
    def Withdraw(self, amount: float):
        self.account_to_perform_transaction_on.amount -= amount
        return "Amount withdrawn successfully"
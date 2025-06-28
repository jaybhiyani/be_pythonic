# https://medium.com/@endlichfelipe/implementing-the-observer-design-pattern-in-python-e1201e32d1f1
# Observer Pattern Implementation in Python with Classes and Decorators

from abc import ABC, abstractmethod
from dataclasses import dataclass, field

class Observer(ABC):
    @abstractmethod
    def update(self, message: str) -> None:
        pass

@dataclass
class ConcreteObserver(Observer):
    name: str

    def update(self, value: str):
        print(f"{self.name} received {value}")

@dataclass
class Subject():
    obserbers: list[Observer] = field(default_factory=list)

    def attach(self, observer: Observer) -> None:
        self.obserbers.append(observer)

    def detach(self, observer: Observer) -> None:
        self.obserbers.remove(observer)

    def notify(self, value) -> None:
        for observer in self.obserbers:
            observer.update(value)

class WeatherStation(Subject):
    temperature: float = 0.0

    def set_temperature(self, temperature: float) -> None:
        self.temperature = temperature
        self.notify(f"Temperature updated to {self.temperature}")

class WeatherDisplay(Observer):
    def update(self, value: str) -> None:
        print(f"Weather display updated with {value}")

def main():
    # subject = Subject()
    weatherStation = WeatherStation()
    weatherDisplay = WeatherDisplay()
    # observer1 = ConcreteObserver("Observer 1")
    # observer2 = ConcreteObserver("Observer 2")

    # subject.attach(observer1)
    # subject.attach(observer2)

    weatherStation.attach(weatherDisplay)
    weatherStation.set_temperature(25.0)

    # subject.notify("Hello, Observers!")
    # subject.detach(observer1)
    # subject.detach(observer2)
    # subject.notify("Goodbye, Observers")

main()



###############################################################################################################################################################


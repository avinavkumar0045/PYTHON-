from abc import ABC, abstractmethod

class Animal(ABC):#abstract class different from data hiding, here we also fix what to show and obviously what not to show
    @abstractmethod
    def make_sound(self):
        pass

class Lion(Animal):
    def make_sound(self):
        print("Bhago bhago sher aaya")

class Cow(Animal):
    def make_sound(self):
        print("Gai hamari mata hai")
lion = Lion()
lion.make_sound()

cow = Cow()
cow.make_sound()
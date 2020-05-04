#this module simulates returning menu information about specialty pizza ingredients on the product detail page.

from abc import ABCMeta, abstractmethod

class Pizza(metaclass=ABCMeta):
    def __init__(self):

        @abstractmethod
        def getToppings(self):
            pass
        
    def __str__(self):
       return "{}".format(self.__class__. __name__)

class FourCheese(Pizza):
    def getToppings(self):
        return "Mozzarella, Parmesan, Pecorino and Manchego"

class Vegetarian(Pizza):
    def getToppings(self):
        return "Red & Green Bell Peppers, Black Olives, Mushrooms and Onions"

class MeatLover(Pizza):
    def getToppings(self):
        return "Bacon, Beef, Ham, Pepperoni and Sausage"

class PizzaFactory(object):
    @classmethod
    def create(cls, name, *args):
        name = name.lower().strip()
        
        if name == 'cheese':
            return FourCheese(*args)
        elif name == 'veggie':
            return Vegetarian(*args)
        elif name == 'meaty':
            return MeatLover(*args)

def main():
    factory = PizzaFactory()
 
    cheesy = factory.create('cheese')
    print (cheesy, ':' , cheesy.getToppings())
     
    veggie = factory.create('veggie')
    print (veggie, ':' , veggie.getToppings())
    
    meaty = factory.create('meaty')
    print(meaty, ':' , meaty.getToppings())


main()
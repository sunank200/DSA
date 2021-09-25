from abc import ABCMeta, abstractmethod, abstractstaticmethod

"""
Imagine that you’re creating a furniture shop simulator. Your code consists
of classes that represent:

A family of related products, say: Chair + Sofa + CoffeeTable.

Several variants of this family. For example, products Chair + Sofa +
CoffeeTable are available in these variants: Modern, Victorian, ArtDeco.

Solution
The first thing the Abstract Factory pattern suggests is to explicitly declare
interfaces for each distinct product of the product family (e.g., chair, sofa
or coffee table). Then you can make all variants of products follow those
interfaces. For example, all chair variants can implement the Chair interface;
all coffee table variants can implement the CoffeeTable interface, and so on.

The next move is to declare the Abstract Factory—an interface with a list of
creation methods for all products that are part of the product family (for
example, createChair, createSofa and createCoffeeTable). These methods must
return abstract product types represented by the interfaces we extracted
previously: Chair, Sofa, CoffeeTable and so on.

Now, how about the product variants? For each variant of a product family, we
create a separate factory class based on the AbstractFactory interface. A
factory is a class that returns products of a particular kind. For example,
the ModernFurnitureFactory can only create ModernChair, ModernSofa and
ModernCoffeeTable objects.
"""

"""
Factory method pattern with multiple factory

https://sourcemaking.com/design_patterns/abstract_factory
"""


class IChair(metaclass=ABCMeta):
    """
    Abstract Chair
    """

    @abstractstaticmethod
    def has_legs(self):
        pass

    @abstractstaticmethod
    def sit_on(self):
        pass


class ISofa(metaclass=ABCMeta):
    """
    Abstract Sofa
    """

    @abstractstaticmethod
    def has_legs(self):
        pass

    @abstractstaticmethod
    def length(self):
        pass

    @abstractstaticmethod
    def sit_on(self):
        pass


class ITable(metaclass=ABCMeta):
    """
    Abstract Table
    """

    @abstractstaticmethod
    def has_legs():
        pass

    @abstractstaticmethod
    def sit_on(self):
        pass


class ModernChair(IChair):
    """
    Concrete Chair (ModernChair)
    """

    def __init__(self):
        self.info = "Modern Chair"

    def has_legs(self):
        return 4

    def sit_on(self):
        return True


class ModernSofa(ISofa):
    """
    Concrete Sofa
    """

    def __init__(self):
        self.info = "Modern Sofa"

    def has_legs(self):
        return 6

    def length(self):
        return 30

    def sit_on(self):
        return True


class ModernTable(ITable):
    """ "
    Concrete Table
    """

    def __init__(self):
        self.info = "Modern Table"

    def has_legs(self):
        return 5

    def sit_on(self):
        return False


class IFurnitureFactory(metaclass=ABCMeta):
    """
    Abstract Furniture factory
    """

    @abstractmethod
    def create_chair(self):
        pass

    @abstractmethod
    def create_table(self):
        pass

    @abstractmethod
    def create_sofa(self):
        pass


class ModernFactory(IFurnitureFactory):
    """
    Concrete Factory
    """

    def create_chair(self):
        return ModernChair()

    def create_sofa(self):
        return ModernSofa()

    def create_table(self):
        return ModernTable()


if __name__ == "__main__":
    f = ModernFactory()
    modern_chair = f.create_chair()
    print(modern_chair.info)

    modern_table = f.create_table()
    print(modern_table.info)

    modern_sofa = f.create_sofa()
    print(modern_sofa.info)

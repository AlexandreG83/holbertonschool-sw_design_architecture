#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Beverage(ABC):
    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def description(self):
        pass


class Coffee(Beverage):
    def cost(self):
        return 50

    def description(self):
        return "Coffee"


class BeverageDecorator(Beverage):
    def __init__(self, inner):
        self._inner = inner


class MilkDecorator(BeverageDecorator):
    def cost(self):
        return self._inner.cost() + 10

    def description(self):
        return self._inner.description() + " + milk"


class SugarDecorator(BeverageDecorator):
    def cost(self):
        return self._inner.cost() + 5

    def description(self):
        return self._inner.description() + " + sugar"


class CaramelDecorator(BeverageDecorator):
    def cost(self):
        return self._inner.cost() + 15

    def description(self):
        return self._inner.description() + " + caramel"


def main():
    coffee_with_milk = MilkDecorator(Coffee())
    print(
        coffee_with_milk.description(),
        coffee_with_milk.cost()
    )

    coffee_with_sugar_and_milk = MilkDecorator(
        SugarDecorator(Coffee())
    )
    print(
        coffee_with_sugar_and_milk.description(),
        coffee_with_sugar_and_milk.cost()
    )

    coffee_with_all = CaramelDecorator(
        MilkDecorator(
            SugarDecorator(Coffee())
        )
    )
    print(
        coffee_with_all.description(),
        coffee_with_all.cost()
    )


if __name__ == "__main__":
    main()
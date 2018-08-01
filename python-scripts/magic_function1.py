__author__ = 'stevenlee'

class Money:

    currency_rates = {
        '$': 1,
        '€': 0.88,
    }

    def __init__(self, symbol, amount):
        self.symbol = symbol
        self.amount = amount

    def __repr__(self):
        return '%s%.2f' % (self.symbol, self.amount)

    def convert(self, other):
        """ Convert other amount to our currency """
        new_amount = (
            other.amount / self.currency_rates[other.symbol]
            * self.currency_rates[self.symbol])

        return Money(self.symbol, new_amount)

    def __add__(self, other):
        """ Add 2 Money instances using '+' """
        new_amount = self.amount + self.convert(other).amount
        return Money(self.symbol, new_amount)


if __name__ == "__main__":
    soda_cost = Money('$', 5.25)
    print("soda_cost is:", soda_cost)

    pizza_cost = Money('€', 7.99)
    print("pizza_cost is:", pizza_cost)

    print("soda_cost + pizza_cost is:",soda_cost + pizza_cost)
    print("pizza_cost + soda_cost is:", pizza_cost + soda_cost)
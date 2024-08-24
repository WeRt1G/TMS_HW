class Pizza:
    def __init__(
        self,
        size,
        cheese=False,
        pepperoni=False,
        mushrooms=False,
        onions=False,
        bacon=False,
    ):
        self.size = size
        self.cheese = cheese
        self.pepperoni = pepperoni
        self.mushrooms = mushrooms
        self.onions = onions
        self.bacon = bacon

    def __str__(self):
        toppings = []
        if self.cheese:
            toppings.append("cheese")
        if self.pepperoni:
            toppings.append("pepperoni")
        if self.mushrooms:
            toppings.append("mushrooms")
        if self.onions:
            toppings.append("onions")
        if self.bacon:
            toppings.append("bacon")

        return f"Pizza(size={self.size}, toppings={', '.join(toppings)})"


class PizzaBuilder:
    def __init__(self):
        self.size = None
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False
        self.onions = False
        self.bacon = False

    def set_size(self, size):
        self.size = size
        return self

    def add_cheese(self):
        self.cheese = True
        return self

    def add_pepperoni(self):
        self.pepperoni = True
        return self

    def add_mushrooms(self):
        self.mushrooms = True
        return self

    def add_onions(self):
        self.onions = True
        return self

    def add_bacon(self):
        self.bacon = True
        return self

    def build(self):
        return Pizza(
            self.size,
            self.cheese,
            self.pepperoni,
            self.mushrooms,
            self.onions,
            self.bacon,
        )


class PizzaDirector:
    def __init__(self, builder):
        self.builder = builder

    def make_pizza(
        self,
        size,
        with_cheese=True,
        with_pepperoni=False,
        with_mushrooms=False,
        with_onions=False,
        with_bacon=False,
    ):
        self.builder.set_size(size)

        if with_cheese:
            self.builder.add_cheese()
        if with_pepperoni:
            self.builder.add_pepperoni()
        if with_mushrooms:
            self.builder.add_mushrooms()
        if with_onions:
            self.builder.add_onions()
        if with_bacon:
            self.builder.add_bacon()

        return self.builder.build()


builder = PizzaBuilder()

director = PizzaDirector(builder)

pizza = director.make_pizza(
    size="large",
    with_cheese=True,
    with_pepperoni=True,
    with_mushrooms=True,
)

print(pizza)

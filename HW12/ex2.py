class PchelaSlon:
    def __init__(self, pchela, slon):
        self.pchela = pchela
        self.slon = slon

    def fly(self):
        return self.pchela >= self.slon

    def trumpet(self):
        if self.pchela <= self.slon:
            return "tu-tu-doo-doo"
        else:
            return "wzzzz"

    def eat(self, meal, value):
        if meal == "nectar":
            self.pchela += value
            self.slon -= value
        elif meal == "grass":
            self.pchela -= value
            self.slon += value
        else:
            raise ValueError("meal must be 'nectar' or 'grass'")

        self.pchela = min(max(self.pchela, 0), 100)
        self.slon = min(max(self.slon, 0), 100)


pchela_slon_1 = PchelaSlon(20, 10)
pchela_slon_2 = PchelaSlon(10, 20)
pchela_slon_3 = PchelaSlon(50, 50)

print(pchela_slon_1.fly())
print(pchela_slon_1.trumpet())
print(pchela_slon_2.fly())
print(pchela_slon_2.trumpet())

pchela_slon_3.eat("grass", 30)
print(pchela_slon_3.pchela)
print(pchela_slon_3.slon)

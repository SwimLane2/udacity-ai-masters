class Customer:
    def __init__(self, first_name, last_name, tier=("free", 0)):
        self.first_name = first_name
        self.last_name = last_name
        self.tier = tier

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    def can_access(self, song):
        customer_tier = self.tier[0]

        if customer_tier == "premium":
            return True

        return song["tier"] == "free"

    def bill_for(self, months):
        return months * self.tier[1]

    @classmethod
    def premium(cls, first_name, last_name):
        return cls(first_name, last_name, ("premium", 10))


if __name__ == "__main__":
    marco = Customer("Marco", "Polo")
    print(marco.name)
    print(marco.can_access({"tier": "free", "title": "1812 Overture"}))
    print(marco.can_access({"tier": "premium", "title": "William Tell Overture"}))

    victoria = Customer.premium("Alexandrina", "Victoria")
    print(victoria.can_access({"tier": "free", "title": "1812 Overture"}))
    print(victoria.can_access({"tier": "premium", "title": "William Tell Overture"}))
    print(victoria.bill_for(5))
    print(victoria.name)

class Refrigerator:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def compute_discount(self):
        if self.price <= 25000:
            discount = 2000
        elif self.price <= 50000:
            discount = 5000
        else:
            discount = 10000
        return discount

    def display_details(self):
        discount = self.compute_discount()
        amount_after_discount = self.price - discount
        print("Customer Name:", self.name)
        print("Discount:", discount)
        print("Amount to be paid after discount:", amount_after_discount)


# Creating an object of the class and calling the member methods
customer_name = input("Enter customer name: ")
price = float(input("Enter price of the refrigerator: "))

refrigerator = Refrigerator(customer_name, price)
refrigerator.display_details()

class Restaurant:
    def __init__(self):
        self.menu_items = []
        self.booked_tables = []
        self.customer_orders = []

    def add_item_to_menu(self, item):
        self.menu_items.append(item)
        print(f"Added '{item}' to the menu.")

    def book_table(self, table_number):
        if table_number not in self.booked_tables:
            self.booked_tables.append(table_number)
            print(f"Table {table_number} is now reserved.")
        else:
            print(f"Table {table_number} is already booked.")

    def customer_order(self, order):
        self.customer_orders.append(order)
        print(f"Order '{order}' has been placed.")

    def print_menu(self):
        print("Menu:")
        for item in self.menu_items:
            print(f"- {item}")

    def print_table_reservations(self):
        print("Table Reservations:")
        for table_number in self.booked_tables:
            print(f"- Table {table_number}")

    def print_customer_orders(self):
        print("Customer Orders:")
        for order in self.customer_orders:
            print(f"- {order}")

# Create an instance of the Restaurant class
restaurant = Restaurant()

# Add items to the menu
restaurant.add_item_to_menu("Pizza")
restaurant.add_item_to_menu("Burger")
restaurant.add_item_to_menu("Salad")

# Make table reservations
restaurant.book_table(1)
restaurant.book_table(3)
restaurant.book_table(2)
restaurant.book_table(1)  # Trying to book an already booked table

# Take customer orders
restaurant.customer_order("Pizza")
restaurant.customer_order("Burger")
restaurant.customer_order("Salad")

# Print the menu
restaurant.print_menu()
# Print table reservations
restaurant.print_table_reservations()
# Print customer orders
restaurant.print_customer_orders()

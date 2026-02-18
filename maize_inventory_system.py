# Maize Bag Inventory Tracking System

class MaizeInventory:
    def __init__(self):
        self.total_weight = 0  # in kg
        self.history = []

    def add_bags(self, bags):
        """
        Adds maize bags to the inventory.
        :param bags: Number of 90kg bags to be added.
        """
        weight_added = bags * 90
        self.total_weight += weight_added
        self.history.append(("Added", weight_added, self.total_weight))
        print(f"Added {weight_added} kg. Total inventory: {self.total_weight} kg.")

    def deduct_bags(self, bags):
        """
        Deducts maize bags from the inventory.
        :param bags: Number of 90kg bags to be deducted.
        """
        weight_deducted = bags * 90
        if weight_deducted > self.total_weight:
            print("Error: Not enough inventory to deduct that many bags.")
        else:
            self.total_weight -= weight_deducted
            self.history.append(("Deducted", weight_deducted, self.total_weight))
            print(f"Deducted {weight_deducted} kg. Total inventory: {self.total_weight} kg.")

    def show_inventory(self):
        """
        Displays the current inventory.
        """
        print(f"Current inventory: {self.total_weight} kg.")

    def show_history(self):
        """
        Displays the history of inventory changes.
        """
        for action in self.history:
            print(f"{action[0]}: {action[1]} kg, Total: {action[2]} kg")

# Example usage
if __name__ == '__main__':
    inventory = MaizeInventory()
    inventory.add_bags(10)  # Adding 10 bags
    inventory.deduct_bags(3)  # Deducting 3 bags
    inventory.show_inventory()  # Show current inventory
    inventory.show_history()  # Show history of transactions
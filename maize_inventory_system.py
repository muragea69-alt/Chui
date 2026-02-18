class MaizeInventorySystem:
    def __init__(self, total_weight=90):
        self.total_weight = total_weight  # weight in kgs
        self.remaining_weight = total_weight

    def deduct_weight(self, weight):
        if weight < 0:
            print("Cannot deduct a negative weight.")
            return
        if weight > self.remaining_weight:
            print("Cannot deduct more weight than remaining.")
            return
        self.remaining_weight -= weight
        print(f'Deducted {weight} kgs. Remaining: {self.remaining_weight} kgs')

    def restock(self):
        self.remaining_weight = self.total_weight
        print(f'Restocked. Total weight: {self.total_weight} kgs')

# Example usage:
if __name__ == '__main__':
    maize_system = MaizeInventorySystem()
    maize_system.deduct_weight(10)  # Deduct 10 kgs
    maize_system.deduct_weight(5)   # Deduct 5 kgs
    maize_system.restock()           # Restock to 90 kgs

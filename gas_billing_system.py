# Gas Billing System

class Company:
    def __init__(self, name, address):
        self.name = name
        self.address = address

class Cylinder:
    def __init__(self, weight, company):
        self.weight = weight
        self.company = company

class Buyer:
    def __init__(self, name, location):
        self.name = name
        self.location = location

class Transaction:
    def __init__(self, buyer, cylinder, amount):
        self.buyer = buyer
        self.cylinder = cylinder
        self.amount = amount

class SafaricomMPesa:
    @staticmethod
    def process_payment(amount, phone_number):
        # Integrate with Safaricom M-Pesa API to process payment
        return True  # Assuming payment is successful

class BillingSystem:
    def __init__(self):
        self.transactions = []

    def generate_bill(self, transaction):
        # Logic to generate bill
        return f'Bill generated for {transaction.buyer.name} for amount {transaction.amount}'

    def create_invoice(self, transaction):
        # Logic to create an invoice
        return f'Invoice created for {transaction.buyer.name} for amount {transaction.amount}'

    def process_transaction(self, buyer, cylinder, amount, phone_number):
        transaction = Transaction(buyer, cylinder, amount)
        if SafaricomMPesa.process_payment(amount, phone_number):
            self.transactions.append(transaction)
            return self.generate_bill(transaction), self.create_invoice(transaction)
        return 'Payment failed',''
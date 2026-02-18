import json
from datetime import datetime
from enum import Enum

class PaymentMethod(Enum):
    SAFARICOM_MPESA = "safaricom_mpesa"
    CASH = "cash"
    CARD = "card"

class Company:
    """Represents a gas distribution company"""
    def __init__(self, company_id, name, location, contact_number):
        self.company_id = company_id
        self.name = name
        self.location = location
        self.contact_number = contact_number

class Cylinder:
    """Represents a gas cylinder with weight"""
    def __init__(self, cylinder_id, company_id, weight, price_per_kg):
        self.cylinder_id = cylinder_id
        self.company_id = company_id
        self.weight = weight
        self.price_per_kg = price_per_kg

    def calculate_cost(self):
        return self.weight * self.price_per_kg

class Buyer:
    """Represents a gas buyer"""
    def __init__(self, buyer_id, name, location, phone_number):
        self.buyer_id = buyer_id
        self.name = name
        self.location = location
        self.phone_number = phone_number

class Transaction:
    """Represents a billing transaction"""
    def __init__(self, transaction_id, buyer, cylinder, company, quantity=1):
        self.transaction_id = transaction_id
        self.buyer = buyer
        self.cylinder = cylinder
        self.company = company
        self.quantity = quantity
        self.total_amount = cylinder.calculate_cost() * quantity
        self.timestamp = datetime.now().isoformat()
        self.payment_method = None
        self.payment_status = "pending"
        self.mpesa_reference = None

    def to_dict(self):
        return {
            "transaction_id": self.transaction_id,
            "buyer_name": self.buyer.name,
            "buyer_location": self.buyer.location,
            "buyer_phone": self.buyer.phone_number,
            "cylinder_weight": self.cylinder.weight,
            "quantity": self.quantity,
            "total_amount": self.total_amount,
            "company": self.company.name,
            "timestamp": self.timestamp,
            "payment_method": self.payment_method,
            "payment_status": self.payment_status,
            "mpesa_reference": self.mpesa_reference
        }

class SafaricomMPesa:
    """Handles Safaricom M-Pesa payment integration"""
    def __init__(self, shortcode, passkey, api_key):
        self.shortcode = shortcode
        self.passkey = passkey
        self.api_key = api_key

    def initiate_stk_push(self, phone_number, amount, transaction_id):
        """Initiate M-Pesa STK Push"""
        print(f"[M-PESA] Initiating STK Push")
        print(f"  Phone: {phone_number}")
        print(f"  Amount: KES {amount}")
        print(f"  Transaction ID: {transaction_id}")
        return {
            "status": "initiated",
            "phone": phone_number,
            "amount": amount,
            "transaction_id": transaction_id
        }

    def verify_payment(self, mpesa_reference):
        """Verify M-Pesa payment"""
        print(f"[M-PESA] Verifying payment: {mpesa_reference}")
        return True

class BillingSystem:
    """Main billing system for gas distribution"""
    def __init__(self, company, mpesa_config=None):
        self.company = company
        self.mpesa = None
        if mpesa_config:
            self.mpesa = SafaricomMPesa(
                mpesa_config.get('shortcode'),
                mpesa_config.get('passkey'),
                mpesa_config.get('api_key')
            )
        self.transactions = []
        self.transaction_counter = 0

    def create_transaction(self, buyer, cylinder, quantity=1):
        """Create a new billing transaction"""
        self.transaction_counter += 1
        transaction_id = f"TXN-{self.company.company_id}-{self.transaction_counter:05d}"
        transaction = Transaction(transaction_id, buyer, cylinder, self.company, quantity)
        self.transactions.append(transaction)
        return transaction

    def process_safaricom_payment(self, transaction):
        """Process payment via Safaricom M-Pesa"""
        if not self.mpesa:
            raise Exception("M-Pesa not configured")
        
        transaction.payment_method = PaymentMethod.SAFARICOM_MPESA.value
        result = self.mpesa.initiate_stk_push(
            transaction.buyer.phone_number,
            transaction.total_amount,
            transaction.transaction_id
        )
        return result

    def confirm_payment(self, transaction, mpesa_reference):
        """Confirm M-Pesa payment"""
        if self.mpesa:
            if self.mpesa.verify_payment(mpesa_reference):
                transaction.mpesa_reference = mpesa_reference
                transaction.payment_status = "completed"
                print(f"[SUCCESS] Payment confirmed for {transaction.transaction_id}")
                return True
        return False

    def generate_bill(self, transaction):
        """Generate a bill for the transaction"""
        bill = f"""
╔══════════════════════════════════════════════╗
║           GAS DISTRIBUTION BILL              ║
╚══════════════════════════════════════════════╝

COMPANY DETAILS:
  Name: {transaction.company.name}
  Location: {transaction.company.location}
  Contact: {transaction.company.contact_number}

TRANSACTION DETAILS:
  ID: {transaction.transaction_id}
  Date: {transaction.timestamp}

BUYER INFORMATION:
  Name: {transaction.buyer.name}
  Location: {transaction.buyer.location}
  Phone: {transaction.buyer.phone_number}

CYLINDER DETAILS:
  Weight: {transaction.cylinder.weight} kg
  Price per kg: KES {transaction.cylinder.price_per_kg}
  Quantity: {transaction.quantity}

BILLING SUMMARY:
  Unit Cost: KES {transaction.cylinder.calculate_cost()}
  Total Amount: KES {transaction.total_amount}
  Payment Method: {transaction.payment_method or 'Not specified'}
  Payment Status: {transaction.payment_status}
  M-Pesa Reference: {transaction.mpesa_reference or 'N/A'}

╚══════════════════════════════════════════════╝
        """
        return bill

    def get_transaction_history(self):
        """Get all transactions"""
        return [t.to_dict() for t in self.transactions]

    def export_to_json(self, filename='transactions.json'):
        """Export all transactions to JSON"""
        with open(filename, 'w') as f:
            json.dump(self.get_transaction_history(), f, indent=2)
        print(f"Transactions exported to {filename}")


# Example usage
if __name__ == "__main__":
    # Create company
    company = Company(
        company_id="GAS001",
        name="Kenya Gas Distributors Ltd",
        location="Nairobi, Kenya",
        contact_number="+254712345678"
    )

    # Create buyer
    buyer = Buyer(
        buyer_id="BUYER001",
        name="John Kipchoge",
        location="Westlands, Nairobi",
        phone_number="+254798765432"
    )

    # Create cylinder
    cylinder = Cylinder(
        cylinder_id="CYL001",
        company_id="GAS001",
        weight=13,
        price_per_kg=2500
    )

    # M-Pesa configuration
    mpesa_config = {
        'shortcode': '174379',
        'passkey': 'bfb279f9aa9bdbcf158e97dd1a503b6e323a0540',
        'api_key': 'your_api_key_here'
    }

    # Initialize billing system
    billing_system = BillingSystem(company, mpesa_config)

    # Create transaction
    transaction = billing_system.create_transaction(buyer, cylinder, quantity=1)
    print(f"✓ Transaction created: {transaction.transaction_id}")
    print(f"✓ Amount due: KES {transaction.total_amount}\n")

    # Process M-Pesa payment
    billing_system.process_safaricom_payment(transaction)

    # Confirm payment
    billing_system.confirm_payment(transaction, "MPE20260218ABC123")

    # Generate bill
    bill = billing_system.generate_bill(transaction)
    print(bill)

    # Export transactions
    billing_system.export_to_json()
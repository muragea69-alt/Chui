class GasBillingSystem:
    def __init__(self):
        self.prices = {
            '6kg': 1100,
            '13kg': 2300
        }
        self.payment_options = [
            'Safaricom M-Pesa',
            'Equity Bank Lipa na M-Pesa (Account Number: 0700875728)'
        ]

    def get_price(self, cylinder_size):
        return self.prices.get(cylinder_size, 'Invalid cylinder size')

    def process_payment(self, payment_option, amount):
        if payment_option in self.payment_options:
            return f'Payment of {amount} KES processed via {payment_option}'
        return 'Invalid payment option'

    def generate_bill(self, cylinder_size, payment_option):
        price = self.get_price(cylinder_size)
        if isinstance(price, int):
            # Assuming all payments are successful for simplicity
            self.process_payment(payment_option, price)
            return f'Bill generated: {price} KES for {cylinder_size} cylinder.'
        else:
            return price

# Example usage
if __name__ == '__main__':
    billing_system = GasBillingSystem()
    print(billing_system.generate_bill('6kg', 'Safaricom M-Pesa'))
    print(billing_system.generate_bill('13kg', 'Equity Bank Lipa na M-Pesa'))

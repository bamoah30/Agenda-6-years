class BankAccount:
    bank_name = "GCB"

    def __init__(self, balance, time):
        self.balance = balance
        self.time = time

    def calculate_balance(self):
        rate = 0.07
        amount = (self.balance *rate *self.time) + self.balance
        print(f'Your {BankAccount.bank_name} acount has {amount} in it. Thank you!!!')


my_bank = BankAccount(20000,3)

print(my_bank.calculate_balance())

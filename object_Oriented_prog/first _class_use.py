import time
class Bank:
    bank_name = "GCB"

    def display_bank(self):
        self.balance = 2000
        self.transaction_date = time.ctime()
        return (f'As at {self.transaction_date} your balance is {self.balance}')

    def __str__(self):
        return (f"You are using {self.bank_name} and you balance is : {self.display_bank()}")
    
# Creating an object

my_bank = Bank()
print(my_bank)

print(my_bank.display_bank())
# Python inheritance Bank_Account program which performs the following operations: make a deposit, withdraw funds, and display the account information for the created bank account instance.

class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount
        return "The new balance is: " + str(self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return "You have withdrawn " + str(amount) + ", your current balance is " + str(self.balance)

    def check_balance(self):
        return "The current balance is: " + str(self.balance)

    def customer_details(self):
        print("Account number:", self.account_number)
        print("Name:", self.customer_name)
        print("Balance:", self.balance)
        print("Date of opening:", self.date_of_opening)


# Example usage:
customer = BankAccount(1234, 1000, "9/7/2023", "John")
customer.customer_details()
print(customer.deposit(200))
print(customer.withdraw(200))
print(customer.check_balance())

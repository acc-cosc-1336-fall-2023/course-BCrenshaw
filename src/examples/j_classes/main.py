import bank_account#, atm, menu#, random as r

"""
account = bank_account.BankAccount(-1)
my_atm = atm.ATM(account)
menu.run_menu(my_atm)
"""

list_accounts = []

account = bank_account.BankAccount(50)
list_accounts.append(account)

account = bank_account.BankAccount(50)
list_accounts.append(account)

account = bank_account.BankAccount(50)
list_accounts.append(account)

for account in list_accounts:
    print(account)
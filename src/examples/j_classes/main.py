import bank_account, atm, menu, random as r

account = bank_account.BankAccount(-1)
my_atm = atm.ATM(account)

menu.run_menu(my_atm)

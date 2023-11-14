import random

class BankAccount:
	__balance = 0 #hide it from other classes

	def __init__(self, balance): #constructor -- helps us initialize class/data variable
		if balance >= 0:
			self.__balance = balance
		else:
			self.__get_balance_from_db() #private function inaccessible from outside class.

	def get_balance(self): #other classes can see get_balance
		return self.__balance

	def deposit(self, amount):

		if amount > 0:
			self.__balance += amount

	def withdraw(self, amount):

		if 0 < amount <= self.__balance:
			self.__balance -= amount
	
	def __get_balance_from_db(self):
		self.__balance = random.randint(0,10000)

	def __str__(self):
		#return str(self.__balance)
		return f'The balance is ${self.__balance:,.2f}'
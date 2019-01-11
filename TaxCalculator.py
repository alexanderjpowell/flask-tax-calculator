
class TaxCalculator(object):

	def __init__(self, income, filing_status, year):
		self.income = income
		self.filing_status = filing_status
		self.year = year

	def calculate(self):
		return 5

if __name__ == "__main__":

	a = TaxCalculator(80000, 'single', '2018')
	print(a.calculate())
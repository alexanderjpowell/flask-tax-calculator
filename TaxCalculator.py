
class TaxCalculator(object):

	def __init__(self, income, filing_status, year):
		self.income = income
		self.filing_status = filing_status
		self.year = year

	def calculate(self):
		if self.year == "2017":
			if self.filing_status == "single":
				if self.income <= 9325:
					return 0.1 * self.income
				elif self.income <= 37950:
					return 932.5 + 0.15 * (self.income - 9325)
				elif self.income <= 91900:
					return 5226.25 + 0.25 * (self.income - 37950)
				elif self.income <= 191650:
					return 18713.75 + 0.28 * (self.income - 91900)
				elif self.income <= 416700:
					return 46634.75 + 0.33 * (self.income - 191650)
				elif self.income <= 418400:
					return 120910.25 + 0.35 * (self.income - 416700)
				elif self.income > 418400:
					return 121505.25 + 0.396 * (self.income - 418400)
			elif self.filing_status == "married_filing_jointly":
				if self.income <= 18650:
					return 0.1 * self.income
				elif self.income <= 75900:
					return 1865 + 0.15 * (self.income - 18650)
				elif self.income <= 153100:
					return 10452.5 + 0.25 * (self.income - 75900)
				elif self.income <= 233350:
					return 29752.5 + 0.28 * (self.income - 153100)
				elif self.income <= 416700:
					return 52222.5 + 0.33 * (self.income - 233350)
				elif self.income <= 470700:
					return 112728 + 0.35 * (self.income - 416700)
				elif self.income > 470700:
					return 131628 + 0.396 * (self.income - 470700)
			elif self.filing_status == "married_filing_separately":
				if self.income <= 9325:
					return 0.1 * self.income
				elif self.income <= 37950:
					return 932.5 + 0.15 * (self.income - 9325)
				elif self.income <= 76550:
					return 5226.25 + 0.25 * (self.income - 37950)
				elif self.income <= 116675:
					return 14876.25 + 0.28 * (self.income - 76550)
				elif self.income <= 208350:
					return 26111.25 + 0.33 * (self.income - 116675)
				elif self.income <= 235350:
					return 56364 + 0.35 * (self.income - 208350)
				elif self.income > 235350:
					return 65814 + 0.396 * (self.income - 235350)
			elif self.filing_status == "head_of_household":
				if self.income <= 13350:
					return 0.1 * self.income
				elif self.income <= 50800:
					return 1335 + 0.15 * (self.income - 13350)
				elif self.income <= 131200:
					return 6952.5 + 0.25 * (self.income - 50800)
				elif self.income <= 212500:
					return 27052.5 + 0.28 * (self.income - 131200)
				elif self.income <= 416700:
					return 49816.5 + 0.33 * (self.income - 212500)
				elif self.income <= 444550:
					return 117202.5 + 0.35 * (self.income - 416700)
				elif self.income > 444550:
					return 126950 + 0.396 * (self.income - 444550)
		elif self.year == "2018":
			if self.filing_status == "single":
				if self.income <= 9525:
					return 0.1 * self.income
				elif self.income <= 38700:
					return 952.5 + 0.12 * (self.income - 9525)
				elif self.income <= 82500:
					return 4453.5 + 0.22 * (self.income - 38700)
				elif self.income <= 157500:
					return 14089.5 + 0.24 * (self.income - 82500)
				elif self.income <= 200000:
					return 32089.5 + 0.32 * (self.income - 157500)
				elif self.income <= 500000:
					return 45689.5 + 0.35 * (self.income - 200000)
				elif self.income > 500000:
					return 150689.5 + 0.37 * (self.income - 500000)
			elif self.filing_status == "married_filing_jointly":
				if self.income <= 19050:
					return 0.1 * self.income
				elif self.income <= 77400:
					return 1905 + 0.12 * (self.income - 19050)
				elif self.income <= 165000:
					return 8907 + 0.22 * (self.income - 77400)
				elif self.income <= 315000:
					return 28179 + 0.24 * (self.income - 165000)
				elif self.income <= 400000:
					return 64179 + 0.32 * (self.income - 315000)
				elif self.income <= 600000:
					return 91379 + 0.35 * (self.income - 400000)
				elif self.income > 600000:
					return 161379 + 0.37 * (self.income - 600000)
			elif self.filing_status == "married_filing_separately":
				if self.income <= 9525:
					return 0.1 * self.income
				elif self.income <= 38700:
					return 952.5 + 0.12 * (self.income - 9525)
				elif self.income <= 82500:
					return 4453.5 + 0.22 * (self.income - 38700)
				elif self.income <= 157500:
					return 14089.5 + 0.24 * (self.income - 82500)
				elif self.income <= 200000:
					return 32089.5 + 0.32 * (self.income - 157500)
				elif self.income <= 300000:
					return 45689.5 + 0.35 * (self.income - 200000)
				elif self.income > 300000:
					return 80689.5 + 0.37 * (self.income - 300000)
			elif self.filing_status == "head_of_household":
				if self.income <= 13600:
					return 0.1 * self.income
				elif self.income <= 51800:
					return 1360 + 0.12 * (self.income - 13600)
				elif self.income <= 82500:
					return 5944 + 0.22 * (self.income - 51800)
				elif self.income <= 157500:
					return 12698 + 0.24 * (self.income - 82500)
				elif self.income <= 200000:
					return 30698 + 0.32 * (self.income - 157500)
				elif self.income <= 500000:
					return 44298 + 0.35 * (self.income - 200000)
				elif self.income > 500000:
					return 149298 + 0.37 * (self.income - 500000)


if __name__ == "__main__":

	a = TaxCalculator(68000, 'single', '2018')
	print(a.calculate())














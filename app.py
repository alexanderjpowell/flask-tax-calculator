from flask import Flask, render_template, request
from TaxCalculator import TaxCalculator

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():

	if request.method == 'POST':
		income = str(request.form.get("income"))
		
		filing_status = str(request.form.get("filing_status"))
		if filing_status == "option1":
			filing_status = "single"
		elif filing_status == "married_filing_jointly":
			filing_status = "married_filing_jointly"
		elif filing_status == "married_filing_separately":
			filing_status = "married_filing_separately"
		elif filing_status == "head_of_household":
			filing_status = "head_of_household"
		
		tax_year = str(request.form.get("tax_year"))
		if tax_year == "option1":
			tax_year = "2017"
		elif tax_year == "option2":
			tax_year = "2018"

		taxCalculator = TaxCalculator(float(income), filing_status, tax_year)
		#taxCalculator = TaxCalculator(68000, 'single', '2018')
		taxes = taxCalculator.getTaxesDue()
		#print "Taxes: " + str(taxes)
		taxes_string = str(taxes)

		#return "Submitted Form.  Income: $" + income + "\n" + "Filing Status: " + filing_status + "\n" + "Tax Year: " + tax_year
		return render_template("results.html", taxes_due=taxes_string)
	else:
		return render_template("index.html")

if __name__ == "__main__":
	app.run(host='0.0.0.0')
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():

	if request.method == 'POST':
		income = str(request.form.get("income"))
		filing_status = str(request.form.get("filing_status"))
		tax_year = str(request.form.get("tax_year"))

		#return "Submitted Form.  Income: $" + income + "\n" + "Filing Status: " + filing_status + "\n" + "Tax Year: " + tax_year
		return render_template("results.html")
	else:
		return render_template("index.html")

if __name__ == "__main__":
	app.run(debug=True)
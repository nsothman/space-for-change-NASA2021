from flask import Flask, render_template
import csv
app = Flask(__name__)

injusticeResults = []
with open("./Datasets/injustice.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
    for row in reader: # each row is a list
        injusticeResults.append(row)

countries = []
with open("./Datasets/countries.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
    for row in reader: # each row is a list
        countries.append(row)


@app.route("/", methods = ["GET", "POST"])
def home():
    return render_template("map.html", injusticeResults = injusticeResults, countries = countries)

if __name__ == "__main__":
    app.run()

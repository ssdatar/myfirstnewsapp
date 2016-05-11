import csv
from flask import Flask, abort, render_template
from csv import DictReader

app = Flask(__name__)

def get_csv():
	csv_path = './static/art.csv'
	
	with open(csv_path, 'r') as csv_in:
		datarows = list(DictReader(csv_in))

	return datarows

@app.route("/")
def index():
	template = 'index.html'
	data = get_csv()
	return render_template(template, data=data)

@app.route('/<row_id>/')
def detail(row_id):
  template = 'view.html'
  datarows = get_csv()
  for row in datarows:
    if row['_id'] == row_id:
      return render_template(template, obj=row)
  abort(404)

if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)
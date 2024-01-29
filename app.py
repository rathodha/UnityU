from flask, import Flask, render_template
from importData import read_csv_file
import data.js


app = Flask(__name__)

@app.route(welcome.html)

def index():

    data = read_csv_file(data.js)

    return render_template('welcome.html')



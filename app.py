from flask import Flask, render_template
import pymongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/_____")



@app.route('/')
def home():
    mars_info = 
    return render_template('index.html', mars_info=mars_info)


@app.route('/scrape')
def index():
    mars_data = scrape_mars.scrape
    




if __name__ == "__main__":
    app.run(debug=True)

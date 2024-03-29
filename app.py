from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

# Create an instance of Flask (91)
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection (92)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#define the route for the HTML page (94)
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

#set up our scraping route (95)
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return redirect('/', code=302)

#tell Flask to run (99)
if __name__ == "__main__":
    app.run(debug=True)
    

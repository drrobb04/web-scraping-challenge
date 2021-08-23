#dependencies
import scrape_mars
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

# Create an instance of our Flask app.
app = Flask(__name__)

# Establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_scrape_db")

# Route to render index.html template using data from Mongo
@app.route("/")
def index():

    # Find one record of data from the mongo database
    mars_run = mongo.db.mars_run.find_one()

    # Return template and data
    return render_template("index.html", mars_run=mars_run)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    mars_run = mongo.db.mars_run
    mars_info = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    mars_run.update({}, mars_info, upsert=True)

    # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
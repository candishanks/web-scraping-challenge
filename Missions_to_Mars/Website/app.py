from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_final

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    mars_data = mongo.db.collection.find_one()

    # Return template and data
    return render_template("index.html", mars=mars_data)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    mars_data = scrape_final.scrape_info()

    mongo.db.collection.update({}, mars_data, upsert=True)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
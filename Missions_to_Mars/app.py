{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# import dependencies\n",
    "from flask import Flask, render_template, redirect\n",
    "from flask_pymongo import PyMongo\n",
    "import scrape_mars\n",
    "\n",
    "# Create an instance of Flask\n",
    "app = Flask(__name__)\n",
    "\n",
    "# Use PyMongo to establish Mongo connection\n",
    "mongo = PyMongo(app, uri=\"mongodb://localhost:27017/mars_app\")\n",
    "\n",
    "# create home route and define home function\n",
    "@app.route(\"/\")\n",
    "def home():\n",
    "    # Find one record of data from the mongo database\n",
    "    mars_info = mongo.db.mars_collection.find_one()\n",
    "\n",
    "    # Return template and data\n",
    "    return render_template(\"index.html\", mars_data=mars_info)\n",
    "\n",
    "# create scrape route \n",
    "@app.route(\"/scrape\")\n",
    "def scrape():\n",
    "    # run the scrape function\n",
    "    mars_data = scrape_mars.scrape()\n",
    "\n",
    "    # insert the mars data in to the collection\n",
    "    mongo.db.mars_collection.update({}, mars_data, upsert=True)\n",
    "\n",
    "    # go back to the home page\n",
    "    return redirect(\"/\")\n",
    "\n",
    "# run the app\n",
    "# if __name__ == \"__main__\":\n",
    "#     app.run(debug=True)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

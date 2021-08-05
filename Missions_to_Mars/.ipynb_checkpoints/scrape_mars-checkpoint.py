{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import Dependancies\n",
    "import pandas as pd\n",
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup as bs\n",
    "import  requests\n",
    "import pymongo\n",
    "from webdriver_manager.chrome import ChromeDriverManager"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def init_browser():\n",
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create Scrape Function\n",
    "def scrape():\n",
    "    browser = init_browser()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use Browser to open the URL\n",
    "url = 'https://redplanetscience.com/'\n",
    "\n",
    "# Open the URL\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Scrape Page Into Soup\n",
    "html = browser.html\n",
    "soup = bs(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Get the Latest News Title & Paragraph\n",
    "data = soup.find(\"div\", id=\"news\", class_=\"container\")\n",
    "news_title = data.find(\"div\", class_\"content_title\").a.text\n",
    "paragraph = data.find(\"div\", class_\"article_teaser_body\").text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Mars Space Images, get the Full Size Featured Image\n",
    "featured_image_url = 'https://spaceimages-mars.com/image/featured/mars1.jpg'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# use browser to open the url for image\n",
    "browser.visit(featured_image_url) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create HTML to Parse\n",
    "html = browser.html\n",
    "soup = bs(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#MARS FACTS"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Get the URL for Mar's Facts\n",
    "facts_url = 'https://galaxyfacts-mars.com/'\n",
    "\n",
    "# # Use Pandas to Parse the URL (read to html)\n",
    "table = pd.read_html(facts_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Convert the Data Table into a HTML table string\n",
    "facts_df = table[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Rename the Columns\n",
    "facts_df.columns = \"Description\", \"Mars\", \"Earth\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Reset the Index for the DataFrame\n",
    "facts_df.set_index(\"Description\", inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Convert the DataFrame into a HTML Table String\n",
    "facts_html = facts_df.to.html()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# MARS HEMISPHERE"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Get the URL & Open in Browser\n",
    "h_url = 'https://marshemispheres.com/'\n",
    "# # Use Browser to open the URL for the Image\n",
    "browser.visit(h_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create HTML\n",
    "html = browser.html\n",
    "soup = bs(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "data = soup.find_all(\"div\", class_=\"item\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Navigate the page to obtain high res Images for each Mar's Hemispheres (Image & Title)\n",
    "data = soup.find_all(\"div\", class_=\"item\")\n",
    "\n",
    "hemisphere_img_urls = []\n",
    "\n",
    "# # Loop through the image data to find title & url info\n",
    "for d in data:\n",
    "    \n",
    "    title = d.find(\"h3\").text\n",
    "    \n",
    "    img_url = d.a[\"href\"]\n",
    "    \n",
    "    url = \"https://marshemispheres.com/\" + img_url\n",
    "    \n",
    "# Use requests to get Full Image URL\n",
    "    response = requests.get(url)\n",
    "    \n",
    "# Create Soup Object\n",
    "    soup = bs(response.text, \"html.parser\")\n",
    "    \n",
    "# Find Full Image URL\n",
    "    new_url = soup.find(\"img\", class_=\"wide-image\")[\"src\"]\n",
    "    \n",
    "# Create Full Image URL\n",
    "    full_url = \"https://marshemispheres.com/\" + new_url\n",
    "    \n",
    "# Create a Dictionary & Append to a List (One Dict for each hemishpere)\n",
    "    hemisphere_img_urls.append({\"title\": title, \"img_url\": full_url})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Store the return value into a Python Dictionary\n",
    "    mars_data = {\n",
    "        \"news_title\": news_title,\n",
    "        \"paragraph\" : paragraph,\n",
    "        \"featured_image_url\": featured_image_url,\n",
    "        \"html_table\": facts_html,\n",
    "        \"hemisphere_img_urls\": hemisphere_img_urls\n",
    "    }"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Close the Browser\n",
    " browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Return the Results\n",
    " return mars_data"
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

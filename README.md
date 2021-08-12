
# Web Scraping Project - Mission to Mars

![image](https://user-images.githubusercontent.com/82673788/129237431-3edc9e33-6ef9-43f7-af6b-fc4805b83540.png)





_____________________________________________

For this project, I built a web application that scrapes various websites for data related to the Mission to Mars
and displays the information in a single HTML page.

____________________________________________

## Step 1 - Scraping

____________________________________________

I completed my initial scraping using Jupyter Notebook, BeautifulSoup, Pandas and Requests/Splinter

The Jupyter Notebook file is called mission_to_mars.ipynb and was used to complete all of my scraping
and analysis.

https://github.com/dschoen24/web-scraping-challenge/tree/main/Missions_to_Mars/mission_to_mars.ipynb


The following is the information of what was scraped and where I retrieved that information:

### NASA Mars News

- I scraped the Mars News Site (https://redplanetscience.com/) and collected the latest News Title and Paragraph Text.

- I assigned this information to variables that I would be able to reference later.

### JPL Mars Space Images - Featured Image

- I visited the url for the sites Featured Space Image (https://spaceimages-mars.com/)

- I used Splinter to navigate the site and find the image url for the current Featured Mars Image

- Once the Featured Mars Image url was found, I made sure to find the full size .jpg image 
  and assigned the url string to a variable called featured_image_url

- The complete url string for this image (featured_image_url) was saved to be able to reference later.

### Mars Facts

- I visited the Mars Facts webpage (https://galaxyfacts-mars.com/) and used Pandas to scrape the table
  containing facts about the planet i.e. Diameter, Mass, ect.

- I droped a column and a row containging information about Earth since I was only interested in Mars Information

- I then used Pandas to convert the data into an HTML table string to be able to reference on my HTML page

### Mars Hemispheres

- I visited the astrogeology site (https://marshemispheres.com/) to obtain high resolution images for each
  of the Mar's hemispheres.

- I searched the site to find each of the links to the hemispheres in order to save the full size image url
  for each hemisphere.

- I then saved the image urls for the full resolution hemisphere images and the hemisphere title
  containing the hemisphere namge

- I used a Python dictionary to store this data to be able to bring into my HTML page

- The Python dictionary was appended into a list containing the hemisphere title and image url for each
  of the Mar's hemispheres

______________________________________________________

## Step 2 - MondoDB and Flask Application

______________________________________________________






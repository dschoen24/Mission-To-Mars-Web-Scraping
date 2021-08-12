
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

The following is the information of what was scraped and where I retrieved that information:

### NASA Mars News

- I scraped the Mars News Site () and collected the latest News Title and Paragraph Text.

- I assigned this information to variables that I would be able to reference later.

### JPL Mars Space Images - Featured Image

- I visited the url for the sites Featured Space Image ()

- I used Splinter to navigate the site and find the image url for the current Featured Mars Image

- Once the Featured Mars Image url was found, I made sure to find the full size .jpg image 
  and assigned the url string to a variable called featured_image_url

- The complete url string for this image (featured_image_url) was saved to be able to reference later.

### Mars Facts






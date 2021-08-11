# Import Dependancies
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
import  requests
import pymongo
from webdriver_manager.chrome import ChromeDriverManager


def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)

# create scrape function
def scrape():
    browser = init_browser()

    # use browser to open the url 
    url = "https://redplanetscience.com/"

    browser.visit(url)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # get the latest news
    data = soup.find("div", id="news", class_="container")
    news_title = data.find("div", class_="content_title").get_text()
    paragraph = data.find("div", class_="article_teaser_body").get_text()
    

    # for Mars latest image visit the url and get the full image url
    image_url = 'https://spaceimages-mars.com'

    # use browser to open the url for image
    browser.visit(image_url) 

    # create html to parse
    html = browser.html

    # create soup object to parse html
    soup = bs(html, "html.parser")
    
    # Use BeautifulSoup to Navigate to the Image
    image = soup.find("img", class_="headerimage")

    image = image.attrs['src']

    # Create the URL for the Image
    featured_image_url = image_url + "/" + image
   
    # Mars facts
    # get the url for Mars's facts 
    facts_url = 'https://galaxyfacts-mars.com/'

    # Use panda's `read_html` to parse the url
    table = pd.read_html(facts_url)

    # convert table to pandas dataframe
    facts_df = table[0]

    #rename the columns
    facts_df.columns = "Description", "Values", "Earth"

    #Drop the Earth Column
    facts_df = facts_df.drop(columns = ["Earth"])

    # Drop the First Row Information
    facts_df = facts_df.drop(0)

    # reset the index for the df
    facts_df.set_index("Description", inplace=True)

    # convert dataframe to an html table string
    facts_html = facts_df.to_html()

    # Mars hemisphere
    # get the url and open it with browser
    h_url = 'https://marshemispheres.com/'
    browser.visit(h_url)
    # cerate html 
    html = browser.html

    # use beautiful soup to create soup object
    soup = bs(html, "html.parser")

    data = soup.find_all("div", class_="item")
    
    # cretae a list to hold data for hemispheres
    hemisphere_img_urls = []

    # loop the data list to find titles and img urls for hemispheres
    for d in data:
    
        title = d.find("h3").text
    
        img_url = d.a["href"]
    
        url = "https://marshemispheres.com/" + img_url
    
        # use requests to get full images url 
        response = requests.get(url)
    
        # create soup object
        soup = bs(response.text,"html.parser")
    
        # find full image url
        new_url = soup.find("img", class_="wide-image")["src"]
    
        # create full image url
        full_url = "https://marshemispheres.com/" + new_url
        
        #make a dict and append to the list
        hemisphere_img_urls.append({"title": title, "img_url": full_url})
        
    # create mars data dictionary to hold data
    mars_data = {
        "news_title": news_title,
        "paragraph" : paragraph,
        "featured_image_url": featured_image_url,
        "html_table": facts_html,
        "hemisphere_img_urls": hemisphere_img_urls
    }

    # close the browser after scraping
    browser.quit()

    # return results
    return mars_data

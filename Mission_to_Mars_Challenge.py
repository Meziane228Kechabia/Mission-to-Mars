#!/usr/bin/env python
# coding: utf-8

# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd


# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': 'chromedriver'}
browser = Browser('chrome', **executable_path)


# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)


# set up the HTML parser using Beautifulsoup
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('ul.item_list li.slide')

# Let's begin the scraping
slide_elem.find("div", class_='content_title')

# Let's get only the title as text without all that extra html stuff
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p


# ###  Featured Images


# Visit URL
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# Find and click the full image button
full_image_elem = browser.find_by_id('full_image')
full_image_elem.click()



# Find the more info button and click that
browser.is_element_present_by_text('more info', wait_time=1)
more_info_elem = browser.links.find_by_partial_text('more info')
more_info_elem.click()


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# Find the relative image url
img_url_rel = img_soup.select_one('figure.lede a img').get("src")
img_url_rel

# Use the base URL to create an absolute URL
img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
img_url

# Scraping the entire table with Pandas using read_html() function.
df = pd.read_html('http://space-facts.com/mars/')[0]
df.columns=['description', 'value']
df.set_index('description', inplace=True)
df

# Converting DataFramve to html using to_html() function
df.to_html()


# D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles


# Hemispheres

# 1. Use browser to visit the URL 
#url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
url = 'https://mars.nasa.gov/insight/weather/'
browser.visit(url)

# Parse the data
html = browser.html
weather_soup = soup(html, 'html.parser')

# Scrape the Daily Weather Report table
weather_table = weather_soup.find('table', class_='mb_table')
print(weather_table.prettify())


# D1
# 1. Use browser to visit the URL 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)
html = browser.html
items = soup(html, 'html.parser')
#https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars
# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []
# First, get a list of all of the hemispheres
links = browser.find_by_css("a.product-item h3")
# Next, loop through those links, click the link, find the sample anchor, return the href
for i in range(len(links)):
    hemisphere = {}
    # We have to find the elements on each loop to avoid a stale element exception
    browser.find_by_css("a.product-item h3")[i].click()
    # Next, we find the Sample image anchor tag and extract the href
    sample_elem = browser.find_link_by_text('Sample').first
    hemisphere['img_url'] = sample_elem['href']
    # Get Hemisphere title
    hemisphere['title'] = browser.find_by_css("h2.title").text
    # Append hemisphere object to list
    hemisphere_image_urls.append(hemisphere)
    # Finally, we navigate backwards
    browser.back()
# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# Let's shut down the automated browser
#browser.quit()

def init_browser():
    executable_path = {'executable_path': 'chromedriver'}
    browser = Browser('chrome', **executable_path)
    return browser

# Delivrable 2
def scrape_marsH1Cerberus():
     
    browser = init_browser()

    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    browser.visit(url)
    html=browser.html
    sup = soup(html, 'html.parser')
    cerberus_url = (soup.find_all('div', class_='downloads')[0].li.a.get('href'))
    mars_web['hemisphere_urls'] = hemisphere_image_urls
    hemisphere_image_urls.append([{"title": "Cerberus Hemisphere", "img_url": cerberus_url}])
    
    browser.quit()
    return mars_web

def scrape_marsH2Schiaparelli():
 
    browser = init_browser()
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    browser.visit(url)
    html=browser.html
    soup = bs(html, 'html.parser')
    schiaparelli_url = (soup.find_all('div', class_='downloads')[0].li.a.get('href'))
    hemisphere_image_urls.append([{"title": "Schiaparelli Hemisphere", "img_url": schiaparelli_url}])

    browser.quit()
    return mars_web
    
def scrape_marsH3SyrtisMajor():        

    browser = init_browser()
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    browser.visit(url)
    html=browser.html
    soup = bs(html, 'html.parser')
    syrtis_major_url = (soup.find_all('div', class_='downloads')[0].li.a.get('href'))
    hemisphere_image_urls.append([{"title": "Syrtis Major Hemisphere", "img_url": syrtis_major_url}])

    browser.quit()
    return mars_web
        
def scrape_marsH4VallesMarineris():     

    browser = init_browser()
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    browser.visit(url)
    html=browser.html
    soup = bs(html, 'html.parser')
    valles_marineries_url= (soup.find_all('div', class_='downloads')[0].li.a.get('href'))
    hemisphere_image_urls.append([{"title": "Valles Marineris Hemisphere", "img_url": valles_marineries_url}])

    browser.quit()
    return mars_web
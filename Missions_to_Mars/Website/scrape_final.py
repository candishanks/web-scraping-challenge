import os
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager


def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    html = browser.html
    soup = bs(html, "html.parser")

    title_slider = soup.select_one('ul.item_list li.slide')
    title = title_slider.find('div', class_="content_title").get_text()
    title

    paragraph = title_slider.find('div', class_="article_teaser_body").get_text()
    paragraph

    image_slider = soup.select_one('li.slide').get_text
    image_slider

    img = url + image_slider

    mars_data = {
        "Article Title": title,
        "Article Paragraph": paragraph,
        "Images": img
    }

    browser.quit()

    return mars_data

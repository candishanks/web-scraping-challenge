from splinter import Browser
from bs4 import BeautifulSoup as bs


def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    time.sleep(1)

    html = browser.html
    soup = bs(html, "html.parser")

    avg_temps = soup.find('div', id='weather')

    min_temp = avg_temps.find_all('strong')[0].text

    max_temp = avg_temps.find_all('strong')[1].text

    relative_image_path = soup.find_all('img')[2]["src"]
    sloth_img = url + relative_image_path

    costa_data = {
        "sloth_img": sloth_img,
        "min_temp": min_temp,
        "max_temp": max_temp
    }

    browser.quit()

    return costa_data

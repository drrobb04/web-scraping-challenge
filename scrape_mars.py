#dependencies
import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser

def news(browser):
    #code for scraping
    browser = Browser('chrome', **executable_path, headless=False)
    scrape_url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(scrape_url)
    html = browser.html
    news_soup = bs(html, "html.parser")
    articles = news_soup.find_all('div', class_ = "list_text")
    top_article = articles[0]
    news_title = top_article.find(class_ = "content_title").text
    news_graph = top_article.find(class_ = "article_teaser_body").text
    return news_title, news_graph

def image(browser):
    #code for scraping
    browser = Browser('chrome', **executable_path, headless=False)
    scrape_url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"
    browser.visit(scrape_url)
    html = browser.html
    jpl_soup = bs(html, "html.parser")
    image = jpl_soup.find("div", class_ = "floating_text_area")
    subset = image.find("a")
    reference = subset["href"]
    jpl_url = f"https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{reference}"
    return jpl_url

def facts():
    #code for scraping
    mars_facts_df = pd.read_html("https://space-facts.com/mars/")[0]
    return mars_facts_df.to_html()



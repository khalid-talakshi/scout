from xml.etree.ElementTree import fromstring
from django.utils.dateparse import parse_datetime
from datetime import datetime
import requests

def get_mlb_news():
    news_xml = requests.get('https://www.mlb.com/feeds/news/rss.xml')
    tree = fromstring(news_xml.text)
    # root = tree.getroot()
    news = []
    for item in tree.findall('channel/item'):
        date = datetime.strptime(item.find('pubDate').text, '%a, %d %b %Y %H:%M:%S %Z').strftime('%b %d, %Y')
        news_item = {}
        news_item['title'] = item.find('title').text
        news_item['link'] = item.find('link').text
        news_item['pubDate'] = date
        news_item['image'] = item.find('image').attrib['href']
        news_item['author'] = item.find('{http://purl.org/dc/elements/1.1/}creator').text
        news.append(news_item)
    return news

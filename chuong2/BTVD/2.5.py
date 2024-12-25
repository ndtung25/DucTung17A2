import requests
import xml.etree.ElementTree as ET
import csv

def download_rss_feed(url, xml_file_name):
    response = requests.get(url)
    with open(xml_file_name, 'wb') as file:
        file.write(response.content)

def parse_rss_feed(xml_file_name):
    tree = ET.parse(xml_file_name)
    root = tree.getroot()
    news_items = []
    
    for item in root.findall(".//item"):
        news = {
            "title": item.find("title").text,
            "link": item.find("link").text,
            "description": item.find("description").text,
            "pubDate": item.find("pubDate").text
        }
        news_items.append(news)
    
    return news_items

def save_to_csv(news_items, csv_file_name):
    keys = news_items[0].keys()
    with open(csv_file_name, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(news_items)

if __name__ == "__main__":
    url = "http://www.hindustantimes.com/rss/topnews/rssfeed.xml"
    xml_file_name = "rss_feed.xml"
    csv_file_name = "news_items.csv"
    
    download_rss_feed(url, xml_file_name)
    
    news_items = parse_rss_feed(xml_file_name)
    
    if news_items:
        save_to_csv(news_items, csv_file_name)
        print(f"Lưu tin tức thành công vào '{csv_file_name}'.")
    else:
        print("Không tìm thấy mục tin tức nào.")

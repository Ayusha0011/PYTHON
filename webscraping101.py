from bs4 import BeautifulSoup
import requests

html_text =requests.get('https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=python&cboWorkExp1=-1&txtLocation=').text
soup = BeautifulSoup(html_text,'lxml')
jobs = soup.find_all('div', class_='srp-listing clearfix srp-swipeleft')
print(jobs)
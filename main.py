from bs4 import BeautifulSoup
import requests

html_content = requests.get(
    'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=')
print(html_content)

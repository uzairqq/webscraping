from bs4 import BeautifulSoup
import requests

html_content = requests.get(
    'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_content, 'lxml')
jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")

for job in jobs:
    company_name = job.find(
        'h3', class_="joblist-comp-name").text.strip()
    job_skills = job.find(
        'span', class_="srp-skills").text.strip().replace(' ', '')
    job_posted = job.find(
        'span', class_="sim-posted").text.strip()

    print(f'''
    Company Name: {company_name}
    Skills Needed: {job_skills}
    Job Posted: {job_posted}
    ''')

    print('')

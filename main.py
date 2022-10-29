from bs4 import BeautifulSoup
import requests

html_content = requests.get(
    'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_content, 'lxml')
jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")

for job in jobs:
    job_posted = job.find(
        'span', class_="sim-posted").text.strip()
    if 'few' not in job_posted:
        company_name = job.find(
            'h3', class_="joblist-comp-name").text.strip()
        job_skills = job.find(
            'span', class_="srp-skills").text.strip().replace(' ', '')
        more_info = job.header.h2.a['href']

        print(f"Company Name: {company_name}")
        print(f"Required Skills: {job_skills}")
        print(f"This Job Posted: {job_posted}")
        print(f"More Information: {more_info}")

        # print(f'''
        # Company Name: {company_name}
        # Skills Needed: {job_skills}
        # Job Posted: {job_posted}
        # ''')

        print('')

from bs4 import BeautifulSoup
import requests
import time

print('Put Some Skills that you are not fimiliar with')
unfimiliar_skills = input('>')


def findJobs():
    html_content = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_content, 'lxml')
    jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
    for index, job in enumerate(jobs):
        job_posted = job.find(
            'span', class_="sim-posted").text.strip()
        if 'few' not in job_posted:
            company_name = job.find(
                'h3', class_="joblist-comp-name").text.strip()
            job_skills = job.find(
                'span', class_="srp-skills").text.strip().replace(' ', '')
            more_info = job.header.h2.a['href']

            if unfimiliar_skills not in job_skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name} \n")
                    f.write(f"Required Skills: {job_skills} \n")
                    f.write(f"This Job Posted: {job_posted} \n")
                    f.write(f"More Information: {more_info} \n")
                    print(f"File Saved: {index}")


if __name__ == '__main__':
    while True:
        findJobs()
        timewait = 10
        print(f"Waiting {timewait} Minutes...")
        time.sleep(timewait * 60)

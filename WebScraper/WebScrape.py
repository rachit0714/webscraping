from bs4 import BeautifulSoup
import requests

def main(unfamiliar_skills):


    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for job in jobs:
        published_date = job.find('span', class_ = 'sim-posted').span.text
        if 'day' in published_date:
            skills = job.find('span', class_='srp-skills').text.replace('  , ',',')
            skills = skills.strip()
            for skill in unfamiliar_skills:
                if skill not in skills:
                    job_title = job.find('header', class_='clearfix')
                    job_title = job_title.find('a').text.strip()
                    company_name = job.find('h3').text.strip()
                    job_link = job.header.h2.a['href']
                    print(job_title)
                    print(f'Company Name: {company_name}')
                    print(f'Required Skills: {skills}')
                    print(job_link)
                    print('')

def start():
    print('Put some skills that you are unfamiliar with')
    unfamiliar_skills = []
    unfamiliar_skill = 'skills'
    while unfamiliar_skill != '':
        unfamiliar_skill = ''
        unfamiliar_skill = input('>')
        unfamiliar_skills.append(unfamiliar_skill)
    main(unfamiliar_skills)

if __name__ == '__main__':
    while True:
        start()
        print('Type Y/y if you want to remake the filters')
        if input('>') not in ['y','Y']:
            break

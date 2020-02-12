# return 값을 잘 불러오긴 하지만
# <span> 값이 같이 출력되서 번잡함 ㅠㅠ
import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs?q=python&sort=i"


def get_last_page():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")
  pages = soup.find("div", {"class":"s-pagination"}).find_all("a")
  last_page = pages[-2].get_text(strip=True)
  return int(last_page)


def extract_job(html):
  title = html.find("h2", {"class":"fs-body3"}).find("a")["title"]
  company, location = html.find("h3", {"class":"fs-body1"}).find_all("span", recursive=False)
  company.get_text(strip=True)
  location.get_text(strip=True).strip("-").strip(" \r").strip("\n")
  job_id = html["data-jobid"]
  return {"title": title, "company": company, "location": location, "link": f"https://stackoverflow.com/jobs/{job_id}"}


def extract_jobs(last_page):
  jobs = []
  for page in range(last_page):
    result = requests.get(f"{URL}&pg={page + 1}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class":"-job"})
    for result in results:
      job = extract_job(result)
      print(job)
      jobs.append(job)
  return jobs


def get_jobs():
  last_page = get_last_page()
  jobs = extract_jobs(last_page)
  return jobs


# company.string / location.string을 붙여서 return해줌
# 결과는 나쁘지 않지만 여전히 띄어쓰기가 복잡함
def extract_job(html):
  title = html.find("h2", {"class":"fs-body3"}).find("a")["title"]
  company, location = html.find("h3", {"class":"fs-body1"}).find_all("span", recursive=False)
  company.get_text(strip=True)
  location.get_text(strip=True)
  job_id = html["data-jobid"]
  return {"title": title, "company": company.string, "location": location.string, "link": f"https://stackoverflow.com/jobs/{job_id}"}


# SOF 최종
import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs?q=python&sort=i"


def get_last_page():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")
  pages = soup.find("div", {"class":"s-pagination"}).find_all("a")
  last_page = pages[-2].get_text(strip=True)
  return int(last_page)


def extract_job(html):
  title = html.find("h2", {"class":"fs-body3"}).find("a")["title"]
  company, location = html.find("h3", {"class":"fs-body1"}).find_all("span", recursive=False)
  company.get_text(strip=True)
  location.get_text(strip=True)
  job_id = html["data-jobid"]
  return {"title": title, "company": company.string, "location": location.string, "link": f"https://stackoverflow.com/jobs/{job_id}"}


def extract_jobs(last_page):
  jobs = []
  for page in range(last_page):
    print(f"Scrapping SOF: Page: {page}")
    result = requests.get(f"{URL}&pg={page + 1}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class":"-job"})
    for result in results:
      job = extract_job(result)
      jobs.append(job)
  return jobs


def get_jobs():
  last_page = get_last_page()
  jobs = extract_jobs(last_page)
  return jobs


# Indeed 최종
import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class": "pagination"})

    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]
    return max_page


def extract_job(html):
    title = html.find("div", {"class": "title"}).find("a")["title"]
    company = html.find("span", {"class": "company"})
    company_anchor = company.find("a")
    if company:
      if company_anchor is not None:
          company = str(company_anchor.string)
      else:
          company = str(company.string)
      company = company.strip()
    else:
      company = None
    location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]
    job_id = html["data-jk"]
    return {
        'title': title,
        'company': company,
        'location': location,
        "link": f"https://www.indeed.com/viewjob?jk={job_id}"
    }


def extract_jobs(last_page):
  jobs = []
  for page in range(last_page):
    print(f"Scrapping Indeed: Page: {page}")
    result = requests.get(f"{URL}start={page * LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
    for result in results:
      job = extract_job(result)
      jobs.append(job)
  return jobs


def get_jobs():
  last_page = get_last_page()
  jobs = extract_jobs(last_page)
  return jobs


# main.py 수정
from indeed import get_jobs as get_indeed_jobs
from sof import get_jobs as get_sof_jobs


indeed_jobs = get_indeed_jobs()
sof_jobs = get_sof_jobs()

jobs = indeed_jobs + sof_jobs
print(jobs)
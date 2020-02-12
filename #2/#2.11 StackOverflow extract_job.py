# 오류때문에 찾은 다른분의 코딩 케이스
def extract_job(html):
  title = html.find("h2", {"class":"fs-body3"}).find("a")["title"]
  company, location = html.find("h3", {"class":"fs-body1"}).find_all("span", recursive=False)
  company.get_text(strip=True)
  location.get_text(strip=True)
  job_id = html["data-jobid"]
  return {"title": title, "company": company, "location": location, "link": f"https://stackoverflow.com/jobs/{job_id}"}


# 'Tag' object cannot be interpreted as an integer
# extract_jobs >> extract_job
# 고작 s 하나 때문에 1시간을 헤맸다니....
import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs?q=python&sort=i"


def get_last_page():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")
  pages = soup.find("div", {"class":"s-pagination"}).find_all("a")
  last_page = pages[-2].get_text(strip=True)
  return int(last_page)


def extract_jobs(last_page):
  jobs = []
  for page in range(last_page):
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


# title 가져오기
def extract_job(html):
  title = html.find("h2", {"class":"fs-body3"}).find("a")["title"]
  print(title)


# company, location 가져오기
# get_text(strip_True)를 통해서 text만 깔끔하게 가져옴.
def extract_job(html):
  title = html.find("h2", {"class":"fs-body3"}).find("a")["title"]
  company, location = html.find("h3", {"class":"fs-body1"}).find_all("span", recursive=False)
  company.get_text(strip=True)
  location.get_text(strip=True)
  print(company, location)
# print(company.string, location.string)으로 str만 가져오기!


# 지금까지의 sof.py 결과물!
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
  print(company.string, location.string)


def extract_jobs(last_page):
  jobs = []
  for page in range(last_page):
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
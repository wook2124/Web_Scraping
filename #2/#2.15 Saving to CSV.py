# open(파일을 열어주는 역할)함수, mode(읽기전용과 쓰기전용으로 나뉨)
# mode에서 읽기전용은 read(r)이고, 쓰기전용은 write(w)!
# writer = csv.writer(file)의 의미:
# writer란 우리가 정한 'file'이라고 저장한 변수를 csv로 쓰겠다는 것을 정하는 변수
# writer.writerow()의 의미:
# writer 변수로 정한 쓰기권으로 write_row(행) 즉, 행을 추가한다는 뜻
import csv

def save_file(jobs):
  file = open("jobs.csv", mode="w")
  writer = csv.writer(file)
  writer.writerow(["title", "company", "location", "link"])
  print(jobs)
  return


# indeed 원본!! 
# 수업진행 할 때, 모든 페이지를 갖고오면 시간이 많이 걸려서
# 2페이지만 가져오는 함수로 바꿔놨음.
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


# jobs에 있는 각 job을 가지고 row(행)를 작성함
# job이 가진 값의 list를 row(행)로 가져올 것임
import csv

def save_file(jobs):
  file = open("jobs.csv", mode="w")
  writer = csv.writer(file)
  writer.writerow(["title", "company", "location", "link"])
  for job in jobs:
    writer.writerow(list(job.values()))
  return
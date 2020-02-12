# .strip("-").strip(" \r").strip("\n")을 추가해서
# 출력되는 것을 정리하고자함
# "-"는 뒤에 나오는 -를 지우고
# " \r"은 새로운 줄을 표현하는 방법
# "\n"도 " \r"처럼 새로운 줄을 표현함
# 그러나 뒤에 이런것들 추가안해도 전이랑 똑같음!
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


# 추가표현 지우고, return값 입력해줌!
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
  return {"title": title, "company": company, "location": location}


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
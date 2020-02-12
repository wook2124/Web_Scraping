# extract_job(html)로 함수 간소화시키기
# 그리고 {}를 지정해서 dictionary 만들기
# title과 company 이름 따로따로 나오게끔함!
import requests
from bs4 import BeautifulSoup


LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")
  pagination = soup.find("div", {"class":"pagination"})

  links = pagination.find_all('a')
  pages = []
  for link in links[:-1]:
    pages.append(int(link.string))

  max_page = pages[-1]
  return max_page


def extract_job(html):
      title = html.find("div", {"class":"title"}).find("a")["title"]
      company = html.find("span", {"class":"company"})
      company_anchor = company.find("a")
      if company_anchor is not None:
        company = str(company_anchor.string)
      else:
        company = str(company.string)
      company = company.strip()
      return {'title': title, 'company': company}


def extract_indeed_jobs(last_page):
  jobs = []
  # for page in range(last_page):
  result = requests.get(f"{URL}start={0 * LIMIT}")
  soup = BeautifulSoup(result.text, "html.parser")
  results = soup.find_all("div", {"class":"jobsearch-SerpJobCard"})
  for result in results:
    job = extract_job(result)
    print(job)
  return jobs


# 맨 마지막 함수인 extract_indeed_jobs 수정
# job을 jobs에 append(추가)해줌
def extract_indeed_jobs(last_page):
  jobs = []
  # for page in range(last_page):
  result = requests.get(f"{URL}start={0 * LIMIT}")
  soup = BeautifulSoup(result.text, "html.parser")
  results = soup.find_all("div", {"class":"jobsearch-SerpJobCard"})
  for result in results:
    job = extract_job(result)
    jobs.append(job)
  return jobs


# 중간 함수인 extract_job 수정
# location을 None이 뜨지 않게 가져오기 위해서
# display : None이 뜨기 전인 data-rc-loc까지의 정보를 출력!
def extract_job(html):
      title = html.find("div", {"class":"title"}).find("a")["title"]
      company = html.find("span", {"class":"company"})
      company_anchor = company.find("a")
      if company_anchor is not None:
        company = str(company_anchor.string)
      else:
        company = str(company.string)
      company = company.strip()
      location = html.find("div", {"class":"recJobLoc"})["data-rc-loc"]
      print(location)
      return {'title': title, 'company': company, 'location': location}


# 중간 함수인 extract_job 수정
# Format Document를 통해 코드 포맷 수정하고
# ji={job_id} 인자 설정
def extract_job(html):
    title = html.find("div", {"class": "title"}).find("a")["title"]
    company = html.find("span", {"class": "company"})
    company_anchor = company.find("a")
    if company_anchor is not None:
        company = str(company_anchor.string)
    else:
        company = str(company.string)
    company = company.strip()
    location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]
    job_id = html["data-jk"]
    return {
        'title': title,
        'company': company,
        'location': location,
        "link": f"https://www.indeed.com/viewjob?jk={job_id}"
    }


# 마지막 함수 extract_indeed_jobs 수정
# 드디어 전체 페이지 돌리기 대작전!
# 추가로 Scrapping page {page}인자도 프린트 되게끔 수정함
# 들여쓰기 잘못해서 0페이지만 출력되었지만, 다시 제대로 고침!
def extract_indeed_jobs(last_page):
  jobs = []
  for page in range(last_page):
    print(f"Scrapping page {page}")
    result = requests.get(f"{URL}start={page * LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
    for result in results:
      job = extract_job(result)
      jobs.append(job)
  return jobs
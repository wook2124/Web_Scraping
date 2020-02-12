# range - 넣은 수만큼의 크기의 배열을 만들어주는 함수
# f("start={n * 50}")로 str과 인자를 분리한 뒤 
# range로 각 페이지를 start=n으로 배열하기
import requests
from bs4 import BeautifulSoup


indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

pagination = indeed_soup.find("div", {"class":"pagination"})

links = pagination.find_all('a')
pages = []
for link in links[:-1]:
  pages.append(int(link.string))

max_page = pages[-1]

for n in range(max_page):
  print(f"start={n * 50}")


# indeed.py로 함수 정리해서 묶어두기
import requests
from bs4 import BeautifulSoup

INDEED_URL = "https://www.indeed.com/jobs?q=python&limit=50"

def extract_indeed_pages():
  result = requests.get(INDEED_URL)
  soup = BeautifulSoup(result.text, "html.parser")
  pagination = soup.find("div", {"class":"pagination"})

  links = pagination.find_all('a')
  pages = []
  for link in links[:-1]:
    pages.append(int(link.string))

  max_page = pages[-1]
  return max_page

# main.py에서 실행하기
from indeed import extract_indeed_pages


max_indeed_pages = extract_indeed_pages()

print(max_indeed_pages)



# indeed.py에 새로운 함수 만들기
# LIMIT로 묶어서 숫자 50, 20만 입력해도 값이 바뀌도록 하기
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


def extract_indeed_jobs(last_page):
  for page in range(last_page):
    print(f"start={page * LIMIT}")

# main.py에서 실행하기
from indeed import extract_indeed_pages, extract_indeed_jobs


last_indeed_page = extract_indeed_pages()

extract_indeed_jobs(last_indeed_page)



# requests.get활용해서 {URL}인자를 만들고
# result로 변수를 저장하고
# result.status_code를 이용해서 '200'을 20개 나오게함.
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


def extract_indeed_jobs(last_page):
  for page in range(last_page):
    result = requests.get(f"{URL}start={page * LIMIT}")
    print(result.status_code)



# 마지막에 이제 일자리(jobs) 관련해서 추출할 것을 
# 미리 설정하고 마무리함. (main.py에는 indeed_jobs)
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
 

def extract_indeed_jobs(last_page):
  jobs = []
  for page in range(last_page):
    result = requests.get(f"{URL}start={page * LIMIT}")
    print(result.status_code)
  return jobs 
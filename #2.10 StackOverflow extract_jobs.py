# indeed.py와 동일하게 extract_jobs을 가져오고
# range는 int(정수)안에서만 기능하기에 
# return int(last_page)로 str을 int로 바꿔줌
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
    print(page)


def get_jobs():
  last_page = get_last_page()
  jobs = extract_jobs(last_page)
  return jobs


# 두 번째 정의 수정하기
# result를 추가함 (page + 1) 해준 것은
# 숫자가 0부터 시작하는 것을 1로 바꾸기 위함!
def extract_jobs(last_page):
  jobs = []
  for page in range(last_page):
    result = requests.get(f"{URL}&pg={page + 1}")
    print(result.status_code)


# 두 번째 정의 수정하기
# indeed.py와 동일하게 soup 변수를 적용시킴
# soup 변수가 각각의 def함수에서 이름도 같지만 오류가 나지 않는 이유는
# 딱 그 함수의 스코프 안에서만 작동하기 때문!
# div 안에있는 class: -job을 찾고 div data-jobid 출력!
def extract_jobs(last_page):
  jobs = []
  for page in range(last_page):
    result = requests.get(f"{URL}&pg={page + 1}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class":"-job"})
    for result in results:
     print(result["data-jobid"])
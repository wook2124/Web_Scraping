# 설치한 beautifulsoup4를 이용!
import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

print(indeed_soup)


# pagination 숫자 20을 찾아봄 (1~20)
# {}는 속성(attribute)를 부여해줌
import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

pagination = indeed_soup.find("div", {"class":"pagination"})

print(pagination)


# pages를 list로 해서 a(anchor) 들을 찾아봄
import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

pagination = indeed_soup.find("div", {"class":"pagination"})

pages = pagination.find_all('a')

print(pages)


# a(anchor)안에있는 span만 뽑아내기!
import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

pagination = indeed_soup.find("div", {"class":"pagination"})

pages = pagination.find_all('a')

for page in pages:
  print(page.find("span"))


# sapns를 [](list)로 묶어서
# 리스트에 "span"만 찾아서 append(추가)해줌
# 그리고 기계는 0부터 세고 마지막 Next수치는 -1임
import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

pagination = indeed_soup.find("div", {"class":"pagination"})

pages = pagination.find_all('a')

spans = [] #list

for page in pages:
  spans.append(page.find("span"))

print(spans[0:-1]) 
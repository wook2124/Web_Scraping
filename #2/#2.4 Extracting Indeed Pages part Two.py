# span에 있는 str만 뽑아내기! .string
import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

pagination = indeed_soup.find("div", {"class":"pagination"})

links = pagination.find_all('a')
pages = []
for link in links:
  pages.append(link.find("span").string)
page = pages[0:-1]
print(page)


# 굳이 span을 검색하지 않고
# anchor로 검색해도 anchor 안에 있는 span을
# BeautifulSoup이 알아서 찾아줌!
import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

pagination = indeed_soup.find("div", {"class":"pagination"})

links = pagination.find_all('a')
pages = []
for link in links:
  pages.append(link.string)
page = pages[0:-1]
print(page)


# int로 str >> int 변환시켜주기
# links[:-1]로 미리 Next를 포함시키지 않도록 방지!
import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

pagination = indeed_soup.find("div", {"class":"pagination"})

links = pagination.find_all('a')
pages = []
for link in links[:-1]:
  pages.append(int(link.string))
print(pages)


# 기계는 0을 처음으로 인식함 때문에 0 = 2페이지
# 그리고 -1은 마지막 페이지인 20페이지, -2는 19페이지
# 그렇다면 -19는 다시 처음인 2페이지임!
import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

pagination = indeed_soup.find("div", {"class":"pagination"})

links = pagination.find_all('a')
pages = []
for link in links[:-1]:
  pages.append(int(link.string))
print(pages[-19])


# max_page = pages[-1] 수치까지 입력하고 끝!
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
# requests에 대해서!
https://github.com/psf/requests


# requests를 package로 설치하고
# r(rename) = requests.get("url") 한 뒤
# html을 text로 부르는데까지 성공!
import requests

indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

print(indeed_result.text)


# 추가로 beautifulsoup4까지 설치완료!
https://www.crummy.com/software/BeautifulSoup/
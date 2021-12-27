import requests
from bs4 import BeautifulSoup

# 크롤링하려는 주소 삽입한 후 서버로부터 응답 받기
response = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90")  

# 응답객체에서 원하는 text 추출하여 html 소스 가져오기
html = response.text

# html 소스 코드를 가져오기 위해 Beautifulsoup에 담기
soup = BeautifulSoup(html, 'html.parser')

# 전체 뉴스기사 불러오기 (리스트 형태로)
links = soup.select(".news_tit")
for link in links:
    title = link.text # 태그 내부의 text 요소 가져오기
    url = link.attrs['href'] # href 속성 값 가져오기
    print(title, url)
#print(links)
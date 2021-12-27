import requests
from bs4 import BeautifulSoup
import pyautogui

# 파이썬 내장 함수 input 사용하여 검색어 입력 받기
keyword = pyautogui.prompt("검색어를 입력하세요.")
# keyword = input("검색어를 입력하세요 >>>")

# 크롤링하려는 주소 삽입한 후 서버로부터 응답 받기
# 위에서 입력받은 keyword를 url에 삽입
response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}")  
# response = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=" + keyword)  

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
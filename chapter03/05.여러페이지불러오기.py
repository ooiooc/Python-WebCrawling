import requests
from bs4 import BeautifulSoup
import pyautogui

# 파이썬 내장 함수 input 사용하여 검색어 입력 받기
keyword = pyautogui.prompt("검색어를 입력하세요.")
lastPage = pyautogui.prompt("마지막 페이지 번호를 입력해주세요.")

pageNum = 1
for i in range(1, int(lastPage) * 10, 10):
    print(f"{pageNum} 페이지 입니다. >>>>>>>>>>>>>>>>")
    response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}&start={i}")  

    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    links = soup.select(".news_tit")
    for link in links:
        title = link.text # 태그 내부의 text 요소 가져오기
        url = link.attrs['href'] # href 속성 값 가져오기
        print(title, url)
    pageNum = pageNum + 1

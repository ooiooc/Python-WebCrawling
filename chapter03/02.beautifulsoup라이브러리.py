import requests
from bs4 import BeautifulSoup

# naver 서버 불러오기
response = requests.get("https://www.naver.com")

# naver에서 html 파일을 받아온다
html = response.text

soup = BeautifulSoup(html, 'html.parser')

# id 값이 NM_set_home_btn인 요소 하나 검색
word = soup.select_one('#NM_set_home_btn')

# text 요소만 출력
print(word.text)

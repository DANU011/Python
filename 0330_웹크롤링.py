#크롤링하는 예시 -한겨레 신문의 오늘의 뉴스 기사 제목을 크롤링
import requests
from bs4 import BeautifulSoup #버전문제 error -> BeautifulSoup4

url = "https://www.hani.co.kr/arti/list.html?sec=news&subsec=politics"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
titles = soup.find_all("h4", class_="article-title")
for title in titles:
    print(title.text.strip())

#requests.get(url)
import requests
from bs4 import BeautifulSoup

url = "https://www.hani.co.kr/arti/list.html?sec=news&subsec=politics"
response = requests.get(url)
print(response.text)

#find()와 find_all() 메서드를 사용한 예시
from bs4 import BeautifulSoup

html = '''
<html>
<body>
<div class="menu">
    <ul>
        <li><a href="/home">Home</a></li>
        <li><a href="/about">About</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
</div>
<div class="content">
    <h1>Hello, World!</h1>
    <p>This is an example of using Beautifulsoup.</p>
</div>
</body>
</html>
'''

soup = BeautifulSoup(html, 'html.parser')

# find() 메서드 사용 예시
div_menu = soup.find('div', {'class': 'menu'})
print("find() : ",div_menu) #.text)

# find_all() 메서드 사용 예시
links = div_menu.find_all('a') #***
# links = soup.find_all('a')
for link in links:
    print("find_all() : ",link.get('href')) #->text)
    #링크를 가지고 올 수 있다는것->이 링크에서 다시 가능

url = "https://www.hani.co.kr/arti/list.html?sec=news&subsec=politics"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

print('line59======================================================================',soup)

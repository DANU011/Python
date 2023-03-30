#웹 스크래핑 예시

import requests
from bs4 import BeautifulSoup

url = 'https://movie.daum.net/ranking/reservation'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

ol=soup.select_one('.list_movieranking')
li_list=ol.find_all('li') # [] -> 리스트 형태
print(li_list)

movie=[]

for li in li_list: #li=tag
    rank=li.select_one('.rank_num').text # class name
    name=li.select_one('.link_txt').text
    see=li.select_one('.ico_see').text
    grade=li.select_one('.txt_grade').text
    num=li.select_one('.txt_num').text[:-1] # 소숫점x
    mvdate=li.select_one('.txt_info > .txt_num').text # class name 같을 경우 구조 사용
    
    movie.append([rank, name, see, grade, num, mvdate])
    print(rank, name, see, grade, num, mvdate)

print(movie) #나와서 확인

import pandas as pd #판다스를 이용해 csv로 저장

df = pd.DataFrame(movie, columns=['순위','영화명','관람가','평점','예매율','개봉일'])

df.to_csv('movie_info.csv',index=False,encoding='cp949')

#print(df.info()) # 저장될 때 전부 오브젝트 숫자와 비교가 안됨.

df = pd.read_csv('movie_info.csv',encoding='cp949') #읽어오면서 숫자는 숫자로 형변환해줌.

print(df.info()) # 형변환 완료

print(df[(df['평점']>8)])


import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['font.family'] = 'Malgun Gothic'

# 23.01.04 -> '%y.%m.%d'
df['개봉일'] = pd.to_datetime(df['개봉일'], format='%y.%m.%d')
#print(df.info()) #datetime64[ns] -> 형변환 된것 확인

df_weekly = df.resample('W', on='개봉일').mean(numeric_only=True ) #숫자 아닌것 워닝 방지)

#plt.plot(df_weekly.index, df_weekly['예매율'])
#plt.show() #결측치 때문에 앞쪽이 날라감.

df_weekly = df_weekly.fillna(0) #결측치 0으로 처리
print(df_weekly)

plt.plot(df_weekly.index, df_weekly['예매율'])
plt.show()

'''
평가
-> 웹크롤링
-> 공공데이터 가져와서 처리
둘 중에 하나 하거나 하나로 해서 4월 10일 까지 제출
'''

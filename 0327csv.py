#csv
import pandas as pd

df = pd.read_csv('일별평균대기오염도_2022.csv', encoding='cp949');

print(df.info());
print(df.head());
print(df.tail(10));
print(df.columns);

# 열 선택 방법 5: iloc[]를 이용한 열 선택 -> 이름이 길 때
#loc 사용시 columns를 이용해서 열이름 copy해서 쓰기
name_age_col = df.iloc[:, [0, 1]]
print(name_age_col)


# 부분 데이터 선택 방법 1: loc[]를 이용한 조건에 따른 선택 #iloc는 조건들어가는거 안됨
sub_df = df.loc[(df['미세먼지농도(㎍/㎥)'] >= 30) & (df['오존농도(ppm)'] >= 0.001)]
print(sub_df)


'''
# 조건을 사용하여 데이터 -> 선택 2개의 조건 () 사용
df.loc[(df['column_name_1'] > 5) & (df['column_name_2'] == 'value')]
'''


# 부분 데이터 선택 방법 2: query()를 이용한 조건에 따른 선택
'''
# 열 선택 방법 4: loc[]를 이용한 열 선택
name_col = df.loc[:, 'name']
print(name_col)
'''
sub_df_2 = df.loc[(df['미세먼지농도(㎍/㎥)'] >= 30)].loc[:,['측정일시', '측정소명','미세먼지농도(㎍/㎥)']]
print(sub_df_2)


'''
# 열 선택 방법 5: iloc[]를 이용한 열 선택
name_age_col = df.iloc[:, [0, 1]]
print(name_age_col)
'''
# 열 선택 방법 5: iloc[]를 이용한 열 선택
sub_df_3 = df.iloc[:, [0, 1]]
print("sub_df_3 : ")
print(sub_df_3)

# 행 선택 방법 1: 대괄호([])를 이용한 단일 행 선택
row_0 = df.iloc[0]
print("대괄호 단일행 : ")
print(row_0)


# 부분 데이터 선택 방법 5: 조건에 따른 선택 후 열 지정
sub_df_5 = df[df['미세먼지농도(㎍/㎥)'] > 30][['미세먼지농도(㎍/㎥)', '측정소명','측정일시']]
print(sub_df_5)


import pandas as pd

# 데이터 파일 경로
data_path = '일별평균대기오염도_2022.csv'

# CSV 파일 읽기
df = pd.read_csv(data_path, encoding="cp949")

# 필요한 필드 추출
df = df[['측정일시', '측정소명', '미세먼지농도(㎍/㎥)', '초미세먼지농도(㎍/㎥)']]

# 결측치 처리
df = df.dropna()

# 측정일시 컬럼의 데이터 타입을 datetime으로 변경
df['측정일시'] = pd.to_datetime(df['측정일시'], format='%Y%m%d')

print(df.head(20))

import matplotlib.pyplot as plt

# 일별 합계 계산
df_daily = df.resample('D', on='측정일시').sum(numeric_only=True)

# 일평균 대기오염도 계산
df_daily['미세먼지농도(㎍/㎥)'] /= 24
df_daily['초미세먼지농도(㎍/㎥)'] /= 24

# 그래프 그리기
plt.plot(df_daily.index, df_daily['미세먼지농도(㎍/㎥)'], label='PM10')
plt.plot(df_daily.index, df_daily['초미세먼지농도(㎍/㎥)'], label='PM2.5')
plt.legend()
plt.xlabel('Date')
plt.ylabel('Concentration')
plt.title('2022 Air Pollution Trend')
plt.show()

# 데이터 시각화 - 일별 대기오염 추이 그래프
import matplotlib.pyplot as plt

# 일별 합계 계산
df_daily = df.resample('D', on='측정일시').sum(numeric_only=True)

# 일평균 대기오염도 계산
df_daily['미세먼지농도(㎍/㎥)'] /= 24
df_daily['초미세먼지농도(㎍/㎥)'] /= 24

# 그래프 그리기
plt.plot(df_daily.index, df_daily['미세먼지농도(㎍/㎥)'], label='PM10')
plt.plot(df_daily.index, df_daily['초미세먼지농도(㎍/㎥)'], label='PM2.5')
plt.legend()
plt.xlabel('Date')
plt.ylabel('Concentration')
plt.title('2022 Air Pollution Trend')
plt.show()

# 데이터 시각화 - 지역별 대기오염 막대 그래프
import matplotlib.pyplot as plt

# 지역별 미세먼지와 초미세먼지 농도 평균 계산
df_area = df.groupby('측정소명').mean(numeric_only=True).head(10)

# 그래프 그리기
plt.bar(df_area.index, df_area['미세먼지농도(㎍/㎥)'], label='PM10')
plt.bar(df_area.index, df_area['초미세먼지농도(㎍/㎥)'], label='PM2.5')
plt.legend()
plt.xlabel('Area')
plt.ylabel('Concentration')
plt.title('Air Pollution by Area')
plt.show()


# 데이터 시각화 - 대기오염 상자그림
import matplotlib.pyplot as plt

# 그래프 그리기
plt.boxplot([df['미세먼지농도(㎍/㎥)'], df['초미세먼지농도(㎍/㎥)']])
plt.xticks([1,2],['PM10', 'PM2.5'])
plt.ylabel('Concentration')
plt.title('Air Pollution Boxplot')
plt.show()


#PM2.5와 PM10가 동시에 이상치인 데이터를 모아서 result.csv 파일로 저장
import pandas as pd

# 데이터 파일 경로
data_path = '일별평균대기오염도_2022.csv'

# CSV 파일 읽기
df = pd.read_csv(data_path, encoding='cp949')

# 필요한 필드 추출
df = df[['측정일시', '측정소명', '미세먼지농도(㎍/㎥)', '초미세먼지농도(㎍/㎥)']]

# 결측치 처리
df = df.dropna()

# 측정일시 컬럼의 데이터 타입을 datetime으로 변경
df['측정일시'] = pd.to_datetime(df['측정일시'], format='%Y%m%d')

# 이상치를 모아서 result.csv 파일로 저장
q1_pm10 = df['미세먼지농도(㎍/㎥)'].quantile(0.25)
q3_pm10 = df['미세먼지농도(㎍/㎥)'].quantile(0.75)
iqr_pm10 = q3_pm10 - q1_pm10
q1_pm25 = df['초미세먼지농도(㎍/㎥)'].quantile(0.25)
q3_pm25 = df['초미세먼지농도(㎍/㎥)'].quantile(0.75)
iqr_pm25 = q3_pm25 - q1_pm25

outlier_df = df[((df['미세먼지농도(㎍/㎥)'] < q1_pm10 - 1.5 * iqr_pm10) | (df['미세먼지농도(㎍/㎥)'] > q3_pm10 + 1.5 * iqr_pm10))
                &
                ((df['초미세먼지농도(㎍/㎥)'] < q1_pm25 - 1.5 * iqr_pm25) | (df['초미세먼지농도(㎍/㎥)'] > q3_pm25 + 1.5 * iqr_pm25))]

outlier_df.to_csv('result.csv', index=False, encoding='utf-8-sig')








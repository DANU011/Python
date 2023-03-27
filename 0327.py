#NumPy -> array 모듈
#pip install numpy 도구 -> 시스템 쉘

import numpy as np

# 1차원 배열 생성
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)  # [1 2 3 4 5]

# 2차원 배열 생성
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2)

'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''

# 배열 데이터 타입 지정
arr3 = np.array([1, 2, 3], dtype=float)
print(arr3)  # [1. 2. 3.]


import numpy as np

# 3차원 배열 생성
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr3d)

# 4차원 배열 생성
arr4d = np.array([[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]])
print(arr4d)

#배열 인덱싱 및 슬라이싱

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# 인덱스가 0부터 시작하므로 arr[0]은 첫번째 요소를 의미함
print(arr[0])  # 1

# 음수 인덱스를 사용하면 배열의 끝부터 요소를 선택할 수 있음
print(arr[-1])  # 5

# 다차원 배열의 인덱싱
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[0, 0])  # 1
print(arr2d[1, 1])  # 5

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# 슬라이싱은 [시작:끝:간격] 형식으로 사용
print(arr[1:4])  # [2 3 4]

# 다차원 배열의 슬라이싱
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[0:2, 1:3])
'''
[[2 3]
 [5 6]]
'''

# 모든 행을 선택할 때는 ':'만 사용 가능
print(arr2d[:, 1])
'''
[2 5 8]
'''

#부울린 인덱싱
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
mask = np.array([True, False, True, False, True])

# mask 배열에 True에 해당하는 인덱스의 요소만 선택
print(arr[mask])  # [1 3 5]

#팬시 인덱싱
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
idx = np.array([0, 2, 4])

# 인덱스 배열에 해당하는 요소만 선택
print(arr[idx])  # [1 3 5]

# 다차원 배열에서의 팬시 인덱싱
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
row_idx = np.array([0, 2])
col_idx = np.array([1, 2])

# 인덱스 배열로 선택된 요소만 선택
print(arr2d[row_idx, col_idx])  # [2 9]

#NumPy 배열은 다양한 수학 연산을 지원
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# 덧셈 연산
print(arr1 + arr2)  # [5 7 9]

# 뺄셈 연산
print(arr1 - arr2)  # [-3 -3 -3]

# 곱셈 연산
print(arr1 * arr2)  # [ 4 10 18]

# 나눗셈 연산
print(arr1 / arr2)  # [0.25 0.4  0.5]

#브로드캐스팅
'''브로드캐스팅은 NumPy에서 크기가 다른 배열 간의 연산을 가능하게 해주는 기능
브로드캐스팅은 작은 배열을 자동으로 확장하여 큰 배열에 맞추어 연산을 수행'''

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6, 7])

'''
# 브로드캐스팅을 통해 크기가 다른 배열 간 연산이 가능
print(arr1 + arr2)  # [ 5  7  9 10]
'''
#유니버설 함수 (Universal Functions)
import numpy as np

arr = np.array([0, 1, 2, 3, 4])

# 제곱근 함수
print(np.sqrt(arr))  # [0.         1.         1.41421356 1.73205081 2.        ]

# 지수 함수
print(np.exp(arr))  # [ 1.          2.71828183  7.3890561  20.08553692 54.59815003]

# 로그 함수
print(np.log(arr+1))  # [0.         0.69314718 1.09861229 1.38629436 1.60943791]


import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# 배열의 요소에 대해 적용되는 함수
print(np.add(arr1, arr2))  # [5 7 9]
print(np.multiply(arr1, arr2))  # [ 4 10 18]
print(np.power(arr1, arr2))  # [   1   32  729]

#배열 변형 및 조작
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# 배열 형태 변경
arr2d = arr.reshape((2, 4))
print(arr2d)

# 배열 구조 변경
arr2d_reshape = arr2d.reshape(4, 2)
print(arr2d_reshape)

# 배열 전치(Transpose)
arr2d_transpose = arr2d.T
print("전치 : ",arr2d_transpose)

#NumPy 배열을 파일로 저장하고 읽어오기 
'''
np.save()는 하나의 NumPy 배열을 하나의 파일로 저장
np.savez()는 여러 개의 NumPy 배열을 하나의 압축 파일(.npz)로 저장
'''

import numpy as np

# 단일 배열 저장
arr1 = np.array([1, 2, 3, 4, 5])
np.save('arr1.npy', arr1)

# 다중 배열 저장
arr2 = np.array([1, 2, 3, 4, 5])
arr3 = np.array([10, 20, 30, 40, 50])
np.savez('arr.npz', arr2=arr2, arr3=arr3)

# 배열 불러오기
loaded_arr1 = np.load('arr1.npy')
loaded_data = np.load('arr.npz')
loaded_arr2 = loaded_data['arr2']
loaded_arr3 = loaded_data['arr3']

#통계 및 수학 함수
#데이터 분석 및 머신 러닝에서 자주 사용되는 다양한 연산을 수행
import numpy as np

# 1차원 배열 생성
arr = np.array([1, 2, 3, 4, 5])

# 평균 계산
print(np.mean(arr))  # 3.0

# 중앙값 계산
print(np.median(arr))  # 3.0

# 표준편차 계산
print(np.std(arr))  # 1.4142135623730951

# 분산 계산
print(np.var(arr))  # 2.0

# 최대값, 최소값 계산
print(np.max(arr))  # 5
print(np.min(arr))  # 1

#확률 분포 및 난수 생성 함수
import numpy as np

# 정규 분포
# loc: 정규 분포의 평균값, scale: 표준편차, size: 생성할 난수의 개수

arr1 = np.random.normal(0, 1, size=10)
print('정규분포 : ',arr1)
'''
[-1.03175853 -0.26330108  0.50114289  0.43128428  1.52632134
 -0.11669154 -0.38778772 -0.58322862  0.1852227  -1.12919514]
'''

# 균등 분포
# low와 high: 균등 분포의 최솟값과 최댓값, size: 생성할 난수의 개수

arr2 = np.random.uniform(0, 1, size=10)
#arr2 = np.random.uniform(low=0.0, high=1.0, size=5)
#[0.2834756  0.41949812 0.91779272 0.2805554  0.1886998 ]
print('균등분포 : ',arr2)
'''
[0.3082703  0.59827088 0.61679035 0.3049514  0.10465949
 0.95647913 0.52484807 0.62345654 0.36863133 0.66491068]
'''

# 이항 분포
# n: 베르누이 시행을 반복하는 횟수, p: 각 시행에서의 성공 확률, size는 생성할 난수의 개수

arr3 = np.random.binomial(10, 0.5, size=10)
print('이항분포 : ',arr3)
'''
[6 7 6 3 7 3 6 3 7 3] -> 각 열번씩 던졌을 때의 결과
'''

# 포아송 분포
# lam: 단위 시간 또는 공간에서 발생하는 사건의 평균 개수, size: 생성할 난수의 개수
# ex 카페 시간당 손님 방문 횟수

arr4 = np.random.poisson(3, size=10)
print('포아송분포 : ',arr4)
'''
[2 2 2 6 2 1 1 1 1 6]
'''

# pandas -> DataFrame

#Series 1차원 배열 형태의 자료구조, 각 요소는 인덱스와 값으로 구성
import pandas as pd

# Series 생성
# 리스트 사용
data = pd.Series([1, 2, 3, 4])
print(data)
# 결과:
# 0    1
# 1    2
# 2    3
# 3    4
# dtype: int64

# 문자열 인덱스 사용
data = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(data)

# 딕셔너리 사용
data1 = {'a': 1, 'b': 2, 'c': 3 ,'d': 4}
s1 = pd.Series(data1)
print(s1)

# 결과:
# a    1
# b    2
# c    3
# d    4
# dtype: int64

#Series 인덱싱 및 슬라이싱
#정수형, 문자열 등 다양한 인덱스 사용 가능 , 슬라이싱을 통한 부분 데이터 선택 가능
import pandas as pd

# 시리즈 생성
data = [10, 20, 30, 40, 50]
index = ['a', 'b', 'c', 'd', 'e']
s = pd.Series(data, index=index)

# 시리즈 인덱싱
print(s['a'])  # 10
print(s[['a', 'c', 'e']])  # a    10, c    30, e    50
print(s[:3])  # a    10, b    20, c    30
print(s[s > 30])  # d    40, e    50

# 기본 산술 연산
import pandas as pd

# 시리즈 생성
data1 = {'a': 1, 'b': 2, 'c': 3}
data2 = {'a': 10, 'c': 30, 'd': 40}
s1 = pd.Series(data1)
s2 = pd.Series(data2)

# 덧셈 연산
s = s1 + s2
print(s)  # a    11.0, b     NaN, c    33.0, d     NaN
           # dtype: float64

# 뺄셈 연산
s = s1 - s2
print(s)  # a    -9.0, b     NaN, c   -27.0, d     NaN
           # dtype: float64

# 곱셈 연산
s = s1 * s2
print(s)  # a    10.0, b     NaN, c    90.0, d     NaN
           # dtype: float64

# 나눗셈 연산
s = s1 / s2
print(s)  # a    0.1 , b     NaN, c    0.1 , d     NaN
           # dtype: float64

# 집계 함수 사용 
import pandas as pd

# 시리즈 생성
data = [10, 20, 30, 40, 50]
index = ['a', 'b', 'c', 'd', 'e']
s = pd.Series(data, index=index)

# 집계 함수 예시
print(s.sum())  # 150
print(s.mean())  # 30.0
print(s.std())  # 15.811388300841896
print(s.max())  # 50
print(s.min())  # 10

#DataFrame
#2차원 테이블 형태의 자료구조, 인덱스와 열(column)로 구성된 데이터

import pandas as pd
import numpy as np

# 데이터프레임 생성 방법 1: 딕셔너리를 이용한 데이터프레임 생성
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}) #행이 아닌 각각의 열이됨.
print(df1)

# 데이터프레임 생성 방법 2: 리스트를 이용한 데이터프레임 생성
data = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
df2 = pd.DataFrame(data, columns=['A', 'B', 'C']) #열이름
print(df2)

# 데이터프레임 생성 방법 3: Numpy 배열을 이용한 데이터프레임 생성
arr = np.array([[1, 4, 7], [2, 5, 8], [3, 6, 9]])
df3 = pd.DataFrame(arr, columns=['A', 'B', 'C'])
print(df3)

# 데이터프레임 생성 방법 4: 시리즈를 이용한 데이터프레임 생성
s1 = pd.Series([1, 2, 3])
s2 = pd.Series([4, 5, 6])
s3 = pd.Series([7, 8, 9])
df4 = pd.DataFrame({'A': s1, 'B': s2, 'C': s3})
print(df4)
'''
# 데이터프레임 생성 방법 5: 외부 데이터 파일을 이용한 데이터프레임 생성
df5 = pd.read_csv('data.csv')
print(df5) #파일 없어서 에러
'''

'''
DataFrame 정보 확인
head(): 데이터프레임에서 상위 5개 데이터를 출력
tail(): 데이터프레임에서 하위 5개 데이터를 출력
info(): 데이터프레임의 정보를 출력합니다. 열 이름, 데이터 타입, 결측치 개수 등을 확인 ***
describe(): 데이터프레임에서 수치형 열의 기술 통계 정보를 출력
columns: 데이터프레임의 열 이름을 출력
index: 데이터프레임의 행 인덱스를 출력
dtypes: 데이터프레임의 열의 데이터 타입을 출력
shape: 데이터프레임의 크기를 출력
isnull().sum(): 데이터프레임에서 결측치의 개수를 출력
'''

#DataFrame 정보 확인
import pandas as pd

# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [25, 30, 35, 40, 45],
        'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo']}
df = pd.DataFrame(data)

# 데이터프레임 정보 출력
print(df.head())            # 상위 5개 데이터 출력
print(df.tail())            # 하위 5개 데이터 출력
print("info : ",df.info())            # 데이터프레임 정보 출력
print("열이름 : ",df.describe())        # 수치형 열의 기술 통계 정보 출력
print(df.columns)           # 열 이름 출력
print(df.index)             # 행 인덱스 출력
print(df.dtypes)            # 열의 데이터 타입 출력
print(df.shape)             # 데이터프레임의 크기 출력
print(df.isnull().sum())    # 결측치 개수 출력

#DataFrame 인덱싱 및 슬라이싱
'''열(column) 선택
iloc[]는 정수 인덱스를 기반으로 데이터를 선택
loc[]는 인덱스의 이름을 기반으로 데이터를 선택
'''
import pandas as pd

# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [25, 30, 35, 40, 45],
        'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo']}
df = pd.DataFrame(data)

# 열 선택 방법 1: 대괄호([])를 이용한 단일 열 선택
name_col = df['name']
print(name_col)

# 열 선택 방법 2: 점(.)을 이용한 단일 열 선택
age_col = df.age
print(age_col)

# 열 선택 방법 3: 대괄호([])를 이용한 복수 열 선택
name_age_col = df[['name', 'age']]
print(name_age_col)

# 열 선택 방법 4: loc[]를 이용한 열 선택
name_col = df.loc[:, 'name']
print(name_col)

# 열 선택 방법 5: iloc[]를 이용한 열 선택
name_age_col = df.iloc[:, [0, 1]]
print(name_age_col)

'''
행(row) 선택
query() 메소드
데이터프레임에서 특정 조건에 맞는 데이터를 선택하는 메소드
조건을 문자열로 입력
'''
# 나이가 30 이상이고, 도시가 'London'인 데이터 선택
sub_df = df.query('age >= 30 and city == "London"')
print(sub_df)

import pandas as pd

# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [25, 30, 35, 40, 45],
        'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo']}
df = pd.DataFrame(data)

# 행 선택 방법 1: 대괄호([])를 이용한 단일 행 선택
row_0 = df.iloc[0]
print(row_0)

# 행 선택 방법 2: loc[]를 이용한 단일 행 선택
row_1 = df.loc[1]
print(row_1)

# 행 선택 방법 3: iloc[]를 이용한 복수 행 선택
rows_1_3 = df.iloc[[1, 3]]
print(rows_1_3)

# 행 선택 방법 4: loc[]를 이용한 복수 행 선택 # 이름이 정수라서 차이가 안나 보임
rows_2_4 = df.loc[[2, 4]]
print(rows_2_4)

sub_df = df.loc[df['age'] >= 30]
print(sub_df)

# 행 선택 방법 5: 슬라이싱을 이용한 범위 지정
rows_1_3 = df[1:4]
print(rows_1_3)

# 행 선택 방법 6: query()를 이용한 조건에 따른 행 선택
rows_age_over_30 = df.query('age > 30')
print(rows_age_over_30)

'''
부분 데이터 선택
at
데이터프레임에서 단일 값을 선택하는 메소드
'''
import pandas as pd

# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [25, 30, 35, 40, 45],
        'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo']}
df = pd.DataFrame(data)

# 부분 데이터 선택 방법 1: loc[]를 이용한 조건에 따른 선택
sub_df_1 = df.loc[df['age'] > 30, ['name', 'city']]
print(sub_df_1)

# 부분 데이터 선택 방법 2: query()를 이용한 조건에 따른 선택
sub_df_2 = df.query('age > 30')[['name', 'city']]
print(sub_df_2)

# 부분 데이터 선택 방법 3: 슬라이싱을 이용한 범위 지정
sub_df_3 = df.iloc[1:3, 1:3]
print(sub_df_3)

# 부분 데이터 선택 방법 4: iloc[]를 이용한 인덱스 지정
sub_df_4 = df.iloc[[1, 3], [0, 2]]
print(sub_df_4)

# 부분 데이터 선택 방법 5: 조건에 따른 선택 후 열 지정
sub_df_5 = df[df['age'] > 30][['name', 'city']]
print(sub_df_5)

# 부분 데이터 선택 방법 6: at[]을 이용한 특정 위치 선택
val = df.at[1, 'age']
print(val)
'''
#loc: 인덱스의 이름
#행 선택하기
# 이름을 사용하여 행 선택
df.loc['row_name']

# 조건을 사용하여 행 선택
df.loc[df['column_name'] > 5]

#열 선택하기
# 열의 이름을 사용하여 열 선택
df.loc[:, 'column_name']

# 열의 이름을 리스트로 사용하여 여러 열 선택
df.loc[:, ['column_name_1', 'column_name_2']]

#조건 사용하기, 괄호로 조건을 묶어서 사용
# 조건을 사용하여 데이터 선택
df.loc[(df['column_name_1'] > 5) & (df['column_name_2'] == 'value')]
=====================================================================

#iloc: 정수 인덱스

#행 선택하기
# 정수를 사용하여 행 선택
df.iloc[0]

# 슬라이스를 사용하여 행 선택
df.iloc[1:3]

# 정수 리스트를 사용하여 행 선택
df.iloc[[0, 2, 4]]

#열 선택하기
# 정수를 사용하여 열 선택
df.iloc[:, 0]

# 정수 리스트를 사용하여 열 선택
df.iloc[:, [0, 2]]

#조건 사용하기, 조건을 사용하여 데이터를 선택하는 기능이 없음
'''

#DataFrame 연산
#기본 산술 연산 및 집계 함수 사용 가능, 열 및 행을 기준으로 연산 가능
import pandas as pd

data1 = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
data2 = {'A': [9, 8, 7], 'B': [6, 5, 4], 'C': [3, 2, 1]}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# 기본 연산
print(df1 + df2)
# 결과:
#    A  B  C
# 0 10 10 10
# 1 10 10 10
# 2 10 10 10

# 집계 함수
print(df1.mean()) # 열방향, 우선 디폴트 -> 결과: A    2.0, B    5.0, C    8.0, dtype: float64
print(df1.mean(axis=1)) # 행방향 -> 결과: 0    4.0, 1    5.0, 2    6.0, dtype: float64


'''
데이터 입출력
CSV, Excel, SQL 등 다양한 형식으로 파일을 저장할 수 있음

import pandas as pd

data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)

# CSV 파일 쓰기
df.to_csv('output.csv', index=False)

# Excel 파일 쓰기
df.to_excel('output.xlsx', sheet_name='Sheet1', index=False)
'''

#결측치 처리 - 결측치 대체, 제거 등
import pandas as pd
import numpy as np

# 예제 데이터
data = {'A': [1, np.nan, 3], 'B': [4, 5, np.nan], 'C': [7, 8, 9]}
df = pd.DataFrame(data)

# 결측치 확인
print(df.isnull())
# 결과:
#        A      B      C
# 0  False  False  False
# 1   True  False  False
# 2  False   True  False

# 결측치 대체
filled_df = df.fillna(0)
print(filled_df)
# 결과:
#      A    B  C
# 0  1.0  4.0  7
# 1  0.0  5.0  8
# 2  3.0  0.0  9

# 결측치 제거 - 행 자체를 제거 .dropna()
dropped_df = df.dropna()
print(dropped_df)
# 결과:
#      A    B  C
# 0  1.0  4.0  7

# 중복 데이터 처리 - 중복 데이터 제거
import pandas as pd

# 예제 데이터
data = {'A': [1, 2, 2], 'B': [4, 5, 5], 'C': [7, 8, 8]}
df = pd.DataFrame(data)

# 중복 확인
print(df.duplicated())
# 결과:
# 0    False
# 1    False
# 2     True

# 중복 제거
deduplicated_df = df.drop_duplicates()
print(deduplicated_df)
# 결과:
#    A  B  C
# 0  1  4  7
# 1  2  5  8


#데이터 형 변환 - astype() :데이터의 자료형을 변환해주는 함수
'''
int 또는 int64: 정수형
float 또는 float64: 실수형
bool 또는 bool_: 불리언형
str 또는 object: 문자열형
category: 범주형
datetime64: 날짜/시간형
'''
import pandas as pd

# 데이터프레임 생성
data = {'int_col': [1, 2, 3, 4, 5],
        'float_col': [1.1, 2.2, 3.3, 4.4, 5.5],
        'str_col': ['1', '2', '3', '4', '5'],
        'bool_col': [True, False, True, False, True],
        'category_col': ['a', 'b', 'c', 'a', 'b'],
        'date_col': ['2022-01-01', '2022-02-01', '2022-03-01', '2022-04-01', '2022-05-01']}

df = pd.DataFrame(data)

# 열 데이터 형 변환
df['int_col'] = df['int_col'].astype(float)  # 정수형 -> 실수형
df['float_col'] = df['float_col'].astype(int)  # 실수형 -> 정수형
df['str_col'] = df['str_col'].astype(bool)  # 문자열 -> 불리언형
df['bool_col'] = df['bool_col'].astype(str)  # 불리언형 -> 문자열형
df['category_col'] = df['category_col'].astype('category')  # 문자열 -> 범주형
df['date_col'] = pd.to_datetime(df['date_col'])  # 문자열 -> 날짜/시간형 ***

# 데이터프레임 정보 출력
print(df.dtypes)


#category
'''
범주형 데이터
범주형 데이터는 주로 성별, 지역, 학교 등과 같이, 일정한 기준에 따라 분류되는 데이터
그룹화, 집계 등 데이터 분석 작업에서 사용
'''
import pandas as pd

# 데이터프레임 생성
data = {'gender': ['Male', 'Female', 'Male', 'Male', 'Female'],
        'age': [20, 30, 25, 35, 27],
        'city': ['Seoul', 'Busan', 'Seoul', 'Incheon', 'Seoul']}

df = pd.DataFrame(data)

# gender 열을 category 형으로 변환
df['gender'] = df['gender'].astype('category')

# city 열을 category 형으로 변환
df['city'] = df['city'].astype('category')

# 카테고리별 데이터 개수 확인
print(df['gender'].value_counts())
print(df['city'].value_counts())

# 카테고리별 통계량 확인
print(df.groupby('gender').mean(numeric_only=True))
print(df.groupby('city').mean(numeric_only=True))


# 데이터 형 변환 - to_numeric(): 데이터를 수치형으로 변환해주는 함수
import pandas as pd

# 데이터프레임 생성
data = {'int_col': [1, 2, 3, 4, 5],
        'float_col': [1.1, 2.2, 3.3, 4.4, 5.5],
        'str_col': ['1', '2', '3', '4', '5']}

df = pd.DataFrame(data)

# 열 데이터 형 변환
df['int_col'] = pd.to_numeric(df['int_col'])  # 정수형 -> 숫자형
df['float_col'] = pd.to_numeric(df['float_col'])  # 실수형 -> 숫자형
df['str_col'] = pd.to_numeric(df['str_col'])  # 문자열 -> 숫자형

# 데이터프레임 출력
print(df)

'''
데이터 형 변환
apply():데이터프레임이나 시리즈에서 함수를 적용하여 새로운 결과를 반환하는 메소드 ->함수를 적용하기 위한 함수
 df.apply(func, axis=0, **kwargs)
func: 적용할 함수
axis: 적용할 축. 0은 열, 1은 행입니다. 기본값은 0
**kwargs: func 함수에 추가적으로 전달할 인수
'''
import pandas as pd

# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie'],
        'age': ['25', '30', '35'],
        'score1': [80, 70, 85],
        'score2': [85, 75, 90]}

df = pd.DataFrame(data)

# apply() 메소드를 이용하여 모든 문자열 값을 대문자로 변환
df['name'] = df['name'].apply(lambda x: x.upper())
df['age'] = df['age'].apply(int)

print(df)


#.str 엑세서를 이용한 문자열 처리 예시
'''
\s: 모든 공백 문자
\w: 모든 단어 문자
^: 부정을 의미
[^\w\s] 패턴은 단어 문자와 공백 문자가 아닌 모든 문자
'''
import pandas as pd

# 샘플 데이터 생성
data = {
    'text': ['Hello, World!', 'Pandas is great', 'Python is awesome']
}
df = pd.DataFrame(data)

# 문자열 처리 작업
df['lower'] = df['text'].str.lower()  # 모든 문자를 소문자로 변환
df['words'] = df['text'].str.split()  # 공백을 기준으로 단어 분할
df['no_punctuation'] = df['text'].str.replace('[^\w\s]', '', regex=True)  # 구두점, 기호 제거
df['word_count'] = df['text'].str.split().str.len()  # 단어 개수 계산

print(df.iloc[:, 1:])


# 열(column) 및 행(row) 조작 - 열(column) 추가
import pandas as pd

# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [25, 30, 35, 40, 45],
        'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo']}
df = pd.DataFrame(data)

# 열 추가 방법 1: 기존 열을 이용하여 새로운 열 추가
df['age2'] = df['age'] + 1

# 열 추가 방법 2: insert() 메소드를 이용하여 특정 위치에 열 추가
df.insert(loc=2, column='gender', value=['F', 'M', 'M', 'M', 'F'])

# 열 추가 방법 3: assign() 메소드를 이용하여 여러 개의 열 한 번에 추가
df = df.assign(age3=[26, 31, 36, 41, 46], height=[160, 170, 180, 175, 165])

# 출력
print(df)


# 열(column) 및 행(row) 조작 - 행(row) 추가
# **** ignore_index=True로 설정하면, 행이 추가된 후의 인덱스가 0부터 다시 생성

import pandas as pd

# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [25, 30, 35, 40, 45],
        'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo']}
df = pd.DataFrame(data)

# 행 추가 방법 1: append() 메소드를 이용하여 단일 행 추가
new_row = {'name': 'Frank', 'age': 50, 'city': 'Seoul'}
df = df.append(new_row, ignore_index=True)

# 행 추가 방법 2: append() 메소드를 이용하여 여러 행 추가
new_rows = [{'name': 'George', 'age': 22, 'city': 'Toronto'},
            {'name': 'Helen', 'age': 27, 'city': 'Sydney'}]
df = df.append(new_rows, ignore_index=True)

# 출력
print(df)


#열(column) 및 행(row) 조작 - 삭제
import pandas as pd

# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [25, 30, 35, 40, 45],
        'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo']}
df = pd.DataFrame(data)

# 행 삭제 방법 1: drop() 메소드를 이용하여 단일 행 삭제
df = df.drop(0)

# 행 삭제 방법 2: drop() 메소드를 이용하여 여러 행 삭제
df = df.drop([1, 2])

# 열 삭제 방법 1: drop() 메소드를 이용하여 단일 열 삭제
df = df.drop('age', axis=1)

# 열 삭제 방법 2: drop() 메소드를 이용하여 여러 열 삭제
df = df.drop(['name', 'city'], axis=1)

# 출력
print(df)


#열(column) 및 행(row) 조작 - 재정렬
import pandas as pd

# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [25, 30, 35, 40, 45],
        'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo']}
df = pd.DataFrame(data)

# 행 재정렬 방법 1: loc[]을 이용하여 행 순서 변경
df = df.loc[[4, 3, 2, 1, 0]]

# 행 재정렬 방법 2: sort_values() 메소드를 이용하여 열 기준으로 정렬
df = df.sort_values('age', ascending=False)

# 열 재정렬 방법 1: 열 이름 순서 변경
df = df[['city', 'name', 'age']]

# 열 재정렬 방법 2: 열 이름을 알파벳 순서로 정렬
df = df.reindex(sorted(df.columns), axis=1)

# 출력
print(df)


# 데이터 병합
# Concat - 데이터프레임을 수직(위-아래) 또는 수평(좌-우)으로 연결하는 데 사용
'''
axis
0: 행방향
1: 열방향

ignore_index=True
인덱스가 0부터 시작하는 연속된 정수로 재설정
'''
import pandas as pd

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']})

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']})

result = pd.concat([df1, df2], axis=0, ignore_index=True)

print(result)

# Merge 두 데이터프레임을 공통 열 또는 인덱스를 기준으로 병합하는 데 사용
# 기본 조인 방법은 inner join
'''
result = pd.merge(left, right, on='key', how='inner’)
result = pd.merge(left, right, on='key', how='outer')
result = pd.merge(left, right, on='key', how='left')
result = pd.merge(left, right, on='key', how='right')
'''
import pandas as pd

left = pd.DataFrame({'key': ['K0', 'K1', 'K3'],
                     'A': ['A0', 'A1', 'A3'],
                     'B': ['B0', 'B1', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K2', 'K3'],
                      'C': ['C0', 'C2', 'C3'],
                      'D': ['D0', 'D2', 'D3']})

result = pd.merge(left, right, on='key', how='outer' )


print(result)


# Join
#인덱스(행이름)를 기준으로 두 데이터프레임을 병합하는 데 사용
#기본적으로 left join을 수행( how=＇inner'|'outer'|'right') 
import pandas as pd

# 예시 데이터
left = pd.DataFrame({'A': ['A0', 'A1', 'A3'],
                     'B': ['B0', 'B1', 'B3']},
                     index=['K0', 'K1', 'K3'])
right = pd.DataFrame({'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']},
                      index=['K0', 'K1', 'K2', 'K3'])

# 인덱스를 기준으로 병합
result = left.join(right)

print(result)


# 데이터 그룹화
# 집계함수 , agg() 메서드 적용
# 데이터 그룹화 - 데이터를 특정 기준에 따라 그룹화하고 집계
import pandas as pd

data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily', 'Frank'],
        'gender': ['F', 'M', 'M', 'M', 'F', 'M'],
        'age': [25, 30, 35, 40, 45, 50],
        'score1': [80, 70, 85, 75, 90, 95],
        'score2': [85, 75, 90, 80, 95, 100]}

df = pd.DataFrame(data)

# count
print(df.groupby('gender')[['score1', 'score2']].count())

# size
print(df.groupby('gender')[['score1', 'score2']].size())

# sum
print(df.groupby('gender')[['score1', 'score2']].sum())

# mean
print(df.groupby('gender')[['score1', 'score2']].mean())

# median
print(df.groupby('gender')[['score1', 'score2']].median())

# min
print(df.groupby('gender')[['score1', 'score2']].min())

# max
print(df.groupby('gender')[['score1', 'score2']].max())

# std
print(df.groupby('gender')[['score1', 'score2']].std())

# var
print(df.groupby('gender')[['score1', 'score2']].var())

# sem
print(df.groupby('gender')[['score1', 'score2']].sem())

# describe
print(df.groupby('gender')[['score1', 'score2']].describe())


# agg
# 집계 함수를 적용하는 함수
# A와 B 컬럼에 대해서 그룹화한 결과에 대해 C 컬럼에 대해서는 count 함수를 적용하고,
# D 컬럼에 대해서는 sum과 mean 함수를 각각 적용
import pandas as pd

df = pd.DataFrame({
    'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
    'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
    'C': [1, 2, 3, 4, 5, 6, 7, 8],
    'D': [10, 20, 30, 40, 50, 60, 70, 80]
})

result = df.groupby(['A', 'B']).agg({'C': 'count', 'D': ['sum', 'mean']})
print(result)


#사용자 정의 함수를 적용 가능
import pandas as pd

df = pd.DataFrame({
    'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
    'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
})

def my_func(x):
    return '-'.join(sorted(x))

result = df.groupby('A').agg({'B': my_func})

print(result)

#		                  B
#A                         
#bar          one-three-two
#foo  one-one-three-two-two


# Pivot_table - 데이터를 재구성하여 요약하거나 집계할 때 유용
# 위 데이터프레임에서 Name 열과 Date 열을 기준으로 Value 열의 평균을 계산하려면
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Alice', 'Bob', 'Bob', 'Alice', 'Alice', 'Bob', 'Bob'],
    'Date': ['Day 1', 'Day 2', 'Day 1', 'Day 2', 'Day 1', 'Day 2', 'Day 1', 'Day 2'],
    'Value': [10, 20, 15, 25, 30, 40, 35, 45]
})

result = df.pivot_table(values='Value', index='Name', columns='Date', aggfunc='mean')

print(result)

#Date   Day 1  Day 2
#Name               
#Alice     20     30
#Bob       25     35


# 매출 데이터를 이용한 지역별, 시간대별 매출 집계
import pandas as pd

# 매출 데이터 생성
data = {'Region': ['East', 'East', 'West', 'West', 'North', 'North', 'South', 'South'], 
        'Time': ['Morning', 'Afternoon', 'Morning', 'Afternoon', 'Morning', 'Afternoon', 'Morning', 'Afternoon'],
        'Sales': [100, 150, 200, 250, 300, 350, 400, 450]}
df = pd.DataFrame(data)

# 피벗테이블 생성
result = pd.pivot_table(df, index='Region', columns='Time', values='Sales', aggfunc='sum')

print(result)


#고객 데이터를 이용한 지역별, 연령대별 평균 소비 금액 집계
import pandas as pd

# 고객 데이터 생성
data = {'Region': ['East', 'East', 'West', 'West', 'North', 'North', 'South', 'South'], 
        'Age': [20, 30, 40, 50, 30, 40, 50, 60],
        'Sales': [100, 150, 200, 250, 300, 350, 400, 450]}
df = pd.DataFrame(data)

# 피벗테이블 생성
result = pd.pivot_table(df, index='Region', columns=pd.cut(df['Age'], [10, 30, 50, 70]), values='Sales', aggfunc='mean')
#.cut(df['Age'], [10, 30, 50, 70]) age를 가져와서  [10, 30, 50, 70] 범위로 쪼개라 -> 열이름으로 들어감
print(result)


# 시계열 데이터 변환
#pd.to_datetime() 문자열이나 다른 형식의 날짜와 시간 데이터를 datetime 형식으로 변환할 때 사용
import pandas as pd

data = {'date': ['2021-08-15', '2021-08-16', '2021-08-17'],
        'value': [100, 200, 150]}
df = pd.DataFrame(data)
print(df.info())
df['date'] = pd.to_datetime(df['date'])
print(df.info())
# Output:
#         date  value
# 0 2021-08-15    100
# 1 2021-08-16    200
# 2 2021-08-17    150

'''
to_datetime에서 자동으로 인식하는 날짜 형식
%Y-%m-%d %H:%M:%S.%f
%Y-%m-%d %H:%M:%S
%Y-%m-%d %H:%M
%Y-%m-%d
%m/%d/%Y %H:%M:%S
%m/%d/%Y %H:%M
%m/%d/%Y
%m/%d/%y %H:%M:%S
%m/%d/%y %H:%M
%m/%d/%y
'''
'''
시계열 데이터 변환
pd.to_datetime()
문자열이 다른 형식으로 되어 있을 경우 이를 자동으로 감지하지 못할 수 있다. 
이때는 format 인자를 사용하여 문자열의 형식을 지정해줄 수 있다.
'''
import pandas as pd

# 날짜 데이터 생성
df = pd.DataFrame({'date': ['2022년 01월 01일', '2022년 01월 02일', '2022년 01월 03일']})

# 날짜 데이터를 datetime 형식으로 변환
df['date'] = pd.to_datetime(df['date'], format='%Y년 %m월 %d일')

# 년, 월, 일 컬럼 추출
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day

print(df)

#dt.year: pandas에서 제공하는 datetime 타입의 열에서 해당 날짜의 연도를 추출하는 속성

'''
날짜 형식 기호
%Y: 네 자리 연도 (예: 2022)
%y: 두 자리 연도 (예: 22)
%m: 두 자리 월 (01부터 12까지)
%d: 두 자리 일 (01부터 31까지)
%H: 두 자리 24시간 기준 시간 (00부터 23까지)
%I: 두 자리 12시간 기준 시간 (01부터 12까지)
%p: AM 또는 PM
%M: 두 자리 분 (00부터 59까지)
%S: 두 자리 초 (00부터 59까지)
%f: 마이크로초 (000000부터 999999까지)
%j: 연중 일 (001부터 366까지)
%U: 연중 주 (일요일을 한 주의 시작으로 기준, 00부터 53까지)
%W: 연중 주 (월요일을 한 주의 시작으로 기준, 00부터 53까지)
%Z: 시간대 이름 (예: PST, EST, UTC 등)
%z: UTC 오프셋 (예: +0900, -0800 등)
'''


'''
시계열 데이터 변환
pd.resample()
기존의 데이터셋을 새로운 시간 간격에 맞추어 변환해줍니다.
미리 정의된 문자열로 일반적인 시간 간격에 대한 별칭을 제공
D(day), H(hour)
on 매개변수를 사용하여 시간 인덱스를 지정
'''
import pandas as pd

data = {'date': ['2022-01-01', '2022-01-02', '2022-02-01', '2022-02-02', '2023-01-01', '2023-01-02', '2023-02-01', '2023-02-02', '2022-01-01', '2022-01-02', '2022-02-01', '2022-02-02', '2023-01-01', '2023-01-02', '2023-02-01', '2023-02-02'],
        'location': ['서울', '서울', '서울', '서울', '서울', '서울', '서울', '서울', '부산', '부산', '부산', '부산', '부산', '부산', '부산', '부산'],
        'PM10': [50, 40, 45, 55, 60, 65, 70, 80, 55, 45, 50, 60, 70, 75, 80, 90],
        'PM2.5': [25, 20, 22, 28, 30, 35, 40, 45, 30, 25, 28, 35, 40, 42, 45, 50]}

df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'])

df_monthly = df.groupby('location').resample('A', on='date').mean(numeric_only=True)
print(df_monthly)

'''
시(시간)계열 데이터 변환
pd.resample()
시간 간격(alias) 문자열
B: 평일(Business day) 기준으로 간격 지정
C: 사용자 지정 시간대 내에서의 주기마다 간격 지정
D: 달력 일(Day) 기준으로 간격 지정
W: 주(Week) 기준으로 간격 지정
M: 달(Month)의 마지막 날 기준으로 간격 지정
SM: 반월(Semi-Month) 기준으로 간격 지정 (월의 15일과 말일을 기준)
BM: 평일 기준으로 한 달의 마지막 날까지 간격 지정
CBM: 사용자 지정 시간대 내에서 평일 기준으로 한 달의 마지막 날까지 간격 지정
MS: 달(Month)의 시작일 기준으로 간격 지정
SMS: 반월(Semi-Month) 기준으로 간격 지정 (월의 1일과 15일을 기준)
BMS: 평일 기준으로 한 달의 시작일부터 마지막 날까지 간격 지정
CBMS: 사용자 지정 시간대 내에서 평일 기준으로 한 달의 시작일부터 마지막 날까지 간격 지정
Q: 분기(Quarter)의 마지막 날 기준으로 간격 지정
BQ: 평일 기준으로 분기의 마지막 날까지 간격 지정
QS: 분기(Quarter)의 시작일 기준으로 간격 지정
BQS: 평일 기준으로 분기의 시작일부터 마지막 날까지 간격 지정
A: 해(Year)의 마지막 날 기준으로 간격 지정
BA: 평일 기준으로 해의 마지막 날까지 간격 지정
AS: 해(Year)의 시작일 기준으로 간격 지정
BAS: 평일 기준으로 해의 시작일부터 마지막 날까지 간격 지정
'''
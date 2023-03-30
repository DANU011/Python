#선 그래프

import matplotlib.pyplot as plt
import numpy as np

# x, y 데이터 생성
x = np.arange(0, 10, 0.1)
y = np.sin(x)

# 선 그래프 그리기
#plt.plot(x, y)

# 선 그래프 스타일 변경
plt.plot(x, y, color='red', linestyle='--', linewidth=2, marker='o', markersize=5)


# 그래프 타이틀과 축 라벨 설정
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('y')

# 그래프 출력
plt.show()

#산점도

import matplotlib.pyplot as plt
import numpy as np

# x, y 데이터 생성
x = np.random.rand(100)
y = np.random.rand(100)

# 산점도 그리기
#plt.scatter(x, y)

# 산점도 스타일 변경
plt.scatter(x, y, color='red', marker='o', s=50, alpha=0.5)


# 그래프 타이틀과 축 라벨 설정
plt.title('Scatter Plot')
plt.xlabel('x')
plt.ylabel('y')

# 그래프 출력
plt.show()

#그래프 스타일링
import matplotlib.pyplot as plt
import numpy as np

# 색상 변경 예제
x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, color='blue')
plt.plot(x, y2, color='#FF5733')
plt.title('Sine and Cosine Waves')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# 라인 스타일 변경 예제
x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, linestyle='dashed')
plt.plot(x, y2, linestyle='dashdot')
plt.title('Sine and Cosine Waves')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

#마커 변경
import matplotlib.pyplot as plt
import numpy as np

# 마커 변경 예제
x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y, marker='^')
plt.title('Scatter Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

#범례 추가
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, linestyle='dashed', label='Sine')
plt.plot(x, y2, linestyle='dashdot', label='Cosine')
plt.title('Sine and Cosine Waves')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper right', fontsize=12, shadow=True, title='Legend')
plt.show()

#스타일 적용하기 plt.style.context() 함수를 사용하여 각 스타일을 적용
import matplotlib.pyplot as plt
import numpy as np

# 스타일 리스트
styles = ['bmh', 'classic', 'dark_background', 'fivethirtyeight', 'ggplot', 'grayscale', 'Solarize_Light2', 'tableau-colorblind10']

# 스타일 적용 예제
for style in styles:
    plt.style.use(style)
    x = np.arange(0, 10, 0.1)
    y1 = np.sin(x)
    y2 = np.cos(x)

    plt.plot(x, y1, label='Sine')
    plt.plot(x, y2, label='Cosine')
    plt.title('Sine and Cosine Waves')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()
    
#서브플롯
import matplotlib.pyplot as plt
import numpy as np

# 2x2 서브플롯 예제
x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

# 2x2 서브플롯 생성
plt.subplot(2,2,1)
plt.plot(x,y1)
plt.title('Sine')

plt.subplot(2,2,3)
plt.plot(x,y1)
plt.title('Sine')

plt.show()

# 첫 번째 서브플롯
axs[0, 0].plot(x, y1)
axs[0, 0].set_title('Sine')




# 두 번째 서브플롯
axs[0, 1].plot(x, y2)
axs[0, 1].set_title('Cosine')

# 세 번째 서브플롯
axs[1, 0].plot(x, y1 + y2)
axs[1, 0].set_title('Sine + Cosine')

# 네 번째 서브플롯
axs[1, 1].plot(x, y1 - y2)
axs[1, 1].set_title('Sine - Cosine')

plt.show()

#막대 그래프 (Bar plot)
import matplotlib.pyplot as plt
import numpy as np

labels = ['apple', 'banana', 'orange', 'grape', 'kiwi']
values = [20, 10, 15, 25, 30]

plt.bar(labels, values)
plt.show()

#히스토그램 (Histogram)
import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(0, 1, 1000)

plt.hist(data)
plt.show()

#히트맵 (Heatmap)
import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(10, 10)

plt.imshow(data, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.show()









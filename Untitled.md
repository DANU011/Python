1. 손실 함수 및 비용 함수 계산 코드  
선형 회귀 비용 함수 (평균 제곱 오차)


```python
import numpy as np

def compute_cost(X, y, w, b):
    """ 
    선형 회귀 비용 함수 계산 (Mean Squared Error)
    
    X: 입력 데이터 (m x n)
    y: 실제 값 (m x 1)
    w: 가중치 벡터 (n x 1)
    b: 편향 (상수)
    """
    m = len(y)  # 샘플 수
    cost = (1 / (2 * m)) * np.sum((X.dot(w) + b - y) ** 2)
    return cost

```

로지스틱 회귀 손실 함수 (이진 교차 엔트로피)


```python
def sigmoid(z):
    """시그모이드 함수"""
    return 1 / (1 + np.exp(-z))

def compute_loss(X, y, theta):
    """
    로지스틱 회귀 손실 함수 (Binary Cross-Entropy Loss)
    
    X: 입력 데이터 (m x n)
    y: 실제 레이블 (m x 1)
    theta: 모델 파라미터 (n x 1)
    """
    m = len(y)
    h = sigmoid(np.dot(X, theta))  # 예측값 (0 ~ 1)
    loss = (-1 / m) * (np.dot(y.T, np.log(h)) + np.dot((1 - y).T, np.log(1 - h)))
    return loss[0]

```

2. 경사 하강법 코드  
선형 회귀 경사 하강법


```python
def gradient_descent(X, y, w, b, learning_rate, iterations):
    """
    선형 회귀 경사 하강법을 사용해 최적 파라미터를 찾음.
    
    X: 입력 데이터 (m x n)
    y: 실제 값 (m x 1)
    w: 가중치 벡터 (n x 1)
    b: 편향 (상수)
    learning_rate: 학습률
    iterations: 반복 횟수
    """
    m = len(y)  # 샘플 수
    cost_history = []  # 비용 저장
    
    for i in range(iterations):
        # 예측 계산
        y_pred = X.dot(w) + b
        
        # 파라미터 업데이트를 위한 미분값 계산
        dw = (1 / m) * X.T.dot(y_pred - y)
        db = (1 / m) * np.sum(y_pred - y)
        
        # 파라미터 업데이트
        w -= learning_rate * dw
        b -= learning_rate * db
        
        # 비용 저장
        cost = compute_cost(X, y, w, b)
        cost_history.append(cost)
        
    return w, b, cost_history

```

로지스틱 회귀 경사 하강법


```python
def gradient_descent_logistic(X, y, theta, learning_rate, iterations):
    """
    로지스틱 회귀 경사 하강법을 사용한 최적 파라미터 찾기
    
    X: 입력 데이터 (m x n)
    y: 실제 레이블 (m x 1)
    theta: 모델 파라미터 (n x 1)
    learning_rate: 학습률
    iterations: 반복 횟수
    """
    m = len(y)
    loss_history = []
    
    for _ in range(iterations):
        # 예측 계산
        h = sigmoid(np.dot(X, theta))
        
        # 파라미터 업데이트
        gradient = np.dot(X.T, (h - y)) / m
        theta -= learning_rate * gradient
        
        # 손실 저장
        loss = compute_loss(X, y, theta)
        loss_history.append(loss)
    
    return theta, loss_history

```

3. 신경망 전방향 및 후방향 전파  
전방향 전파


```python
def forward_propagation(X, parameters):
    """
    신경망 전방향 전파를 수행하여 예측 결과 계산
    
    X: 입력 데이터 (m x n)
    parameters: 신경망 가중치 및 편향을 담은 딕셔너리
    """
    L = len(parameters) // 2  # 신경망 층 수
    A = X
    caches = {"A0": X}  # 각 층의 활성화 값을 저장
    
    for l in range(1, L+1):
        W = parameters[f"W{l}"]
        b = parameters[f"b{l}"]
        Z = np.dot(W, A) + b
        A = sigmoid(Z)  # 활성화 함수 적용
        
        caches[f"Z{l}"] = Z
        caches[f"A{l}"] = A
    
    return A, caches

```

후방향 전파 (가중치 업데이트)


```python
def backward_propagation(x, y, z1, a1, z2, a2, W1, W2, b1, b2, learning_rate):
    """
    신경망 후방향 전파 수행 및 가중치 업데이트
    
    x, y: 입력 및 실제 값
    z1, a1, z2, a2: 각 층의 계산된 값
    W1, W2, b1, b2: 가중치 및 편향
    learning_rate: 학습률
    """
    # 출력층 오차
    delta2 = a2 - y
    dW2 = np.dot(delta2, a1.T)
    db2 = delta2
    
    # 은닉층 오차
    delta1 = np.dot(W2.T, delta2) * relu_derivative(z1)
    dW1 = np.dot(delta1, x.T)
    db1 = delta1
    
    # 가중치와 편향 업데이트
    W1 -= learning_rate * dW1
    b1 -= learning_rate * db1
    W2 -= learning_rate * dW2
    b2 -= learning_rate * db2
    
    return W1, b1, W2, b2

```

4. 벡터화 코드  
벡터화된 예측 및 비용 계산


```python
def predict_with_vectorization(X, coefficients):
    """벡터화를 사용해 예측 수행"""
    return np.dot(X, coefficients)  # 예측 계산을 빠르게 수행

```

벡터화된 경사 하강법


```python
def gradient_descent_with_vectorization(X, y, theta, learning_rate, iterations):
    """
    벡터화를 사용한 경사 하강법
    
    X: 입력 데이터
    y: 실제 값
    theta: 모델 파라미터
    """
    m = len(y)
    for _ in range(iterations):
        predictions = np.dot(X, theta)
        errors = predictions - y
        gradients = np.dot(X.T, errors) / m
        theta -= learning_rate * gradients
    
    return theta

```

로지스틱 회귀용 벡터화 코드


```python
import numpy as np

def sigmoid(z):
    """시그모이드 함수"""
    return 1 / (1 + np.exp(-z))

def predict_with_vectorization_logistic(X, theta):
    """로지스틱 회귀에서 벡터화를 사용한 예측 수행"""
    return sigmoid(np.dot(X, theta))

def gradient_descent_with_vectorization_logistic(X, y, theta, learning_rate, iterations):
    """
    로지스틱 회귀에서 벡터화를 사용한 경사 하강법
    
    X: 입력 데이터
    y: 실제 값
    theta: 모델 파라미터
    learning_rate: 학습률
    iterations: 반복 횟수
    """
    m = len(y)
    for _ in range(iterations):
        # 예측값을 시그모이드로 변환하여 계산
        predictions = predict_with_vectorization_logistic(X, theta)
        
        # 로지스틱 회귀용 경사 계산
        errors = predictions - y
        gradients = np.dot(X.T, errors) / m
        theta -= learning_rate * gradients
    
    return theta

```

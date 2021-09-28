import cv2 as cv
import numpy as np

img = cv.imread("coin.bmp", cv.IMREAD_GRAYSCALE)      # 흑백 영상 읽기
cv.imshow("img", img)
H, W = img.shape[:]     # img의 height, width 값 가져오기
output = np.zeros((H, W), img.dtype)    # 2차원 배열 0 초기화

# 변수 선언
hist = np.zeros(256, int)   # hist: 각 픽셀이 가지는 값(0~255)의 개수
p = np.zeros(256, float)    # p: 각 픽셀 밝기의 비율
N = H * W                   # 전체 픽셀 수
I = 255                     # gray level
sigmaw = np.zeros(N, float) # sigmaw: t에 따른 Sigma_w^2(t)
minSigmaw = 100000          # 0~t 에서의 최소 sigmaw 값
T = 0                       # sigmaw를 최소로 하는 t

#1. 히스토그램 구하기
for y in range(H):
    for x in range(W):
        k = img[y, x]           # k: img(x, y)의 픽셀 값
        hist[k] = hist[k] + 1

#2. 전체 픽셀에 대한 각 밝기의 비율 구하기
for i in range(I):
    p[i] = hist[i] / N

#3. t에 따른 Sigma_w^2(t) 값 구하기
for t in range(I):
    #3-1. q1, q2 구하기
    q1 = q2 = 0
    for i in range(t):
        q1 += p[i]
    for i in range(t + 1, I):
        q2 += p[i]

    if q1 == 0 or q2 == 0:      # 0으로 나눌 경우의 에러 제외
        continue

    #3-2. mu1, mu2 구하기
    mu1 = mu2 = 0
    for i in range(t):
        mu1 += i * p[i] / q1
    for i in range(t+1, I):
        mu2 += (i) * p[i] / q2

    #3-3. sigma1, sigma2 구하기
    sigma1 = sigma2 = 0
    for i in range(t):
        sigma1 += pow(i - mu1, 2) * p[i] / q1
    for i in range(t + 1, I):
        sigma2 += pow(i - mu2, 2) * p[i] / q2

    #3-4. sigmaw 구하기
    sigmaw[t] = q1 * sigma1 + q2 * sigma2

    #4. sigmaw를 최소로 하는 t 구하기
    if minSigmaw > sigmaw[t]:
        minSigmaw = sigmaw[t]
        T = t

#5. 구한 T 값을 이용하여 이진화
for y in range(H):
    for x in range(W):
        if img[x, y] < T:
            output[x, y] = 0
        else:
            output[x, y] = 255

cv.imshow("output", output)
cv.imwrite("1814965_otsu.jpg", output)
cv.waitKey(0)



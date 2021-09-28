import cv2 as cv
import numpy as np

img = cv.imread("citrus.bmp", cv.IMREAD_GRAYSCALE)      # 흑백 영상 읽기
cv.imshow("img", img)
H, W = img.shape[:]     # img의 height, width 값 가져오기
output = np.zeros((H, W), img.dtype)    # 2차원 배열 0 초기화
#valuable 선언 및 초기화
hist = np.zeros(256, int)           # hist: 각 픽셀이 가지는 값(0~255)의 개수
sum_of_hist = np.zeros(256, int)    # sum_of_hist: 누적합

#1. Calculation of histogram
for y in range(H):
    for x in range(W):
        k = img[y, x]           # k: img(x, y)의 픽셀 값
        hist[k] = hist[k] + 1

sum = 0
#2. Cumulative Histogram
for i in range(256):        # 0~255
    sum = sum + hist[i]
    sum_of_hist[i] = sum

#3. Transform the input image to output image
area = H * W        # img 전체 픽셀 수
Dm = 255            # img 최대 밝기
for y in range(H):
    for x in range(W):
        k = img[x][y]
        output[x][y] = (Dm / area) * sum_of_hist[k]

cv.imshow("output", output)
cv.imwrite("1814965_histogramEqualization.jpg", output)
cv.waitKey(0)


import cv2 as cv
import numpy as np

img = cv.imread("citrus.bmp", cv.IMREAD_GRAYSCALE)      # 흑백 영상 읽기
cv.imshow("img", img)
H, W = img.shape[:]     # img의 height, width 값 가져오기
output = np.zeros((H, W), img.dtype)    # 2차원 배열 0 초기화

for y in range(H):
    for x in range(W):
        k = img[x][y]
        output[x][y] = 255 * pow(k/255, 1/2)

cv.imshow("output", output)
cv.imwrite("1814965_gammaCorrection.jpg", output)
cv.waitKey(0)


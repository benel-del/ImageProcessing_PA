import cv2 as cv
import numpy as np
import math

img = cv.imread("edge.png", cv.IMREAD_GRAYSCALE)
H, W = img.shape[:]
output = np.zeros((H, W), img.dtype)

# 1. 행렬 생성
cm = np.zeros((H+W+1, 100), img.dtype)

maxT = 0
maxRho = 0
# 2. 누적 행렬 구성
for y in range(H):
    for x in range(W):
        if img[y, x] == 255:
            for t in range(100):
                theta = np.pi / 100 * t
                rho = x * math.cos(theta) + y * math.sin(theta)
                r = int(rho + 0.5)              # 반올림 역할
                cm[r, t] = cm[r, t] + 1

                # 3. 허프 누적 행렬의 최댓값 선정 알고리즘 작성
                if cm[r, t] > cm[int(maxRho + 0.5), maxT]:
                    maxT = t
                    maxRho = rho

# theta, rho 값 획득
theta = np.pi / 100 * maxT
rho = maxRho

# 4. 획득한 라인 그리기
for j in range(H):
    y = (rho - j * math.cos(theta)) / math.sin(theta)
    output[int(y + 0.5), j] = 255

cv.imshow("input", img)
cv.imshow("output", output)
cv.imwrite("1814965_hough.jpg", output)
cv.waitKey(0)

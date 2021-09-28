# 원본 컬러 영상 읽어 R, G, B 값 획득하기
import cv2 as cv
import numpy as np

img = cv.imread("Mandrill.bmp", cv.IMREAD_COLOR)    # Mandrill.bmp 영상을 Color로 읽기
cv.imshow("image", img)     # img 출력하기
H, W, C = img.shape[:]      # img의 height, width, channel 정보 얻기
img2 = np.zeros((H, W, C), img.dtype)   # img와 동일한 크기의 0으로 채워진 행렬 만들기
img3 = np.zeros((H, W, C), img.dtype)
img4 = np.zeros((H, W, C), img.dtype)

h, w = img.shape[:2]    # img의 height, width 정보 얻기

for y in range(h):
    for x in range(w):
        img2[y, x, 0] = img[y, x, 0]   # img의 B 값만 가져와 img2의 B에 저장
        img3[y, x, 1] = img[y, x, 1]   # img의 G 값만 가져와 img3의 G에 저장
        img4[y, x, 2] = img[y, x, 2]   # img의 R 값만 가져와 img4의 R에 저장
cv.imwrite("Lab02_B.jpg", img2)     # img2를 Lab02_B.jpg로 저장
cv.imwrite("Lab02_G.jpg", img3)
cv.imwrite("Lab02_R.jpg", img4)
cv.imshow("1814965_B", img2)        # img2 출력하기
cv.imshow("1814965_G", img3)
cv.imshow("1814965_R", img4)

cv.waitKey(0)


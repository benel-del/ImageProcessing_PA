# 흑백 영상 읽어 역상 영상 획득하기
import cv2 as cv
import numpy as np

img = cv.imread("rice.bmp", cv.IMREAD_GRAYSCALE)        # 흑백 영상 읽기
H, W = img.shape[:]     # height, width 값 얻기(흑백 - 2차원)
img_inverse = np.zeros((H, W), img.dtype)   # 원본 영상과 동일한 크기의 0으로 채워진 배열 생성
for y in range(H):
    for x in range(W):
        img_inverse[y, x] = 255 - img[y, x]     # 역상 색상 저장

cv.imwrite('Lab02_inverse.jpg', img_inverse)

cv.imshow("image", img)
cv.imshow("image_inverse", img_inverse)
cv.waitKey(0)


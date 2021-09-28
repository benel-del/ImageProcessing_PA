# 버전 확인 + 영상 띄우기
import cv2
import sys

print(cv2.__version__)      # 설치된 openCV 버전 출력하기
print(sys.version)          # 설치된 python 버전 출력하기

img = cv2.imread('1.jpg', cv2.IMREAD_COLOR)     # 1.jpg 영상을 컬러로 읽기
img2 = cv2.resize(img, dsize=(300, 480), interpolation=cv2.INTER_AREA)   # 영상 사이즈 설정하기
cv2.imshow('image', img2)       # 영상 출력하기

cv2.waitKey(0)


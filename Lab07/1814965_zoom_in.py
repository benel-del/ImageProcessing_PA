import cv2 as cv
import numpy as np

src = cv.imread("Mandrill.bmp", cv.IMREAD_COLOR)
cv.imshow("original", src)
H, W, C = src.shape[:]

ratioX = 3
ratioY = 2
newH = H * ratioY
newW = W * ratioX
dst = np.zeros((newH, newW, C), src.dtype)      # destination size 정의

for yD in range(newH):
    for xD in range(newW):
        for c in range(C):
            # origin(x, y) 좌표: x0, y0
            x0 = xD / ratioX
            y0 = yD / ratioY
            x1 = xD // ratioX
            y1 = yD // ratioY

            if x0 == x1 and y0 == y1:       # x0, y0 모두 정수일 경우
                dst[yD][xD] = src[y1][x1]
            else:
                # origin(x, y) 주위의 좌표 4개를 x1, x2, y1, y2로 표현
                x2 = x1 + 1
                y2 = y1 + 1
                if x2 == W:
                    x2 = W - 1
                if y2 == H:
                    y2 = H - 1

                # 양선형 보간법을 위한 거리 비율
                a = x0 - x1
                b = y0 - y1

                if x0 != x1 and y0 != y1:       # x0, y0이 모두 정수가 아닐 경우
                    dst[yD][xD] = (1-a)*b*src[y1][x1] + a*b*src[y1][x2] + (1-a)*(1-b)*src[y2][x1] + a*(1-b)*src[y2][x2]
                elif y0 != y1:      # x0는 정수이고 y0는 정수가 아닐 경우
                    dst[yD][xD] = b * src[y1][x1] + (1 - b) * src[y2][x1]
                elif x0 != x1:      # x0는 정수가 아니고 y0는 정수일 경우
                    dst[yD][xD] = (1 - a) * src[y1][x1] + a * src[y1][x2]

cv.imshow("zoom_in", dst)
cv.imwrite("1814965_zoom_in.jpg", dst)

cv.waitKey(0)

import cv2 as cv
import numpy as np

src = cv.imread("Mandrill.bmp", cv.IMREAD_COLOR)
cv.imshow("img", src)
H, W, C = src.shape[:]
dst = np.zeros((H, W, C), src.dtype)

array_3 = [[1/9 for col in range(3)] for row in range(3)]       # 3*3 Mask
array_5 = [[1/25 for col in range(5)] for row in range(5)]      # 5*5 Mask

# 3*3 Mask Filtering
for y in range(H-1):
    for x in range(W-1):
        for c in range(C):                  # 영상이 color 이므로
            val = 0.0
            for mi in range(-1, 2):         # mi: -1 ~ 1
                for mj in range(-1, 2):     # mj: -1 ~ 1
                    if -1 < y + mi < H and -1 < x + mj < W:
                        val += src[y + mi][x + mj][c] * array_3[mi + 1][mj + 1]
            dst[y, x, c] = np.rint(val)

cv.imshow("output3", dst)
cv.imwrite("1814965_lowpass3.jpg", dst)

# 5*5 Mask Filtering
for y in range(H-2):
    for x in range(W-2):
        for c in range(C):                  # 영상이 color 이므로
            val = 0.0
            for mi in range(-2, 3):         # mi: -2 ~ 2
                for mj in range(-2, 3):     # mj: -2 ~ 2
                    if -1 < y + mi < H and -1 < x + mj < W:
                        val += src[y + mi][x + mj][c] * array_5[mi + 2][mj + 2]
            dst[y, x, c] = np.rint(val)

cv.imshow("output5", dst)
cv.imwrite("1814965_lowpass5.jpg", dst)

cv.waitKey(0)

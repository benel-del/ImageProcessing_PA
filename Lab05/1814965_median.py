import cv2 as cv
import numpy as np

def sort(mask):     # 정렬 함수 정의
    for i in range(8, 0, -1):   # i: 8 ~ 1
        for j in range(0, i):   # j: 0 ~ i-1
            if mask[j] < mask[j + 1]:
                # swap(mask[j], mask[j + 1])
                temp = mask[j + 1]
                mask[j + 1] = mask[j]
                mask[j] = temp
    return mask

src = cv.imread("pepper_noise.bmp", cv.IMREAD_COLOR)
cv.imshow("img", src)
H, W, C = src.shape[:]
dst = np.zeros((H, W, C), src.dtype)
array = np.zeros(9, src.dtype)

for y in range(H-1):
    for x in range(W-1):
        for c in range(C):
            i = 0
            for mi in range(-1, 2):         # mi: -1 ~ 1
                for mj in range(-1, 2):     # mj: -1 ~ 1
                    if -1 < y + mi < H and -1 < x + mj < W:
                        array[i] = src[y + mi][x + mj][c]
                        i += 1
            array = sort(array)         # array 정렬
            dst[y, x, c] = array[4]     # median 지정

cv.imshow("output", dst)
cv.imwrite("1814965_median.jpg", dst)
cv.waitKey(0)

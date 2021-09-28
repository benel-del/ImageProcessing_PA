import cv2 as cv
import numpy as np

src = cv.imread("coin.bmp", cv.IMREAD_GRAYSCALE)
cv.imshow("img", src)
H, W = src.shape[:]

def min(arr, size):
    index = 0
    for i in range(1, size):
        if arr[i] < arr[index]:
            index = i
    return arr[index]

def max(arr):
    index = 0
    for i in range(1, 81):
        if arr[i] > arr[index]:
            index = i
    return arr[index]

def dilation(img):
    dst = np.zeros((H, W), src.dtype)
    for y in range(H):
        for x in range(W):
            index = 0
            array = np.zeros(81)  # 9 * 9 mask
            for mi in range(-4, 5):  # mi: -4 ~ 4
                for mj in range(-4, 5):  # mj: -4 ~ 4
                    if -1 < y + mi < H and -1 < x + mj < W:
                        array[index] = img[y + mi][x + mj]
                        index += 1
            dst[y, x] = max(array)
    return dst

def erosion(img):
    dst = np.zeros((H, W), src.dtype)
    for y in range(H):
        for x in range(W):
            index = 0
            array = np.zeros(81)  # 9 * 9 mask
            for mi in range(-4, 5):  # mi: -4 ~ 5
                for mj in range(-4, 5):  # mj: -4 ~ 5
                    if -1 < y + mi < H and -1 < x + mj < W:
                        array[index] = img[y + mi][x + mj]
                        index += 1
            dst[y, x] = min(array, index)
    return dst

def closing(img):
    return erosion(dilation(img))

# 팽창
img_dilation = dilation(src)
cv.imshow("dilation", img_dilation)
cv.imwrite("1814965_dilation.jpg", img_dilation)

# 침식
img_erosion = erosion(src)
cv.imshow("erosion", img_erosion)
cv.imwrite("1814965_erosion.jpg", img_erosion)

# 채움
img_closing = closing(src)
cv.imshow("closing", img_closing)
cv.imwrite("1814965_closing.jpg", img_closing)

cv.waitKey(0)

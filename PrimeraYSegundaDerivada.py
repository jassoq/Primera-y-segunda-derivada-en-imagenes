import cv2
import numpy as np

img = cv2.imread('IMG.jpg')
cv2.imshow('Imagen Original',img)
B = img[:,:,0]
G = img[:,:,1]
R = img[:,:,2]

EDG = 0.299*(B)+0.587*(G)+0.114*(R)
EDG = EDG.astype(np.uint8)

EDG = np.float_(EDG)
EDG = np.float_(EDG)


x,y = EDG.shape
dx = np.zeros((x, y), dtype= np.float_)
dy = np.zeros((x, y), dtype= np.float_)
d2x = np.zeros((x, y), dtype= np.float_)
d2y = np.zeros((x, y), dtype= np.float_)

for i in range(x - 1):
    for j in range(y):
        devx = EDG[i + 1, j] - EDG[i, j]
        if devx > 0:
            dx[i, j] = devx
        else:
            dx[i, j] = 0


for i in range(x):
    for j in range(y - 1):
        devy = EDG[i, j + 1] - EDG[i, j]
        if devy > 0:
            dy[i, j] = devy
        else:
            dy[i, j] = 0

for i in range(x -1):
    for j in range(y):
        devx_2 = EDG[i +1,j] + EDG[i -1, j] - 2 * EDG[i,j]
        if devx_2 > 0:
            d2x[i,j] = devx_2
        else:
            d2x[i,j] = 0

for i in range(x):
    for j in range(y - 1):
        devy_2 = EDG[i,j + 1] + EDG[i, j - 1] - 2 * EDG[i,j]
        if devy_2 > 0:
            d2y[i,j] = devy_2
        else:
            d2y[i, j] = 0

EDG = np.uint8(EDG)
dx = np.uint8(dx)
dy = np.uint8(dy)
d2x = np.uint8(d2x)
d2y = np.uint8(d2y)

cv2.imshow('Imagen Original',img)
cv2.imshow('Escala de grises', EDG)
cv2.imshow('Primera Derivada X', dx)
cv2.imshow('Primera Deivada Y', dy)
cv2.imshow('Segunda Derivada X',d2x)
cv2.imshow('Segunda Derivada Y',d2y)

'''
concatdx = cv2.hconcat([EDG, dx, dy])
concatdx2 = cv2.hconcat([EDG, d2x, d2y])
cv2.imshow('Priemara Derivada', concatdx)
cv2.imshow('Segunda Derivada', concatdx2)
'''

cv2.waitKey(0)
cv2.destroyAllWindows()

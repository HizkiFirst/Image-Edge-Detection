import cv2 as opencv
import numpy as np

originalImage = opencv.imread('gambar.jpg')

def showImage(img, title):
    opencv.imshow(title,img)
    opencv.waitKey(0)

#mengubah image ke grayscale
grayImage = opencv.cvtColor(originalImage, opencv.COLOR_BGR2GRAY)

rows, cols = grayImage.shape

isEdge = []
edge = grayImage.copy()

#Sobel Kernel X Direction
skX = [
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
]
#Sobel Kernel Y Direction
skY = [
    [-1, -2, -1],
    [0,  0,  0],
    [1,  2,  1]
]
threshold = 50 
# nilai threshold yg diambil 50, 
# semakin tinggi nilai threshold maka program hanya akan mendeteksi 
# edge-edge yang paling jelas saja


#proses mencari central difference
for i in range(rows-1):
    if i > 0:
     for j in range(cols-1):
        if j > 0:
            differenceX = (grayImage[i-1][j-1] * skX[0][0]) + (grayImage[i][j-1] * skX[1][0]) + (grayImage[i+1][j-1] * skX[2][0]) +    (grayImage[i-1][j+1] * skX[0][2]) + (grayImage[i][j+1] * skX[1][2]) + (grayImage[i+1][j+1] * skX[2][2]) 
            differenceY = (grayImage[i-1][j-1] * skY[0][0]) + (grayImage[i-1][j] * skY[0][1]) + (grayImage[i-1][j+1] * skY[0][2]) +    (grayImage[i+1][j-1] * skY[2][0]) + (grayImage[i+1][j] * skY[2][1]) + (grayImage[i+1][j+1] * skY[2][2]) 
            Norm = np.sqrt(pow(differenceX,2) + pow(differenceY,2))
            if Norm > threshold:
                x = [i,j]
                isEdge.append(x)   

for i in range(rows):
    for j in range(cols):
        edge[i,j] = 0

for i in isEdge:
    edge[i[0],i[1]] = 255


showImage(edge, 'Edge')
opencv.imwrite('gray.jpg', grayImage)
opencv.imwrite('Edge.jpg', edge)
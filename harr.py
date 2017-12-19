import numpy as np
import cv2

def harrRow(img, m):
	n = img.shape[0]
	newImg = np.zeros_like(img)
	for i in range(0,n):
		for j in range(0,n):
			newImg[i][j] = img[i][j]
	for i in range(0,m):
		for j in range(0,m/2):
			newImg[i][j] = (img[i][2*j] + img[i][2 * j + 1]) * 0.5
		for j in range(0,m/2):
			newImg[i][j + m/2] = (img[i][2*j] - img[i][2 * j + 1]) * 0.5
	return newImg

def harrCol(img, m):
	newImg = np.transpose(img)
	newImg = harrRow(newImg, m)
	newImg = np.transpose(newImg)
	return newImg

def iHarrRow(img, m):
	n = img.shape[0]
	newImg = np.zeros_like(img)
	for i in range(0,n):
		for j in range(0,n):
			newImg[i][j] = img[i][j]
	for i in range(0,m):
		for j in range(0,m/2):
			newImg[i][2 * j] = img[i][j] + img[i][j + m/2]
			newImg[i][2 * j + 1] = img[i][j] - img[i][j + m/2]
	return newImg

def iHarrCol(img, m):
	newImg = np.transpose(img)
	newImg = iHarrRow(newImg, m)
	newImg = np.transpose(newImg)
	return newImg

def guiyi(img,r1,c1,r2,c2):
	Max = 0.0
	for r in range(r1,r2):
		for c in range(c1,c2):
			if img[r][c] > Max:
				Max = img[r][c]
	for r in range(r1,r2):
		for c in range(c1,c2):
			img[r][c] = img[r][c]/Max * 255.0
	return img

img = cv2.cvtColor(cv2.imread('origin.bmp'),cv2.COLOR_BGR2GRAY).astype('float32')
#print img

n = img.shape[0]
img = harrRow(img,n)
img = harrCol(img,n)
img = harrRow(img,n/2)
img = harrCol(img,n/2)
img = harrRow(img,n/4)
img = harrCol(img,n/4)

cv2.imwrite('Harr4.bmp', img)
absimg = np.abs(img)
cv2.imwrite('Harr4(abs).bmp', absimg)

img = guiyi(img,n/2,n/2,n,n)
img = guiyi(img,0,n/2,n/2,n)
img = guiyi(img,n/2,0,n,n/2)

img = guiyi(img,0,n/4,n/4,n/2)
img = guiyi(img,n/4,0,n/2,n/4)
img = guiyi(img,n/4,n/4,n/2,n/2)

img = guiyi(img,0,n/8,n/8,n/4)
img = guiyi(img,n/8,0,n/4,n/8)
img = guiyi(img,n/8,n/8,n/4,n/4)

cv2.imwrite('Harr(abs-guiyi).bmp',img)
'''
img = iHarrCol(img,n/2)
img = iHarrRow(img,n/2)
img = iHarrCol(img,n)
img = iHarrRow(img,n)
cv2.imwrite('Recover.bmp', img)
print img
'''
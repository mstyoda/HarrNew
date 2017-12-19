import numpy as np
import cv2


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

def getCore88():
	core88 = -np.ones([8,8])
	for i in range(0,4):
		for j in range(0,4):
			core88[i][j] = 1
	for i in range(4,8):
		for j in range(4,8):
			core88[i][j] = 1
	return core88

def harr1(img, core):
	m = core.shape[0]
	step = m//2
	outimg = np.zeros([n//step - 1,n//step -1])
	for i in range(0,n//step - 1):
		for j in range(0,n//step -1):
			sx = i * step
			sy = j * step
			outimg[i][j] = 0
			for x in range(0,m):
				for y in range(0,m):
					outimg[i][j] += img[sx + x][sy + y] * core[x][y]
	outimg = np.abs(outimg)
	outimg = guiyi(outimg, 0, 0, n//step-1, n//step-1)
	return outimg

img = cv2.cvtColor(cv2.imread('origin.bmp'),cv2.COLOR_BGR2GRAY).astype('float32')
#print img

n = img.shape[0]
core22 = np.array([[1,-1],[-1,1]])
core44 = np.array([[-1,-1,1,1],[-1,-1,1,1],[1,1,-1,-1],[1,1,-1,-1]])
core44New = np.array([[1,1,-1,-1],[1,1,-1,-1],[1,1,-1,-1],[1,1,-1,-1]])
core88 = getCore88()
core88New = np.array([
	[1,1,1,1,-1,-1,-1,-1],
	[1,1,1,1,-1,-1,-1,-1],
	[1,1,-1,-1,1,1,-1,-1],
	[1,1,-1,-1,1,1,-1,-1],
	[-1,-1,1,1,-1,-1,1,1],
	[-1,-1,1,1,-1,-1,1,1],
	[-1,-1,-1,-1,1,1,1,1],
	[-1,-1,-1,-1,1,1,1,1]])
img22 = harr1(img, core22)
img44 = harr1(img, core44)
img88 = harr1(img, core88)
img88New = harr1(img, core88New)
img44New = harr1(img, core44New)

cv2.imwrite('core22.bmp',img22)
cv2.imwrite('core44.bmp',img44)
cv2.imwrite('core88.bmp',img88)
cv2.imwrite('core44New.bmp',img44New)
cv2.imwrite('core88New.bmp',img88New)
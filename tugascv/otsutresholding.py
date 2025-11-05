import cv2

image = cv2.imread("example.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)

(T, threshInv) = cv2.threshold(blur, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

cv2.imshow("Otsu", threshInv)
cv2.waitKey(0)

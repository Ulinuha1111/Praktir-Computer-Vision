import cv2

image = cv2.imread("example.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

(T, thresh) = cv2.threshold(gray, 155, 255, cv2.THRESH_BINARY)
(T, threshInv) = cv2.threshold(gray, 155, 255, cv2.THRESH_BINARY_INV)

cv2.imshow("Threshold Binary", thresh)
cv2.imshow("Threshold Binary Inverse", threshInv)
cv2.imshow("Original", image)
cv2.imshow("Masked", cv2.bitwise_and(image, image, mask=threshInv))
cv2.waitKey(0)

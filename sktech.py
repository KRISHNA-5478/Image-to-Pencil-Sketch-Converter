import cv2
img = cv2.imread("main.jpg")
if img is None:
    print("Error: Image not found. Check the path and file name.")
    exit
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
inv = cv2.bitwise_not(gray)
blur = cv2.GaussianBlur(inv, (21, 21), 0)
inv_blur = cv2.bitwise_not(blur)
sketch = cv2.divide(gray, inv_blur, scale=255.0)
cv2.imwrite("sketch.png", sketch)

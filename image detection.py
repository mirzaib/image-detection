import cv2 
Read the image

img = cv2.imread("https://i.pinimg.com/originals/95/b0/3c/95b03cde31e60a52b05c44385a4f1988.jpg")

Convert the image to grayscale

imggray = cv2.cvtColor(img, cv2.COLORBGR2GRAY) 


Perform gaussian blur

imggray = cv2.GaussianBlur(imggray, (21, 21), 0) 


Create a thresholded image

thresh = cv2.threshold(imggray, 25, 255, cv2.THRESHBINARY)[1] 


thresh = cv2.dilate(thresh, None, iterations=2) 


Find contours and calculate their areas

cnts, hierarchy = cv2.findContours(thresh.copy(), cv2.RETREXTERNAL, cv2.CHAINAPPROX_SIMPLE) 
for c in cnts: 
  if cv2.contourArea(c) < 500: 
    continue 
  (x, y, w, h) = cv2.boundingRect(c) 
  # Draw a rectangle around the detected barcode
  
  cv2.rectangle(img, (x, y), (x + height, y + width), (0, 255, 0), 5) 





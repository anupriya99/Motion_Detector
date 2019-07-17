import cv2

img = cv2.imread("C:\\Users\\dell\\Pictures\\Saved Pictures\\animal.jpg",1)

#print(img.shape)

resized = cv2.resize(img,(int(img.shape[1]/2) , int(img.shape[0]/2)))

cv2.imshow("Zoo" , img)
cv2.waitKey(0)
cv2.destroyAllWindows()
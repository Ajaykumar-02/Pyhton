import cv2

# configurable Parameters
source = "STUDENT.jpg" 
destination = "newImage.jpeg"
scale_percent = 50


src = cv2.imread(source,cv2.IMREAD_UNCHANGED)
# cv2.imshow("title",image)

# calculate the 50 % of original demensions 
new_width = int(src.shape[1] * scale_percent / 100)
new_height = int(src.shape[0] * scale_percent / 100)

#resize image 
output = cv2.resize(src,(new_width,new_height))

cv2.imwrite(destination,output)

# cv2.waitKey(0)

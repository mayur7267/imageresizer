import cv2

source = "porche.jpg"
destination='newImage.jpg'
scale_percent=50
src=cv2.imread("porche.jpg",cv2.IMREAD_UNCHANGED)
cv2.imshow("title",src)
width=int(src.shape[1] * scale_percent / 100)
height=int(src.shape[0] * scale_percent /100)
dsize=(width , height)
output=cv2.resize(src,(width,height))
cv2.imwrite(destination ,output)
# cv2.waitKey(0)
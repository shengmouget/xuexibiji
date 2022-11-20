# coding: utf-8 
# @Time    : 2022/11/4 下午10:22
import cv2
def mouse_callback(event,x,y,flags):
    print(event,x,y,flags)
cv2.namedWindow('color',cv2.WINDOW_NORMAL)
img = cv2.imread('/Users/mac/Desktop/DL/fashion_minist/Ankle boot/1.png')
colorspaces = [cv2.COLOR_BGR2RGBA,cv2.COLOR_BGR2BGRA,cv2.COLOR_BGR2GRAY]
cv2.createTrackbar('curcolor','color',1,len(colorspaces),mouse_callback)
while True:
    # cv2.waitKey(0)
    if cv2.waitKey(1)==ord(" "):
        break
    index = cv2.getTrackbarPos('curcolor','color')
#    颜色转换API
    cvt_img = cv2.cvtColor(img,colorspaces[index])
    cv2.imshow('color',img)
cv2.destroyAllWindows()
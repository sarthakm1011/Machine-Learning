import cv2 

cam = cv2.VideoCapture(0)

while True:
	_,frame=cam.read()
	frame = cv2.resize(frame,(400,400))
	
	#rectangle
	cv2.rectangle(frame,(100,100),(200,200),(0,0,0),3)

	#text
	#cv2.putText(frame,"hi",(90,90),1,font,(0,0,0),4,

	cv2.imshow("frame",frame)
	
	if cv2.waitKey(0) == ord('q'):
		break

cv2.destroyAllWindows()

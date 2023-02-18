import cv2

vid = cv2.VideoCapture("C:\\opencv\\testvideos\\car.mp4")
car_cascade = cv2.CascadeClassifier("C:\\opencv\\car_cascade\\cascade.xml")

while 1:
    ret,frame= vid.read()
    frame = cv2.resize(frame,(640,480))
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    carss = car_cascade.detectMultiScale(gray,1.1,2)
    for (x,y,w,h) in carss:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("video",frame)
    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

vid.release()
cv2.destroyAllWindows()
import cv2 as c
from main import get_limits
from PIL import Image

yellow = [0, 255, 255]  # BGR

cap = c.VideoCapture(0)  # try 0, 1, 2 until you find your camera
# On Windows, if it's slow or fails: c.VideoCapture(0, c.CAP_DSHOW)

if not cap.isOpened():
    raise RuntimeError("Could not open camera. Try a different index.")

lowerLimit, upperLimit = get_limits(color=yellow)  # only needs to run once

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    hsv_img = c.cvtColor(frame, c.COLOR_BGR2HSV)
    mask = c.inRange(hsv_img, lowerLimit, upperLimit)
    mask_=Image.fromarray(mask)
    bbox = mask_.getbbox()
    
    print(bbox)
    if bbox is not None:
        x1,y1,x2,y2=bbox
        
        frame=c.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),5)
    
    
    c.imshow("frame", frame)
    c.imshow("mask", mask)

    if c.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
c.destroyAllWindows()

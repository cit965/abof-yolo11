import cv2
from ultralytics import YOLO
import numpy as np

# name_lst = ['cat', 'chicken', 'cow', 'dog', 'fox', 'goat', 'horse', 'person', 'racoon', 'skunk']

my_file = open("coco.txt", "r")
data = my_file.read()
name_lst = data.split("\n")

cap = cv2.VideoCapture(0)
# cap=cv2.VideoCapture('ma.mp4')
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
if not cap.isOpened():
    print("无法打开摄像头")
    exit()
    
model = YOLO("../fall/yolo11n.pt")
w = 1920
h = 1080

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("无法读取帧")
        break
    
    img = cv2.resize(frame, (640, 640))
    results = model.predict(source=img, imgsz=640, conf=0.05, save=False)
    for data in results[0].boxes.data:
        if data[-2].cpu() < 0.6:
            continue
        # cv2.putText(img, name_lst[int(data[-1].cpu())], np.array(data[0:2].cpu(), dtype=int), color=(255, 0, 0), fontScale=2, fontFace=cv2.FONT_HERSHEY_SIMPLEX, thickness=3)
        # cv2.rectangle(img, np.array(data[0:2].cpu(), dtype=int), np.array(data[2:4].cpu(), dtype=int), color=(255, 0, 0), thickness=3)
        x1, y1, x2, y2, conf, cls = np.array(data.cpu()).tolist()
        x1 = int(x1 / 640 * w)
        x2 = int(x2 / 640 * w)
        y1 = int(y1 / 640 * h)
        y2 = int(y2 / 640 * h)
        cls = int(cls)
        cv2.rectangle(frame, [x1, y1], [x2, y2], color=(255, 0, 0), thickness=3)
        cv2.putText(frame, name_lst[cls], [x1, y1], color=(255, 0, 0), fontScale=5, fontFace=cv2.FONT_HERSHEY_SIMPLEX, thickness=4)
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

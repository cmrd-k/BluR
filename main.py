import cv2
import pathlib
import numpy as np

# defines path to Facerecognition classifier and assigns filter to clf
cascade_path = pathlib.Path(cv2.__file__).parent.absolute() / "data/haarcascade_frontalface_default.xml"
clf = cv2.CascadeClassifier(str(cascade_path))

#defines source for video, 0 for webcam, replace 0 with filepath to use saved videos
video = cv2.VideoCapture("./videos/videoplayback.mp4")

while True:
    width = int(video.get(3)) #gets video widht
    height = int(video.get(4)) #gets video height
    mask = np.zeros((height, width, 3), dtype=np.uint8)
    _, frame = video.read()
    blurred = cv2.GaussianBlur(frame, (99,99),0)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = clf.detectMultiScale(
        gray,
        scaleFactor = 1.1,
        minNeighbors = 5,
        minSize =(30,30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )

    for (x, y, width, height) in faces:
        mask = cv2.rectangle(mask, (x,y), (x+width, y+height), (255,255,255), -1)
    out = np.where(mask == np.array([255, 255, 255]), blurred, frame)

    cv2.imshow("Faces", gray)
    if cv2.waitKey(1) == ord("q"):
        break

video.release()
cv2.destroyAllWindows()
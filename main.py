import cv2
from retinaface import RetinaFace
import numpy as np
import time

#defines source for video, 0 for webcam, replace 0 with filepath to use saved videos
video = cv2.VideoCapture("./input/video.mp4")
height = int(video.get(4)) #gets video height
width = int(video.get(3)) #gets video widht
frameCount = int(video.get(7))
framesProcessed = 0
print(f'total frames: {frameCount}')
export = cv2.VideoWriter('./videos/output1.mp4', cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), 20.0, (width,height))


while(video.isOpened()):
    emptyMask = np.zeros((height, width, 1), dtype=np.uint8)  # creates black(0)->white(255) channel
    ret, frame = video.read()
    if ret:
        blurred = cv2.GaussianBlur(frame, (99,99),0)
        faces = RetinaFace.detect_faces(frame)
        # print(faces)
        try: #try catch added bc for loop throws error when no faces in frame
            for key in faces.keys():
                face = faces[key]
                facial_area = face["facial_area"]
                mask = cv2.rectangle(emptyMask, (facial_area[2], facial_area[3]), (facial_area[0], facial_area[1]), (255), -1)
        except Exception as e:
            print(e)
        out = np.where(mask == np.array([255]), blurred, frame)
        export.write(out)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        framesProcessed += 1
        print(f'framesprocessed: {framesProcessed}/{frameCount} == {framesProcessed / frameCount * 100}%')
    else:
        break

processTime = time.process_time()
processTimeM = processTime/60
if processTimeM>= 1:
    print(f'{processTimeM} minutes to process')
else:
    print(f'{processTime} seconds to process')

print(f'Which equates to a Frame processing Rate of {frameCount/processTime} Frames per second')
video.release()
export.release()
cv2.destroyAllWindows()
import cv2
import datetime
import time
import os
from pathlib import Path

now = datetime.datetime.now()                                               # Current time
lVal = 2                                                                    # Loop value !!!DO NOT CHANGE!!! - I know that there are better options for a loop :)
sleepDuration = 10                                                          # Image taking interval 

webserver_path = "C:\webserver"                                             # Location of the Web Server
taken_images_path = Path(__file__).resolve().parent / "taken_images"        # Location of the "taken-images-archive"

print()
print("Webcam script started (Cancel with CRTL + C)")
print("OpenCV Version:",cv2.__version__ )
print("Webcam start:", now)
print()



def captureImage():
    now = datetime.datetime.now()
    timestamp = now.strftime("%d%m%y-%H%M%S")

    filename = taken_images_path / f"capture-{timestamp}.jpg"

    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imwrite("webcam_0.jpg", frame)
    cv2.imwrite(os.path.join(webserver_path, 'webcam_0.jpg'), frame)
    cv2.imwrite(str(filename), frame)
    cap.release()

    print("Captured frame capture -",now.strftime("%d%m%y-%H%M%S"))



while lVal >= 1:

    captureImage()
    time.sleep(sleepDuration)
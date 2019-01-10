
# OpenCV integration with Space Invaders
# Modified by Felipe Bastos <felipebastosweb@gmail.com

import time
import cv2

class DetectHumanMovement(object):
    def __init__(self):
        self.faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        self.handCascade = cv2.CascadeClassifier("haarcascade_hand_default.xml")
        self.video_capture = cv2.VideoCapture(0)
        
        while True:
            if not self.video_capture.isOpened():
                print('Unable to load camera.')
                time.sleep(5)
                continue
            else:
                break
    
    # To capture in main game loop
    def capture_gray_image(self):
        retval, frame = self.video_capture.read()
        self.frame = frame
        if not retval:
            raise Exception('Ops! Capture image failed.')
        # convert to gray scale
        self.gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        return self.gray
    
    # detect all faces in gray image
    def detect_faces(self):
        faces = self.faceCascade.detectMultiScale(
                self.gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(35, 35)
            )
        return faces
    
    # detect all fist
    def detect_fists(self):
        fists = self.handCascade.detectMultiScale(
                self.gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(35, 35)
            )
        return fists

    """
    Define Face Horizontal Orientation (Left or Right)
    window (ex = 0 to WIDTH)
    ---------------x'-------
    -----x'-----------------
    x' <- 500 and
    x' <- 300
    p = x' - (WIDTH / 2)
    """
    def face_h_position(self, face, width):
        (x, y, w, h) = face
        orientation = int((x + (w / 2)) - (width / 2))
        return orientation

    """
    Check Fist to shoot missile
    """
    def fist_check(self):
        fists = self.detect_fists()
        return len(fists)



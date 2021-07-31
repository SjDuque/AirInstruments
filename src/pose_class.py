import cv2
import mediapipe as mp
import math

class BodyPose:

    MP_DRAWING = mp.solutions.drawing_utils
    MP_POSE = mp.solutions.pose

    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.pose = BodyPose.MP_POSE.Pose(
            min_detection_confidence=0.5, 
            min_tracking_confidence=0.5
        )
    
    def isOpened(self):
        return self.cap.isOpened()
    
    def get(self, draw = True):
        
        if self.isOpened():

            success, image = self.cap.read()
            if not success:
                print("Ignoring empty camera frame.")
                return

            # Flip the image horizontally for a later selfie-view display, and convert
            # the BGR image to RGB.
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            # To improve performance, optionally mark the image as not writeable to
            # pass by reference.
            image.flags.writeable = False
            results = self.pose.process(image)

            # Draw the pose annotation on the image.
            image.flags.writeable = True
            
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            if draw:
                BodyPose.MP_DRAWING.draw_landmarks(
                    image, results.pose_landmarks, BodyPose.MP_POSE.POSE_CONNECTIONS)
            cv2.imshow('Air Instrument', cv2.flip(image, 1))

            return results
    

    def find_arm_angle(self, results):
        # Calculate the angle of the elbow

        if results.pose_landmarks is None:
            return

        landmarks = results.pose_landmarks.landmark
        
        PL = BodyPose.MP_POSE.PoseLandmark
        left_shoulder = landmarks[PL.LEFT_SHOULDER]
        right_shoulder = landmarks[PL.RIGHT_SHOULDER]
        left_elbow = landmarks[PL.LEFT_ELBOW]
        right_elbow = landmarks[PL.RIGHT_ELBOW]
        left_wrist = landmarks[PL.LEFT_WRIST]
        right_wrist = landmarks[PL.RIGHT_WRIST]

        left_elbow_angle = self.calc_angle(
            left_shoulder.x, left_shoulder.y,
            left_elbow.x, left_elbow.y,
            left_wrist.x, left_wrist.y
        )

        right_elbow_angle = self.calc_angle(
            right_shoulder.x, right_shoulder.y,
            right_elbow.x, right_elbow.y,
            right_wrist.x, right_wrist.y
        )

        return left_elbow_angle, right_elbow_angle

    def calc_angle(self, p1x, p1y, p2x, p2y, p3x, p3y):
        return (math.atan2(p3y-p2y, p3x-p2x) - math.atan2(p1y-p2y, p1x-p2x))*(180/math.pi)

    def release(self):
        self.cap.release()
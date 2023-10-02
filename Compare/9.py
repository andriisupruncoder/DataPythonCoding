import cv2
import numpy as np
import time
import RPi.GPIO as GPIO

# Define the servo pins
SERVO_PIN_PITCH = 18
SERVO_PIN_YAW = 23

# Define the servo angles
SERVO_MIN_ANGLE = 0
SERVO_MAX_ANGLE = 180

# Initialize the servos
GPIO.setmode(GPIO.BOARD)
GPIO.setup(SERVO_PIN_PITCH, GPIO.OUT)
GPIO.setup(SERVO_PIN_YAW, GPIO.OUT)

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Define the body part to track
body_part = "hand"

# Create a tracker
tracker = cv2.TrackerCSRT_create()

# Start tracking
while True:
    # Capture a frame
    ret, frame = cap.read()

    # Find the body part
    bounding_box = tracker.update(frame)

    # Get the center of the bounding box
    center = (int(bounding_box[0] + bounding_box[2] / 2), int(bounding_box[1] + bounding_box[3] / 2))

    # Calculate the servo angles
    pitch_angle = np.interp(center[0], (0, frame.shape[1]), (SERVO_MIN_ANGLE, SERVO_MAX_ANGLE))
    yaw_angle = np.interp(center[1], (0, frame.shape[0]), (SERVO_MIN_ANGLE, SERVO_MAX_ANGLE))

    # Set the servo angles
    GPIO.output(SERVO_PIN_PITCH, pitch_angle)
    GPIO.output(SERVO_PIN_YAW, yaw_angle)

    # Display the frame
    cv2.imshow("Tracking", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close the webcam
cap.release()

# Close the servos
GPIO.cleanup()
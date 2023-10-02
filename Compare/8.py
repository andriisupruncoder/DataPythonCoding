import cv2
import numpy as np
import RPi.GPIO as GPIO

# Set up the servos
servo_pin_pitch = 18
servo_pin_yaw = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin_pitch, GPIO.OUT)
GPIO.setup(servo_pin_yaw, GPIO.OUT)

# Initialize the servos
servo_pitch = GPIO.PWM(servo_pin_pitch, 50)
servo_yaw = GPIO.PWM(servo_pin_yaw, 50)
servo_pitch.start(7.5)
servo_yaw.start(7.5)

# Load the OpenCV Haar cascade for detecting human body parts
cascade = cv2.CascadeClassifier("haarcascade_fullbody.xml")

# Start the video capture
cap = cv2.VideoCapture(0)

# Loop forever
while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect human body parts in the frame
    body_parts = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # If at least one body part is detected
    if len(body_parts) > 0:
        # Find the largest body part
        largest_body_part = max(body_parts, key=lambda x: x[3])

        # Calculate the center of the largest body part
        center_x = int(largest_body_part[0] + largest_body_part[2] / 2)
        center_y = int(largest_body_part[1] + largest_body_part[3] / 2)

        # Move the servos to center the largest body part in the frame
        servo_pitch.ChangeDutyCycle(center_x / 640.0 * 10 + 7.5)
        servo_yaw.ChangeDutyCycle(center_y / 480.0 * 10 + 7.5)

    # Display the frame
    cv2.imshow("Frame", frame)

    # Wait for a key press
    key = cv2.waitKey(1) & 0xFF

    # If the 'q' key is pressed, break out of the loop
    if key == ord("q"):
        break

# Close the video capture
cap.release()

# Close the servos
servo_pitch.stop()
servo_yaw.stop()

# Close GPIO
GPIO.cleanup()
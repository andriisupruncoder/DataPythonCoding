Sure, here is how you can make a CCTV camera management app using Python:

1. **Install the necessary libraries.**

```
pip install opencv-python
pip install numpy
```

2. **Import the necessary modules.**

```
import cv2
import numpy as np
```

3. **Create a class to represent a CCTV camera.**

```
class CCTVCamera:
    def __init__(self, name, ip_address, port):
        self.name = name
        self.ip_address = ip_address
        self.port = port

    def get_frame(self):
        # Connect to the camera.
        cap = cv2.VideoCapture(self.ip_address + ":" + str(self.port))

        # Get a frame from the camera.
        ret, frame = cap.read()

        # Return the frame.
        return frame
```

4. **Create a function to display a CCTV camera frame.**

```
def display_frame(frame):
    # Convert the frame to RGB.
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Display the frame.
    cv2.imshow("CCTV Camera", frame)
    cv2.waitKey(1)
```

5. **Create a function to manage a CCTV camera.**

```
def manage_camera(camera):
    # Get a frame from the camera.
    frame = camera.get_frame()

    # Display the frame.
    display_frame(frame)
```

6. **Create a list of CCTV cameras.**

```
cameras = [
    CCTVCamera("Camera 1", "192.168.1.100", 8080),
    CCTVCamera("Camera 2", "192.168.1.101", 8081),
]
```

7. **Iterate through the list of cameras and manage each camera.**

```
for camera in cameras:
    manage_camera(camera)
```

8. **Keep the program running until the user presses the "q" key.**

```
while True:
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
```

Once you have completed these steps, you will have created a CCTV camera management app using Python.

Here are some additional resources that you may find helpful:

* [OpenCV Python Tutorial](https://opencv-python-tutroals.readthedocs.io/en/latest/)
* [NumPy Tutorial](https://numpy.org/doc/stable/user/tutorial.html)

I hope this helps! Let me know if you have any other questions.
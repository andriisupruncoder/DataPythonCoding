import cv2
import numpy as np
import tensorflow as tf

from yolo import YOLOv4Tiny


class VideoPeopleCounter:
    def __init__(self, model_path, labels_path, input_size=416):
        self.model = YOLOv4Tiny(model_path, labels_path, input_size)
        self.classes = self.model.classes
        self.genders = ["male", "female"]
        self.ages = ["child", "youth", "middle-aged", "old"]

    def detect_people(self, frame):
        boxes, scores, classes, nums = self.model.predict(frame)
        people = []
        for i in range(nums[0]):
            if classes[0][i] == self.classes.index("person"):
                person = {
                    "box": boxes[0][i],
                    "score": scores[0][i],
                    "class": classes[0][i],
                    "gender": self.genders[int(classes[1][i])],
                    "age": self.ages[int(classes[2][i])],
                }
                people.append(person)
        return people

    def count_people(self, people):
        return len(people)

    def recognize_gender(self, people):
        genders = []
        for person in people:
            genders.append(person["gender"])
        return genders

    def recognize_age(self, people):
        ages = []
        for person in people:
            ages.append(person["age"])
        return ages


def main():
    model_path = "path/to/yolov4-tiny.weights"
    labels_path = "path/to/coco.names"
    counter = VideoPeopleCounter(model_path, labels_path)

    cap = cv2.VideoCapture("path/to/video.mp4")
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        people = counter.detect_people(frame)
        count = counter.count_people(people)
        genders = counter.recognize_gender(people)
        ages = counter.recognize_age(people)

        print("People count:", count)
        print("Genders:", genders)
        print("Ages:", ages)

        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
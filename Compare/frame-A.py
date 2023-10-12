import cv2
import os

def extract_frames(video_path, output_path, interval=1):
    """
    Extracts frames from a video file at the given interval.

    Args:
        video_path: The path to the video file.
        output_path: The path to the output folder.
        interval: The interval between frames, in seconds.

    Returns:
        The number of frames extracted.
    """

    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    frame_num = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if frame_num % interval == 0:
            output_filename = os.path.join(output_path, f"frame_{frame_num:06d}.jpg")
            cv2.imwrite(output_filename, frame)

        frame_num += 1

    cap.release()
    return frame_count


def main():
    video_folder = "./folder"
    output_folder = "./folder"

    for video_filename in os.listdir(video_folder):
        video_path = os.path.join(video_folder, video_filename)
        frame_count = extract_frames(video_path, output_folder)
        print(f"Extracted {frame_count} frames from {video_filename}.")


if __name__ == "__main__":
    main()
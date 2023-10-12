import torch
from ultralytics import YOLO

# Initialize YOLO object with pre-trained weights
model = YOLO("yolov8n.pt")

# Save model to specific path
torch.save(model.state_dict(), "/path/to/model.pt")
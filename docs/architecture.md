# System Architecture

## Overview

The project is built on the ROS2 framework and integrates YOLOv8 with OpenCV for real-time object detection. Images are received from a camera topic, processed by the detection node, and republished as annotated images.

---

## Architecture Diagram

```text
+------------------+
|   USB Camera     |
+------------------+
         |
         v
+------------------+
|  /image_raw      |
+------------------+
         |
         v
+---------------------------+
| YOLO Detector Node        |
|---------------------------|
| - Image Subscriber        |
| - YOLOv8 Inference        |
| - Result Visualization    |
| - Image Publisher         |
+---------------------------+
         |
         v
+-------------------------+
| /yolo/image_annotated   |
+-------------------------+
         |
         v
+------------------+
| rqt_image_view   |
+------------------+
```

---

## Software Components

### ROS2

Responsible for communication between nodes using topics.

### OpenCV

Used for image processing and visualization.

### YOLOv8

Performs object detection and returns bounding boxes, class IDs, and confidence scores.

### cv_bridge

Converts ROS image messages to OpenCV images and vice versa.

---

## Data Flow

```text
Camera
   │
   ▼
ROS Image Message
   │
   ▼
cv_bridge
   │
   ▼
OpenCV Image
   │
   ▼
YOLOv8 Inference
   │
   ▼
Detection Results
   │
   ▼
Bounding Box Rendering
   │
   ▼
ROS Image Publisher
```

---

## Project Structure

```text
my_yolo_detector/

├── __init__.py
├── utils.py
└── yolo_detector_node.py
```

---

## ROS2 Topics

| Topic | Type | Description |
|-------|------|-------------|
| /image_raw | sensor_msgs/Image | Input camera image |
| /yolo/image_annotated | sensor_msgs/Image | Detection result image |

---

## Future Extensions

- Custom ROS2 messages
- Multi-object tracking
- ONNX deployment
- TensorRT acceleration
- Depth camera support
- Multi-camera systems
- Robotic manipulation integration
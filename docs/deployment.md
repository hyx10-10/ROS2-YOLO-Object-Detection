# Deployment Guide

## Overview

This project supports deployment on ROS2-based robotic platforms using a USB camera and a YOLOv8 model for real-time object detection.

---

## Deployment Requirements

### Hardware

- PC or Embedded Linux Device
- USB Camera
- CPU or NVIDIA GPU (Optional)

### Software

- Ubuntu 22.04
- ROS2 Humble
- Python 3.10+
- OpenCV 4.x
- Ultralytics YOLOv8

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Build the ROS2 Workspace

```bash
cd ~/dev_ws

colcon build --symlink-install

source install/setup.bash
```

---

## Prepare the Model

Place the trained model into the following directory:

```text
models/
└── yolov8n.pt
```

Or replace it with your own trained model:

```text
best.pt
```

Update the configuration file if necessary:

```text
config/yolo.yaml
```

---

## Launch the Camera

```bash
ros2 run usb_cam usb_cam_node_exe
```

---

## Launch the Detector

```bash
ros2 launch my_yolo_detector yolo_detector.launch.py
```

---

## Visualize the Results

```bash
ros2 run rqt_image_view rqt_image_view
```

Select the topic:

```text
/yolo/image_annotated
```

---

## Project Workflow

```text
USB Camera
      │
      ▼
ROS2 Image Topic
      │
      ▼
YOLO Detector
      │
      ▼
Detection Results
      │
      ▼
Annotated Image
```

---

## Notes

- Make sure the model path is correct.
- Verify the camera topic before launching the detector.
- Ensure all ROS2 dependencies are installed.
- Use GPU acceleration when available for better performance.
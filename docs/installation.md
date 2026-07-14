# Installation Guide

## System Requirements

- Ubuntu 22.04
- ROS2 Humble
- Python 3.10+
- OpenCV 4.x

---

## Clone the Repository

```bash
git clone https://github.com/hyx10-10/ROS2-YOLO-Object-Detection.git
```

```bash
cd ROS2-YOLO-Object-Detection
```

---

## Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

## Install ROS2 Dependencies

```bash
sudo apt update

sudo apt install ros-humble-cv-bridge

sudo apt install ros-humble-image-transport

sudo apt install ros-humble-sensor-msgs
```

---

## Build the Workspace

```bash
cd ~/dev_ws

colcon build --symlink-install

source install/setup.bash
```

---

## Run

### Terminal 1

```bash
ros2 run usb_cam usb_cam_node_exe
```

### Terminal 2

```bash
ros2 run my_yolo_detector yolo_detector_node
```

### Terminal 3

```bash
ros2 run rqt_image_view rqt_image_view
```

Select:

```
/yolo/image_annotated
```

to view the detection results.
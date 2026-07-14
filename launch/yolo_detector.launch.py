from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription(
        [
            Node(
                package="my_yolo_detector",
                executable="yolo_detector_node",
                name="yolo_detector",
                output="screen",
                parameters=[
                    {
                        "model_path": "models/yolov8n.pt",
                        "confidence_threshold": 0.5,
                        "image_topic": "/image_raw",
                        "output_topic": "/yolo/image_annotated",
                    }
                ],
            )
        ]
    )
import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
from cv_bridge import CvBridge

from ultralytics import YOLO

from .utils import draw_detections


class YOLODetectorNode(Node):

    def __init__(self):
        super().__init__("yolo_detector")

        self.declare_parameter("model_path", "models/yolov8n.pt")
        self.declare_parameter("confidence_threshold", 0.5)
        self.declare_parameter("image_topic", "/image_raw")
        self.declare_parameter("output_topic", "/yolo/image_annotated")

        model_path = self.get_parameter(
            "model_path"
        ).get_parameter_value().string_value

        self.confidence = self.get_parameter(
            "confidence_threshold"
        ).get_parameter_value().double_value

        image_topic = self.get_parameter(
            "image_topic"
        ).get_parameter_value().string_value

        output_topic = self.get_parameter(
            "output_topic"
        ).get_parameter_value().string_value

        self.bridge = CvBridge()

        self.model = YOLO(model_path)

        self.subscription = self.create_subscription(
            Image,
            image_topic,
            self.image_callback,
            10,
        )

        self.publisher = self.create_publisher(
            Image,
            output_topic,
            10,
        )

        self.get_logger().info("YOLO Detector Node Started.")

    def image_callback(self, msg):
        frame = self.bridge.imgmsg_to_cv2(
            msg,
            desired_encoding="bgr8",
        )

        results = self.model(
            frame,
            conf=self.confidence,
            verbose=False,
        )

        annotated = draw_detections(frame, results)

        image_msg = self.bridge.cv2_to_imgmsg(
            annotated,
            encoding="bgr8",
        )

        self.publisher.publish(image_msg)


def main(args=None):
    rclpy.init(args=args)

    node = YOLODetectorNode()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()
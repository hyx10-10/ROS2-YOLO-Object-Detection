from setuptools import setup

package_name = "my_yolo_detector"

setup(
    name=package_name,
    version="1.0.0",
    packages=[package_name],
    data_files=[
        (
            "share/ament_index/resource_index/packages",
            ["resource/" + package_name],
        ),
        (
            "share/" + package_name,
            ["package.xml"],
        ),
        (
            "share/" + package_name + "/launch",
            ["launch/yolo_detector.launch.py"],
        ),
        (
            "share/" + package_name + "/config",
            [
                "config/yolo.yaml",
                "config/camera.yaml",
            ],
        ),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="hyx10-10",
    maintainer_email="1822108575@qq.com",
    description="ROS2 Humble object detection package based on YOLOv8 and OpenCV.",
    license="MIT",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "yolo_detector_node = my_yolo_detector.yolo_detector_node:main",
        ],
    },
)
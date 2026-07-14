import unittest

from my_yolo_detector.utils import draw_detections


class TestYOLODetector(unittest.TestCase):

    def test_draw_detections_function_exists(self):
        self.assertTrue(callable(draw_detections))

    def test_module_import(self):
        self.assertIsNotNone(draw_detections)


if __name__ == "__main__":
    unittest.main()
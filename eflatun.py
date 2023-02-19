import jetson.inference
import jetson.utils
import time

import rclpy  #ROS2 Python kütüphanesi
from rclpy.node import Node  #ROS2'nin Node objesi
from sensor_msgs.msg import Image  #Sensör mesajlarından istenen obje veya objeler
from vision_msgs.msg import Detection2D, Detection2DArray, BoundingBox2D, ObjectHypothesisWithPose  #Görüntü mesajlarından istenen obje veya objeler
from geometry_msgs.msg import Pose2D  #Geometri mesajlarından istenen obje veya objeler

import time  #Süre ölçme ve uyku işlemleri için time kütüphanesi
import cv2  #CPU üzerinde daha komplex görüntü işleme işlemleri OpenCV kütüphanesi
import numpy as np  #NumPY kütüphanesi

NAMESPACE = "camera"  #Bu Nod için kullanılacak isim uzayı
NODENAME = "all_detections"  #Bu Nod için kullanılacak isim
DETECTION_PUBLISHERNAME = "detections"  #Model tespitlerinin paylaşılacağı başlığın ismi

VIDEO_WIDTH = 1920
VIDEO_HEIGHT = 1080

COLOR_RED = (255, 0, 0, 255)
THICK = 2

MARGIN_WIDTH = VIDEO_WIDTH // 4
MARGIN_HEIGHT = VIDEO_HEIGHT // 10

RTP_IP = "rtp://192.168.1.2:1234"
DETECTION_MODEL_PATH = "/home/fener/fener_vehicle/src/Fener-Vehicle-Repo-v2/fener_package_v2/ssd-mobilenet.onnx"
LABELS_PATH = "/home/fener/fener_vehicle/src/Fener-Vehicle-Repo-v2/fener_package_v2/labels.txt"


class JetsonDetector(Node):
    def __init__(self):
        super().__init__(NODENAME, namespace=NAMESPACE)

        self.get_logger().info("Initializing...")

        self.plane_detection_model = jetson.inference.detectNet(
            "ssd-mobilenet-v2",
            threshold=0.5,
            #argv=[
            #    '--model=' + DETECTION_MODEL_PATH, '--labels=' + LABELS_PATH,
            #    '--input-blob=input_0', '--output-cvg=scores',
            #    '--output-bbox=boxes'
            #]
        )

        self.logitech_webcam = jetson.utils.videoSource(
            "v4l2:///dev/video0",
            argv=[
                f"--input-width={VIDEO_WIDTH}", f"--input-height={VIDEO_HEIGHT}"
            ]
        )

        self.rtp_stream_output = jetson.utils.videoOutput(
            RTP_IP, argv=["--headless", "--bitrate=4000000"]
        )

        self.video_file_output = jetson.utils.videoOutput(
            "video_log.mp4", argv=["--headless"]
        )

        self.detections_publisher = self.create_publisher(
            Detection2DArray, "logitech_webcam/all_detections", 2
        )

        self.create_timer(1 / 30, self.detect_objects)
        self.create_timer(1 / 30, self.stream_frame)

        self.get_logger().info("Detection and stream node has been created")

    def get_frame(self):
        self.frame = self.logitech_webcam.Capture()

    def detect_objects(self):
        self.get_frame()

        detections_msg = Detection2DArray()
        detections_msg.header.frame_id = "logitech_webcam"
        detections_msg.header.stamp = self.get_clock().now().to_msg()

        self.detections = self.plane_detection_model.Detect(
            self.frame, overlay="none"
        )

        for single_detection in self.detections:
            detection2D_msg = Detection2D()
            detection2D_msg.header.frame_id = "logitech_webcam"
            detection2D_msg.header.stamp = self.get_clock().now().to_msg()

            results = ObjectHypothesisWithPose()
            results.id = str(single_detection.ClassID)
            results.score = single_detection.Confidence

            center = Pose2D()
            center.x = single_detection.Center[0]
            center.y = single_detection.Center[1]
            center.theta = 0.0

            bbox = BoundingBox2D()
            bbox.center = center
            bbox.size_x = single_detection.Width
            bbox.size_y = single_detection.Height

            detection2D_msg.results.append(results)
            detection2D_msg.bbox = bbox

            detections_msg.detections.append(detection2D_msg)

        self.detections_publisher.publish(detections_msg)

    def stream_frame(self):

        for object in self.detections:

            x1 = object.Left
            x2 = object.Right
            y1 = object.Top
            y2 = object.Bottom

            jetson.utils.cudaDrawLine(
                self.frame, (x1, y1), (x2, y1), COLOR_RED, THICK
            )
            jetson.utils.cudaDrawLine(
                self.frame, (x1, y1), (x1, y2), COLOR_RED, THICK
            )
            jetson.utils.cudaDrawLine(
                self.frame, (x1, y2), (x2, y2), COLOR_RED, THICK
            )
            jetson.utils.cudaDrawLine(
                self.frame, (x2, y1), (x2, y2), COLOR_RED, THICK
            )

        self.rtp_stream_output.Render(self.frame)
        self.video_file_output.Render(self.frame)


def main(args=None):
    rclpy.init(args=args)
    node = JetsonDetector()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()

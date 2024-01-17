import cv2
import numpy as np


class UdpReceiveParser:

    def __init__(self):
        self.parse_result_listener = None
        self.frame_buffer = bytearray(102400)
        self.frame_id = 0
        self.pkg_num = 0
        self.head_data = None

    def display_image(self, data):
        image_np = np.frombuffer(data, dtype=np.uint8)
        image_np = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
        cv2.imshow('Image', image_np)


    def parse(self, b_arr):
        try:
            if len(self.frame_buffer) > 101376 or self.frame_id != b_arr[0]:
                self.frame_buffer.clear()
                self.pkg_num = 0

            self.pkg_num += 1
            self.frame_id = b_arr[0]
            z = b_arr[1] == 1
            self.frame_buffer.extend(b_arr[4:])

            if z and b_arr[2] == self.pkg_num:
                self.display_image(self.frame_buffer)

        except Exception as e:
            print(str(e))
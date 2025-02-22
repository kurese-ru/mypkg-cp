# SPDX-FileCopyrightText: 2024 Hiroto Yasuhara
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class BpmPublisher(Node):
    def __init__(self):
        super().__init__('bpm_publisher')
        self.publisher_ = self.create_publisher(String, 'bpm_info', 10)
        self.timer_ = self.create_timer(1.0, self.timer_callback)
        self.current_bpm = 60

    def timer_callback(self):
        beats_per_second = self.current_bpm / 60.0
        msg = String()
        msg.data = f'BPM: {self.current_bpm}, Beats per second: {beats_per_second:.2f}'
        self.publisher_.publish(msg)
        self.current_bpm += 1
        if self.current_bpm > 200:
            self.current_bpm = 60


def main():
    rclpy.init()
    node = BpmPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

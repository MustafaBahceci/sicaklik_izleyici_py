import random

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class Sensor(Node):
    def __init__(self):
        super().__init__('sensor')

        self.publisher_ = self.create_publisher(Float32, '/sicaklik', 10)
        self.timer = self.create_timer(1.0, self.sicaklik_yayinla)

    def sicaklik_yayinla(self):
        sicaklik = random.uniform(20.0, 40.0)

        mesaj = Float32()
        mesaj.data = sicaklik

        self.publisher_.publish(mesaj)
        self.get_logger().info(
            f'Yayınlanan sıcaklık: {sicaklik:.2f} °C'
        )


def main(args=None):
    rclpy.init(args=args)
    sensor = Sensor()

    try:
        rclpy.spin(sensor)
    except KeyboardInterrupt:
        pass
    finally:
        sensor.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class Izleyici(Node):
    def __init__(self):
        super().__init__('izleyici')

        self.esik_degeri = 30.0

        self.subscription = self.create_subscription(
            Float32,
            '/sicaklik',
            self.sicaklik_kontrol,
            10
        )

    def sicaklik_kontrol(self, mesaj):
        sicaklik = mesaj.data

        self.get_logger().info(
            f'Ölçülen sıcaklık: {sicaklik:.2f} °C'
        )

        if sicaklik > self.esik_degeri:
            self.get_logger().warning(
                f'UYARI! Sıcaklık {self.esik_degeri} °C sınırını aştı!'
            )


def main(args=None):
    rclpy.init(args=args)
    izleyici = Izleyici()

    try:
        rclpy.spin(izleyici)
    except KeyboardInterrupt:
        pass
    finally:
        izleyici.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from tf_transformations import euler_from_quaternion

from time import sleep

class TurtleController(Node):
    def __init__(self):
        # Inicializa o nó de subscrição 
        super().__init__("turtlecontroller")
        self.pose_subscription = self.create_subscription(
            msg_type=Odometry,
            topic='/odom',
            callback=self.pose_callback,
            qos_profile=10
        )
       
    def pose_callback(self, msg):
        # Extrai a posição e orientação do robô
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        z = msg.pose.pose.position.z
        ang = msg.pose.pose.orientation
        # Converte o quaternion para ângulos de Euler
        _, _, theta = euler_from_quaternion([ang.x, ang.y, ang.z, ang.w])
        sleep(3)
        # Imprime a posição e orientação do robô no terminal
        self.get_logger().info(f"x={x}, y={y}, theta={theta}")

    
def main(args=None):
    rclpy.init(args=args)
    turtle_controller = TurtleController()
    rclpy.spin(turtle_controller)
    turtle_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

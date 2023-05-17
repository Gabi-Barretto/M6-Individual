#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from collections import deque
from nav_msgs.msg import Odometry
from tf_transformations import euler_from_quaternion
from time import sleep
import random

queue = deque()

class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer_ = self.create_timer(1, self.move_turtle)
        self.twist_msg_ = Twist()
        self.angle_ = 0
        self.direction_ = 1
        self.pose_subscription = self.create_subscription(
            msg_type=Odometry,
            topic='/odom',
            callback=self.pose_callback,
            qos_profile=10
        )

    def move_turtle(self):
        queue.append(random.randint(3, 9))
        self.twist_msg_.linear.x = queue
        self.twist_msg_.angular.z = 1.0
        self.publisher_.publish(self.twist_msg_)
        queue.popleft()


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
    rclpy.init()
    turtle_controller = TurtleController()
    rclpy.spin(turtle_controller)
    turtle_controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

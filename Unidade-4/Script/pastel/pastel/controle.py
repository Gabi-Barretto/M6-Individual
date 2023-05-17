#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from collections import deque
from nav_msgs.msg import Odometry
from tf_transformations import euler_from_quaternion
from time import sleep
import random
import math
import csv

queue = deque()

class TurtleController(Node):
    def __init__(self, control_period=0.2):
        super().__init__('nodo_controle')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.twist_msg_ = Twist()
        self.position = None
        self.pose = None
        self.setpoint = None
        self.pose_subscription = self.create_subscription(
            msg_type=Odometry,
            topic='/odom',
            callback=self.pose_callback,
            qos_profile=10
        )
        self.control_timer = self.create_timer(
                timer_period_sec=control_period,
                callback=self.control_callback
        )

    def pose_callback(self, msg):
        # Extrai a posição e orientação do robô
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        z = msg.pose.pose.position.z
        self.position = [x, y]
        ang = msg.pose.pose.orientation
        # Converte o quaternion para ângulos de Euler
        _, _, theta = euler_from_quaternion([ang.x, ang.y, ang.z, ang.w])
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

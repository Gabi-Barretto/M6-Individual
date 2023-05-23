import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point, Twist
from nav_msgs.msg import Odometry
from tf_transformations import euler_from_quaternion
from math import atan2
from collections import deque
from time import sleep
import math


class TurtleBotController(Node):
    def __init__(self):
        super().__init__('turtlebot_controller')
        self.goal_position = deque()
        
        self.odom_subscriber = self.create_subscription(
            Odometry,
            '/odom',
            self.odom_callback,
            10
        )
        self.current_position = [0, 0, 0]

       
        self.velocity_publisher = self.create_publisher(Twist, 'cmd_vel', 10)

        # inicializando a fila de pontos
        self.goal_position.append(Point(x=10.0, y=10.0))
    

    def odom_callback(self, msg):
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        ang = msg.pose.pose.orientation
        # Converte o quaternion para ângulos de Euler
        _, _, theta = euler_from_quaternion([ang.x, ang.y, ang.z, ang.w])
        
        self.current_position = (x, y, theta)
        self.get_logger().info(f"x={x}, y={y}, theta={theta}")

    def distance(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    def move_to_next_point(self):
        next_point = self.goal_position.popleft()
        self.get_logger().info(f"next_point: {next_point}")
        goal_x = next_point.x
        goal_y = next_point.y
        while self.distance(self.current_position[0], self.current_position[1], goal_x, goal_y) > 0.5:
            x_start, y_start, theta_start = self.current_position
            x_goal, y_goal = goal_x, goal_y
            theta_goal = atan2(y_goal - y_start, x_goal - x_start)
            twist = Twist()
            twist.linear.x = 1.0
            twist.angular.z = 0.3 * (theta_goal - theta_start)
            self.velocity_publisher.publish(twist)
            sleep(0.3)
            rclpy.spin_once(self)

        twist = Twist()
        twist.linear.x = 0.0
        twist.angular.z = 0.0
        self.velocity_publisher.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    controller = TurtleBotController()
    controller.move_to_next_point()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

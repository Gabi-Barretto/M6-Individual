#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math
import time



class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.timer_ = self.create_timer(1, self.move_turtle)
        self.twist_msg_ = Twist()
        self.angle_ = 0
        self.direction_ = 1

    def move_turtle(self):

        self.twist_msg_.linear.x = 2.0
        self.twist_msg_.linear.y = 0.0
        self.publisher_.publish(self.twist_msg_)
        time.sleep(2) 
        self.twist_msg_.linear.x = -1.5
        self.twist_msg_.linear.y = -1.0
        self.publisher_.publish(self.twist_msg_)
        time.sleep(2)      
        self.twist_msg_.linear.x = 0.5
        self.twist_msg_.linear.y = 1.5
        self.publisher_.publish(self.twist_msg_)
        time.sleep(2)
        self.twist_msg_.linear.x = 0.5
        self.twist_msg_.linear.y = -1.5
        self.publisher_.publish(self.twist_msg_)
        time.sleep(2)   
        self.twist_msg_.linear.x = -1.5
        self.twist_msg_.linear.y = 1.0
        self.publisher_.publish(self.twist_msg_)
        time.sleep(2)   
        

      

def main(args=None):
    rclpy.init()
    turtle_controller = TurtleController()
    rclpy.spin(turtle_controller)
    turtle_controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

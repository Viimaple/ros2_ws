import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Listener(Node):
    def __init__(self):
        super().__init__('listener')

        self.subscription = self.create_subscription(
            Int16,              
            'countup',          
            self.listener_callback,  
            10                   
        )
        self.subscription
    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%d"' % msg.data)

def main():
    rclpy.init()
    node = Listener()
    rclpy.spin(node)

import rclpy
from rclpy.node import Node
from person_msgs.msg import Person

rclpy.init()
node = Node("listener")

def cb(msg):
    node.get_logger().info("Received time zone info: %s" % msg.name)

def main():
    node.create_subscription(Person, "person", cb, 10)
    rclpy.spin(node)


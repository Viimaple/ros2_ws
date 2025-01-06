import rclpy
from rclpy.node import Node
from person_msgs.msg import Person
import pytz
from datetime import datetime

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Person, "person", 10)

def cd():
    msg = Person()

    tz = pytz.timezone("Asia/Tokyo")
    
    current_time = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
    
    utc_offset = tz.utcoffset(datetime.now()).total_seconds() / 3600
    utc_offset_str = f"UTC{'+' if utc_offset >= 0 else '-'}{abs(int(utc_offset))}"

    msg.name = f"JST: {utc_offset_str}"

    pub.publish(msg)

def main():
    node.create_timer(1.0, cd)
    rclpy.spin(node)


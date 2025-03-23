import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32


class ExamplePublisherClass(Node):
    def __init__(self):
        super().__init__("example_publisher_node")
        self.pub = self.create_publisher(Int32, "integer", 10)
        self.timer = self.create_timer(1.0, self.publish_msg)
        self.msg = Int32()
        
    def publish_msg(self):
        self.msg.data += 1
        self.pub.publish(self.msg)
        
    
        
def main():
    rclpy.init()
    
    node = ExamplePublisherClass()
    
    rclpy.spin(node)
        
if __name__ == '__main__':
    main()
    



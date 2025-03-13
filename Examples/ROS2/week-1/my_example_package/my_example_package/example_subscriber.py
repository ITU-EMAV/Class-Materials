import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32


class ExampleSubcriberClass(Node):
    def __init__(self):
        super().__init__("example_subscriber_node")
        subs = self.create_subscription(Int32, "integer", self.subs_callback, 10)
        
        
    def subs_callback(self, msg: Int32):
        print(f"Received msg: {msg.data}")
        
    
        
def main():
    rclpy.init()
    
    node = ExampleSubcriberClass()
    
    rclpy.spin(node)
        
if __name__ == '__main__':
    main()
    



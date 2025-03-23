from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_example_package',
            executable='example_publisher',
            name='publisher'
        ),
        Node(
            package='my_example_package',
            executable='example_subscriber',
            name='sim'
        )

    ])
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='package_name',
            executable='gui_node.py',
            name='gui_node'
        ),
        Node(
            package='package_name',
            executable='gui_pickup_node.py',
            name='gui_pickup_node'
        )
    ])

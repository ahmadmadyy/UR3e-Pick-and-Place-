from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    approach_retreat_node = Node(
        package='moveit2_scripts',
        executable='approach_retreat_trajectory',
        name='approach_retreat_trajectory',
        output='screen',
        parameters=[{
            # MoveIt normally gets these from move_group / launch system
            # Leave empty unless you explicitly override parameters
        }]
    )

    return LaunchDescription([
        approach_retreat_node
    ])

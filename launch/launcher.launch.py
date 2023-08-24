import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription


def generate_launch_description():
    launch_dir = os.path.join(get_package_share_directory("ipb_car_launch"), "launch")
    lidars_launch = IncludeLaunchDescription(os.path.join(launch_dir, "lidars.launch.py"))
    cameras_launch = IncludeLaunchDescription(os.path.join(launch_dir, "cameras.launch.py"))
    return LaunchDescription(
        [
            cameras_launch,
            lidars_launch,
        ]
    )

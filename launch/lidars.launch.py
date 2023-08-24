import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution


def generate_launch_description():
    share_config = os.path.join(get_package_share_directory("ipb_car_launch"), "config")
    lidar_hor_params = PathJoinSubstitution([share_config, "lidar_hor_params.yaml"])
    lidar_ver_params = PathJoinSubstitution([share_config, "lidar_ver_params.yaml"])
    ouster_ros_launch = os.path.join(
        get_package_share_directory("ouster_ros"),
        "launch",
        "driver.launch.py",
    )
    horizontal_lidar = IncludeLaunchDescription(
        launch_description_source=PythonLaunchDescriptionSource(ouster_ros_launch),
        launch_arguments={
            "params_file": lidar_hor_params,
            "ouster_ns": "os_h",
            "viz": "False",
        }.items(),
    )
    vertical_lidar = IncludeLaunchDescription(
        launch_description_source=PythonLaunchDescriptionSource(ouster_ros_launch),
        launch_arguments={
            "params_file": lidar_ver_params,
            "ouster_ns": "os_v",
            "viz": "False",
        }.items(),
    )
    return LaunchDescription(
        [
            horizontal_lidar,
            vertical_lidar,
        ]
    )

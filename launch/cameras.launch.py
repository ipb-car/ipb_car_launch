import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution


def generate_launch_description():
    share_config = os.path.join(get_package_share_directory("ipb_car_launch"), "config")
    cam_front_params = PathJoinSubstitution([share_config, "cam_front.yaml"])
    cam_left_params = PathJoinSubstitution([share_config, "cam_left.yaml"])
    cam_rear_params = PathJoinSubstitution([share_config, "cam_rear.yaml"])
    cam_right_params = PathJoinSubstitution([share_config, "cam_right.yaml"])
    pylon_ros2_launch = os.path.join(
        get_package_share_directory("pylon_ros2_camera_wrapper"),
        "launch",
        "pylon_ros2_camera.launch.py",
    )
    cam_front = IncludeLaunchDescription(
        launch_description_source=PythonLaunchDescriptionSource(pylon_ros2_launch),
        launch_arguments={
            "config_file": cam_front_params,
            "node_name": "cam_front",  # node name
            "camera_id": "cameras",  # namespace
        }.items(),
    )
    cam_left = IncludeLaunchDescription(
        launch_description_source=PythonLaunchDescriptionSource(pylon_ros2_launch),
        launch_arguments={
            "config_file": cam_left_params,
            "node_name": "cam_left",
            "camera_id": "cameras",  # namespace
        }.items(),
    )
    cam_rear = IncludeLaunchDescription(
        launch_description_source=PythonLaunchDescriptionSource(pylon_ros2_launch),
        launch_arguments={
            "config_file": cam_rear_params,
            "node_name": "cam_rear",
            "camera_id": "cameras",  # namespace
        }.items(),
    )
    cam_right = IncludeLaunchDescription(
        launch_description_source=PythonLaunchDescriptionSource(pylon_ros2_launch),
        launch_arguments={
            "config_file": cam_right_params,
            "node_name": "cam_right",
            "camera_id": "cameras",  # namespace
        }.items(),
    )

    return LaunchDescription(
        [
            cam_front,
            cam_left,
            cam_rear,
            cam_right,
        ]
    )

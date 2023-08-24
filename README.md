# ipb-car ROS launch files

This ros package gathers all the necessary stuff that you need to run the
ipb-car setup.

Additionally, we have a [monitor](scripts/monitor.py) script that
helps you to monitor sensor synchronization while recording data. In the near
future this watchdog might find its way to his own repository, but for now we
maintain it here.

## Installation and Launching the System
Use the [meta-workspace](https://gitlab.ipb.uni-bonn.de/ipb-team/robots/ipb-car/meta-workspace) to install, build and launch the system.


## List of ros nodes

You can check this by inspecting the launch files under [launch/](launch/)

## List of recorded topics

You can find the recorded topics under [launch/record.launch](launch/record.launch)

## Rviz

There is an extremely util [ipb_car.rviz](config/ipb_car.rviz) config file that
will help you visualize all the data at once in a clear way by just running:

```sh
rviz -d config/ipb_car.rviz
```

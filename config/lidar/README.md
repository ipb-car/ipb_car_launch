After migrating to the official ROS 1 node from Ouster we could not read this params with rosparam
anymore. Apparently params and args are very different monsters...

To avoid 5 days of debugging we copy-pasted the params to the new lidars.launch file and left this
here as reference. Hopefully on the future we can use this again.

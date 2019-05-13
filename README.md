Once the simulation is running, you must activate the mast for the camera.  This will raise the mast, and point the 
camera in the forward-facing direction.  Optionally, you can activate the robotic arm.  These are managed by a ROS service. 
To activate, open a Terminal window and invoke the following commands.  In Gazebo, you can witness the mast and arm activating.

`$ rosservice call /curiosity_mars_rover/mast_service "model_name: 'open'"`

`$ rosservice call /curiosity_mars_rover/arm_service "model_name: 'open'"`

In simulation, you can drive the rover using the `teleop_twist_keyboard` package.  To move the robot, run the following command
and follow the on-screen instructions.  Increase the speed of the robot to approximately 6 (press the 'q' key several times on your
keyboard to increase the robot speed).

`$ rosrun teleop_twist_keyboard teleop_twist_keyboard.py`

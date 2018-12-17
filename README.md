# COMP150 Reinforcement Learning: Path Planning Amidst Moving Obstacles

## Installation Guide ##
sudo apt install ros-kinetic-desktop-full

sudo apt install ros-kinetic-turtlebot ros-kinetic-turtlebot-gazebo ros-kinetic-turtlebot-apps ros-kinetic-turtlebot-rviz-launchers

sudo apt install ros-kinetic-octomap-msgs ros-kinetic-joy ros-kinetic-geodesy ros-kinetic-octomap-ros ros-kinetic-control-toolbox ros-kinetic-pluginlib ros-kinetic-trajectory-msgs ros-kinetic-control-msgs ros-kinetic-std-srvs ros-kinetic-nodelet ros-kinetic-urdf ros-kinetic-rviz ros-kinetic-kdl-conversions ros-kinetic-eigen-conversions ros-kinetic-tf2-sensor-msgs ros-kinetic-pcl-ros ros-kinetic-navigation cmake gcc g++ qt4-qmake libqt4-dev libusb-dev libftdi-dev python3-defusedxml python3-vcstool

sudo apt-get install ros-kinetic-gazebo8-ros-pkgs ros-kinetic-gazebo8-ros-control ros-kinetic-gazebo8*

sudo apt-get install ros-kinetic-ar-track-alvar-msgs

sudo apt-get install ros-kinetic-sophus

Go to [gym-gazebo]/gym_gazebo/envs/installation

Run bash setup_kinetic.bash

Create CATKIN_IGNORE empty file to joystick_drivers/spacenav_node/, joystick_drivers/wiimote/, and kobuki_desktop/kobuki_qtestsuite/ in [gym-gazebo]/gym_gazebo/envs/installation/catkin_ws/src/.

Run bash setup_kinetic.bash again
bash turtlebot_nn_setup.bash

Before running the python, make sure you do the following.
- Open gym-gazebo/gym_gazebo/envs/installation/catkin_ws/src/turtlebot_simulator/turtlebot_gazebo/launch/includes/kobuki.launch.xml
- In the file, edit line 6 from 

```
<arg name="urdf_file" default="$(find xacro)/xacro --inorder '$(find turtlebot_description)/robots/$(arg base)_$(arg stacks)_$(arg 3d_sensor).urdf.xacro'"/>
```
to
```
<arg name="urdf_file" default="$(find xacro)/xacro.py '$(find turtlebot_description)/robots/$(arg base)_$(arg stacks)_$(arg 3d_sensor).urdf.xacro'"/>
```
This should fix the Turtlebot error that occurs when running the python file.

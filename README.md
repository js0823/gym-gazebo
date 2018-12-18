# COMP150 Reinforcement Learning: Path Planning Amidst Moving Obstacles

## Installation Guide ##
Installation requires you do all the steps below.
```
sudo apt install ros-kinetic-desktop
sudo apt install ros-kinetic-octomap-msgs ros-kinetic-joy ros-kinetic-geodesy ros-kinetic-octomap-ros ros-kinetic-control-toolbox ros-kinetic-pluginlib ros-kinetic-trajectory-msgs ros-kinetic-control-msgs ros-kinetic-std-srvs ros-kinetic-nodelet ros-kinetic-urdf ros-kinetic-rviz ros-kinetic-kdl-conversions ros-kinetic-eigen-conversions ros-kinetic-tf2-sensor-msgs ros-kinetic-pcl-ros ros-kinetic-navigation cmake gcc g++ qt4-qmake libqt4-dev libusb-dev libftdi-dev python3-defusedxml python3-vcstool
sudo apt install gazebo8 ros-kinetic-gazebo8-ros-pkgs ros-kinetic-gazebo8-ros-control
sudo apt install ros-kinetic-ar-track-alvar-msgs
sudo apt install ros-kinetic-sophus
pip install opencv-python
pip install gym
pip install rospkg catkin_pkg
```
After the installation above are finished,
Go to [gym-gazebo]/gym_gazebo/envs/installation

Run 
```
bash setup_kinetic.bash
bash turtlebot_nn_setup.bash
```

After that, go back to the root of the gym-gazebo directory and run
```
sudo pip install -e .
```

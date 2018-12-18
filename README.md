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
Now add the following line to your ~/.bashrc file, at the end of the file:
```
source /opt/ros/kinetic/setup.bash
```

After the installation above are finished, download the project using this command on anywhere you want to download to:
```
git clone https://github.com/js0823/gym-gazebo.git
```
Now, go to [gym-gazebo]/gym_gazebo/envs/installation and run
```
bash setup_kinetic.bash
bash turtlebot_nn_setup.bash
```

After that, go back to the root of the gym-gazebo directory and run
```
sudo pip install -e .
```

At the end, you should see the similar to the following lines in your ~/.bashrc file.
```
source /opt/ros/kinetic/setup.bash
source [path_to_gym-gazebo]/gym-gazebo/gym_gazebo/envs/installation/catkin_ws/devel/setup.bash
export GAZEBO_MODEL_PATH=[path_to_gym-gazebo]/gym-gazebo/gym_gazebo/envs/installation/../assets/models
export GYM_GAZEBO_WORLD_PEDSIM=[path_to_gym-gazebo]/gym-gazebo/gym_gazebo/envs/installation/../assets/worlds/pedsim_turtlebot.world
export GYM_GAZEBO_WORLD_MAZE=[path_to_gym-gazebo]/gym-gazebo/gym_gazebo/envs/installation/../assets/worlds/maze.world
export GYM_GAZEBO_WORLD_CIRCUIT=[path_to_gym-gazebo]/gym-gazebo/gym_gazebo/envs/installation/../assets/worlds/circuit.world
export GYM_GAZEBO_WORLD_CIRCUIT2=[path_to_gym-gazebo]/gym-gazebo/gym_gazebo/envs/installation/../assets/worlds/circuit2.world
export GYM_GAZEBO_WORLD_CIRCUIT2C=[path_to_gym-gazebo]/gym-gazebo/gym_gazebo/envs/installation/../assets/worlds/circuit2c.world
export GYM_GAZEBO_WORLD_ROUND=[path_to_gym-gazebo]/gym-gazebo/gym_gazebo/envs/installation/../assets/worlds/round.world

```

## Running Guide ##
Go to [gym-gazebo]/examples/turtlebot and run
```
python pedsim_turtlebot_dqn.py
```
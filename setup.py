from setuptools import setup, find_packages
import sys, os.path

# Don't import gym module here, since deps may not be installed
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'gym-gazebo'))

setup(name='gym-gazebo',
      version='0.0.1',
      packages=find_packages(),
      install_requires=['gym>=0.2.3'],
      description='Combining gym-gazebo with pedsim_ros simulator to simulate turtlebot learning in gazebo environment',
      url='https://github.com/js0823/gym-gazebo',
      author='Erle Robotics',
      package_data={'gym-gazebo': ['envs/assets/launch/*.launch', 'envs/assets/worlds/*']},
)

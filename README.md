# ar1-robot-navigation

## Setup
Clone the repository into your workspace
```
git clone git clone https://github.com/Ajay-Vishaal/ar1-robot-navigation.git
```
Build the package using the command
```
catkin_make
```

## Runnning the simulation
To launch the simulation, run the below command
```
roslaunch ar1_description main.launch
```
This will launch the simulation along with rviz and Rviz marker publisher node.

To run the goal publisher node, run this command in new terminal
```
rosrun ar1_nav_stack waypoint_navigation.py 
```
This will ask for number of goals and it's respective goal points from the user.

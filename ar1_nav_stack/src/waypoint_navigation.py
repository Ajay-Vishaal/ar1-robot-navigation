#!/usr/bin/env python3

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

class NavigationClient:
    def __init__(self):
        rospy.init_node('nav')
        self.client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
        self.client.wait_for_server()

    def send_goal(self, x, y):
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = 'map'
        goal.target_pose.pose.position.x = x
        goal.target_pose.pose.position.y = y
        goal.target_pose.pose.orientation.w = 1.0

        self.client.send_goal(goal)
        self.client.wait_for_result()

    def send_goals(self, goals):
        for goal in goals:
            x, y = goal
            self.send_goal(x, y)

def main():
    goals = []
    num_goals = int(input("Enter the number of navigation goals: "))
    for i in range(num_goals):
        x = float(input("Enter X coordinate for goal {}: ".format(i+1)))
        y = float(input("Enter Y coordinate for goal {}: ".format(i+1)))
        goals.append((x, y))

    navigation_client = NavigationClient()

    for goal in goals:
        x, y = goal
        navigation_client.send_goal(x, y)

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
#!/usr/bin/env python3

import rospy
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point
from nav_msgs.msg import Path

class RVizMarkerPublisher:
    def __init__(self):
        rospy.init_node('rviz_marker_publisher')
        self.marker_pub = rospy.Publisher('visualization_marker', Marker, queue_size=10)
        self.path_sub = rospy.Subscriber('move_base/NavfnROS/plan', Path, self.path_callback)
        self.rate = rospy.Rate(1)
        self.marker_id = 0
        self.marker = self.create_marker()

    def create_marker(self):
        marker = Marker()
        marker.header.frame_id = "map"
        marker.type = Marker.LINE_LIST
        marker.action = Marker.ADD
        marker.scale.x = 0.1
        marker.scale.y = 0.1
        marker.color.r = 1.0
        marker.color.g = 0.0
        marker.color.b = 0.0
        marker.color.a = 1.0
        marker.points = []
        return marker

    def publish_marker(self, x, y):
        point = Point()
        point.x = x
        point.y = y
        point.z = 0
        self.marker.points.append(point)
        self.marker.id = self.marker_id
        self.marker_id += 1
        self.marker_pub.publish(self.marker)

    def path_callback(self, path_msg):
        self.marker.points = []
        for pose in path_msg.poses:
            x, y = pose.pose.position.x, pose.pose.position.y
            self.publish_marker(x, y)

    def run(self):
        rospy.spin()

if __name__ == '__main__':
    try:
        marker_publisher = RVizMarkerPublisher()
        marker_publisher.run()
    except rospy.ROSInterruptException:
        pass

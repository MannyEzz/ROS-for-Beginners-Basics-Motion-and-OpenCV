#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

def scan_callback(data):
    thr1 = 0.6 
    thr2 = 0.6
    rot1 = 3
    rot2 = 3
    if data.ranges[0]>thr1 and data.ranges[15]>thr2 and data.ranges[345]>thr2:
        print("more")
        move.linear.x = 0.2
        move.angular.z = 0.0
    else:
        print("lesss")
        move.linear.x = 0.0
        move.angular.z = 0.5
        if data.ranges[0]>rot1 and data.ranges[5]>rot2 and data.ranges[355]>rot2:
            move.linear.x = 0.2
            move.angular.z = 0.0
    velocity_publisher.publish(move)



if __name__ == '__main__':
    try:
        move= Twist()
        rospy.init_node('obstacle_avoidance', anonymous=True)
        velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        rospy.Subscriber("scan", LaserScan, scan_callback)
        rospy.spin()
        
    except rospy.ROSInterruptException:
        pass
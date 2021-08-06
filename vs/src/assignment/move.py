#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def callback(yala):
    rospy.loginfo( 'I heard %s, %s', yala.linear ,yala.angular)

def listener():

    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('/turtle1/cmd_vel', Twist, callback)
    rospy.spin()


if __name__ == '__main__':
    listener()
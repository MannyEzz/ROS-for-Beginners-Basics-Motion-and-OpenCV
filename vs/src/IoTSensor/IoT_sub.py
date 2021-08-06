#!/usr/bin/env python

import rospy
from vs.msg import IoTSensor

def callback(dd):
    rospy.loginfo('I heard %d, %s,%.2f, %.2f', dd.id,dd.name, dd.temperature, dd.humidity)
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('iot_sub_node', anonymous=True)

    rospy.Subscriber('iot_sen_topic', IoTSensor, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
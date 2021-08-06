#!/usr/bin/env python
# license removed for brevity

import rospy
from vs.msg import IoTSensor
import random

def talker():
    pub = rospy.Publisher('iot_sen_topic', IoTSensor, queue_size=10)
    rospy.init_node('iot_pub_node', anonymous=True)
    rate = rospy.Rate(1) # 1hz
    i=0
    while not rospy.is_shutdown():
        iot_sensor=IoTSensor()
        iot_sensor.id = 1
        iot_sensor.name = "iot_parking_ %d" %i
        iot_sensor.temperature = 24.33
        iot_sensor.humidity = 33.41
        rospy.loginfo(iot_sensor)
        pub.publish(iot_sensor)
        rate.sleep()
        i=i+1

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
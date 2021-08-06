#!/usr/bin/env python
# license removed for brevity

import rospy
import random
from vs.msg import ezz


def talker():
    pub = rospy.Publisher("IOT_senor",ezz,queue_size = 10)
    rospy.init_node("taker",anonymous = True)
    rate = rospy.Rate(1)
    i = 0

    while not rospy.is_shutdown():
        message= ezz()
        message.id = i
        message.name = "iot %d" %i
        message.temp = 25 + random.random()
        message.hum = 10 + random.random()

        rospy.loginfo(message)
        pub.publish(message)
        rate.sleep()
        i=i+1
        

if __name__ == '__main__':
    try:
        talker()
    except():
        pass
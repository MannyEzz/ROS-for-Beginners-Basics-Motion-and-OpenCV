#!/usr/bin/env python
# license removed for brevity

import rospy
from vs.msg import ezz


def IOT_Callback(message):
    rospy.loginfo("New IOT message %d,%s,%.2f,%.2f",message.id,message.name,message.temp,message.hum)




def listener():
    rospy.init_node("listener", anonymous = True)
    rospy.Subscriber("IOT_senor",ezz,IOT_Callback)
    rospy.spin()


if __name__ == '__main__':
    try:
        listener()
    except():
        pass
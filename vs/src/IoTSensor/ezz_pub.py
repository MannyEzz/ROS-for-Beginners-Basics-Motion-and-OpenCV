#!/usr/bin/env python
# license removed for brevity

import rospy
from vs.msg import IoTSensor

def Sensor_talker():
    pub = rospy.Publisher('Sensor_chatter', IoTSensor, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(0.5) # 10hz
    i=0
    while not rospy.is_shutdown():
        iot_sensor=IoTSensor()
        iot_sensor.id=1
        iot_sensor.name= "pub %d" %i
        iot_sensor.temperature= 55
        iot_sensor.humidity = 33
        rospy.loginfo(iot_sensor)
        pub.publish(iot_sensor)
        rate.sleep()
        i=i+1

if __name__ == '__main__':
    try:
        Sensor_talker()
    except rospy.ROSInterruptException:
        pass
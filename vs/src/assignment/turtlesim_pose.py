#!/usr/bin/env python

import rospy
from turtlesim.msg import Pose


#task 1. import the Pose type from the module turtlesim
x = 0
y = 0
theta = 0

def poseCallback(pose_message):
    global x,y,theta
   #task 4. display the x, y, and theta received from the message
   #print "pose callback"
   #print ('x = '.%) 
   #print ('y = %f' %) 
   #print ('yaw = '.%)
   x = pose_message.x
   y = pose_message.y
   theta = pose_message.theta 

if __name__ == '__main__':
    try:
        
        rospy.init_node('turtlesim_motion_pose', anonymous=True)
             

       #task 2. subscribe to the topic of the pose of the Turtlesim
       rospy.Subscriber("/turtle1/pose",Pose,pose_message)   
       #task 3. spin
       rospy.spin()

       
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")
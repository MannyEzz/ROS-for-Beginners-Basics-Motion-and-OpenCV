#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time

x=0
y=0
theta=0


def pose_call_back(pose_msg):
    global x 
    global y, theta
    x=pose_msg.x
    y=pose_msg.y
    theta=pose_msg.theta


def move (speed, distance, is_forward):
    move_forward = Twist()

    #to get the cuurent location
    global x, y
    x0=x
    y0=y

    if (is_forward):
        move_forward.linear.x = abs(speed)

    else:
        move_forward.linear.x = -abs (speed)

    distance_moved=0.0
    loop_rate = rospy.Rate(10)
    velocity_publisher=rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)   
    

    while True :
        rospy.loginfo('Turtora is moving')
        velocity_publisher.publish(move_forward) 

        loop_rate.sleep()

        distance_moved =  abs( math.sqrt(((x-x0)**2)+((y-y0)** 2)))
        print distance_moved

        if not (distance_moved < distance):
            rospy.loginfo("reached")
            break
    
    move_forward.linear.x=0
    velocity_publisher.publish(move_forward) 


def rotate ( angular_speed, angle, clockwise):
    global theta
    move_rotate = Twist()

    move_rotate.linear.x = 0.0
    move_rotate.linear.y = 0.0
    move_rotate.linear.z = 0.0

    move_rotate.angular.x = 0.0
    move_rotate.angular.y = 0.0
    move_rotate.angular.z = 0.0

    angular_speed1 = math.radians(abs(angular_speed))
    

    if (clockwise):
        move_rotate.angular.z = -abs (angular_speed1)
    else:
        move_rotate.angular.z = abs (angular_speed1)

    angle_moved = 0.0
    loop_rate = rospy.Rate(10)
    velocity_publisher=rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)   
    
    t0 = rospy.Time.now().to_sec()

    while True :
        rospy.loginfo('Turtora is rotating')
        velocity_publisher.publish(move_rotate) 

        t1= rospy.Time.now().to_sec()

        angle_moved = (t1-t0)*angular_speed 
        print angle_moved
        loop_rate.sleep()

        if (angle_moved > angle):
            rospy.loginfo("reached")
            break
    
    move_rotate.angular.z=0
    velocity_publisher.publish(move_rotate) 


def moveGoal ( x_goal, y_goal):
    global x, y, theta
    move_Goal=Twist()

    while (True):
        K_linear = 0.5
        dis = abs(math.sqrt((x_goal-x)**2)+((y_goal -y)**2))
        Linear_speed= dis * K_linear

        K_angular = 4.0
        ang = math.atan2(y_goal - y, x_goal - x)
        ang_speed = (ang - theta) * K_angular

        move_Goal.linear.x = Linear_speed
        move_Goal.angular.z = ang_speed

        velocity_publisher.publish(move_Goal)
        
        print 'x=', x, 'y=', y


        if (dis <0.01):
            break

def set_desired_oriantaion(desired_oriantaion):
    desired_angle = desired_oriantaion - theta

    if desired_angle < 0:
        clockwise = 1
    else:
        clockwise = 0

    rotate (30, math.degrees(abs(desired_angle)) ,clockwise)
    



if __name__ == '__main__':
    try:
        rospy.init_node('talker', anonymous=True)
        velocity_publisher=rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        pose_subs=rospy.Subscriber('/turtle1/pose', Pose, pose_call_back)
        time.sleep(2)

        #move(1.0, 5.0, False)
        #rotate (30,270,True)
        x_goal = rospy.get_param("x_goal")
        y_goal = rospy.get_param("y_goal")
        
        print 'x_goal = ' ,x_goal
        print 'y_goal = ' ,y_goal

        moveGoal(x_goal,y_goal)
        set_desired_oriantaion(50)
    except rospy.ROSInterruptException:
        pass
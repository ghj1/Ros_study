#! /usr/bin/env python3

import cv2
import rospy
from geometry_msgs.msg import Twist


def fun_callback(): 
    pass 

if __name__ == '__main__':
    rospy.init_node('simturtle_pub_rotate')
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)  

    twist = Twist()

    speed = 40
    angle = 180 # degrees

    angular_speed = (speed*2*3.14 )/360
    relative_angle = (angle*2*3.14)/360

    time0 = rospy.Time.now().to_sec()
    current = 0
    twist.angular.z = angular_speed

    while current < relative_angle: #current < relative_angle 이면 나오게 하려는 것
        pub.publish(twist)
        time1 = rospy.Time.now().to_sec()
        current = angular_speed * (time1 - time0)

    twist.angular.z = 0.0 
    pub.publish(twist)

    while True:
        key = cv2.waitKey()
        if key == 27:
            twist.angular.z = -current
            pub.publish(twist)
            

    
        pass
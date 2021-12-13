#! /usr/bin/env python3

import cv2
import rospy
from geometry_msgs.msg import Twist
# from rospy import topics #rostopic info /turtle1/cmd_vel 의 type

def fun_callback(): 
    pass 

if __name__ == '__main__':
    rospy.init_node('simturtle_publisher')
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)   # topic이름 (sub = pub 이름 동일)


    twist = Twist()

    twist.linear.y = twist.linear.z = 0.0
    twist.angular.x = twist.angular.y = twist.angular.z = 0
    
    distance =  2
    speed = 1 

    twist.linear.x = 2
    current_distance = 0
    while not rospy.is_shutdown():
        time0 = rospy.Time.now().to_sec()
        # while True:
        #     key = cv2.waitKey()
        #     if key == ord('g'):

        while current_distance < distance:
                pub.publish(twist)
                time1 = rospy.Time.now().to_sec()
                current_distance = int(speed * (time1-time0))


    twist.linear.x = 0
    pub.publish(twist)
        # twist.linear.x = -current_distance 
        # pub.publish(twist)
        # twist.linear.x = 0 
        # pub.publish(twist)

    pass
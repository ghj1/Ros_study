#! /usr/bin/env python3

import rospy
from std_msgs.msg import String

def fun_callback(msg): 
    rospy.loginfo('%s',msg.data) 
    return

def fun_callback_ex(msg): 
    rospy.loginfo('%s',msg.data) 
    return


if __name__ == '__main__':
    rospy.init_node('sample_pub')
    rospy.Subscriber('hello', String, callback= fun_callback)
    rospy.init_node('sample_pub_ex')
    rospy.Subscriber('hello_ex', String, callback= fun_callback_ex)
    rospy.spin() 
    pass
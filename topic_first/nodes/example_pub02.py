#! /usr/bin/env python3

import rospy
from std_msgs.msg import String  

def fun():
    pass

if __name__ == '__main__':
    rospy.init_node('sample_pub')
    pub_01 = rospy.Publisher('hello_ex', String, queue_size=10)  
  
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        str = 'hello_publisher_ex: %s' % rospy.get_time() 
        pub_01.publish(str) 
        rate.sleep() 
    pass
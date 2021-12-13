#! /usr/bin/env python3

import rospy
from std_msgs.msg import String  

def fun_callback(msg): 
    rospy.loginfo('%s',msg.data) 
    pass 

if __name__ == '__main__':
    rospy.init_node('sample_pub')
    pub = rospy.Publisher('hello', String, queue_size=10)  
    
    # rospy.Subscriber('hello_p', String, callback= fun_callback)
  
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        str = 'hello_publisher: %s' % rospy.get_time() 
        pub.publish(str) 
        rate.sleep() 
    pass
#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from SRA.msg import custom_array ##custom message
import sys


def talker():

    pub_string = rospy.Publisher('string', String, queue_size=10)
    pub_array = rospy.Publisher('array',custom_array, queue_size=10) 
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10)	#10hz
    msg = custom_array()

    while not rospy.is_shutdown():
        string_input = raw_input("Enter your name : ")
        pub_string.publish(string_input)
        
        t1 = int(input("Enter theta1 "))
        t2 = int(input("Enter theta2 "))
        t3 = int(input("Enter theta3 "))

        msg.array1.append(t1)
        msg.array1.append(t2)
        msg.array1.append(t3)

        rospy.loginfo(msg)
        pub_array.publish(msg)
        msg.array1 = []
        rate.sleep()
        

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: 
        pass








    
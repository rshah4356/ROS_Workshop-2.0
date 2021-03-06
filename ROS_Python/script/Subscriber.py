#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from SRA.msg import custom_array


def callback_string(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s",data.data)

def callback_array(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard {},{},{}".format(data.array1[0],data.array1[1],data.array1[2]))
        

def listener():
	rospy.init_node('listener', anonymous=True)
	rospy.Subscriber("string",String,callback_string)
	rospy.Subscriber("array",custom_array, callback_array)

	while not rospy.is_shutdown():
		rospy.spin()
	
   
if __name__ == '__main__':
	listener()
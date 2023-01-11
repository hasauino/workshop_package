#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

rospy.init_node("pub_str")
pub = rospy.Publisher("chat", String, queue_size=10)
rate_value = rospy.get_param("rate", 1)
rate = rospy.Rate(rate_value)

msg = String()
msg.data = "hello world!"
while not rospy.is_shutdown():
    pub.publish(msg)
    rate.sleep()
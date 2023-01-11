#!/usr/bin/env python3

import rospy
from std_msgs.msg import String


def cb(msg):
    print(msg)


rospy.init_node("sub_str")
rospy.Subscriber("chat", String, callback=cb, queue_size=10)
rospy.spin()

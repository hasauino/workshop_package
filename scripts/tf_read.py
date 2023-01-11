#!/usr/bin/env python3

import rospy
import tf

rospy.init_node("tf_reader")

listener = tf.TransformListener()

listener.waitForTransform("link_2", "map", rospy.Time(0), timeout=rospy.Duration(100))

trans, rot = listener.lookupTransform("map", "link_2", rospy.Time(0))

print(trans)
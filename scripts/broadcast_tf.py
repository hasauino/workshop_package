#!/usr/bin/env python3
import rospy
import tf

rospy.init_node("broadcaster")
broadcaster = tf.TransformBroadcaster()

rate = rospy.Rate(20)

while not rospy.is_shutdown():
    broadcaster.sendTransform([2, 3, 0], [0, 0, 0, 1], rospy.Time.now(), "base", "map")
    broadcaster.sendTransform([0, 0, 5], [0, 0, 0, 1], rospy.Time.now(), "link_1", "base")
    broadcaster.sendTransform([1, 0, 0], [0, 0, 0, 1], rospy.Time.now(), "link_2", "link_1")
    rate.sleep()
#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import JointState

rospy.init_node("joints_publisher")
rate = rospy.Rate(20)
pub = rospy.Publisher("joint_states", JointState, queue_size=10)

joints = [
    "neck_base_shoulder_left",
    "shoulder_shoulder_left",
    "shoulder_upperArm_left",
    "upperArm_midArm_left",
    "midArm_lowerArm_left",
    "neck_base_shoulder_right",
    "shoulder_shoulder_right",
    "shoulder_upperArm_right",
    "upperArm_midArm_right",
    "midArm_lowerArm_right",
]
msg = JointState()
msg.name = joints
msg.position = [0.0] * 10

while not rospy.is_shutdown():
    msg.header.stamp = rospy.Time.now()
    msg.position[0] += 0.1
    pub.publish(msg)
    rate.sleep()

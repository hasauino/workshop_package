cmake_minimum_required(VERSION 3.0.2)
project(workshop)


find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  message_generation
)

add_message_files(
  FILES
    Example.msg
)

generate_messages(
  DEPENDENCIES
  std_msgs
)

catkin_package(
  CATKIN_DEPENDS message_runtime
)



catkin_package()


include_directories(
  ${catkin_INCLUDE_DIRS}
)
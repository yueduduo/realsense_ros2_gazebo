<launch>
  <arg name="model" default="$(find realsense_ros2_gazebo)/urdf/test.xacro"/>
  <param name="robot_description" command="$(find xacro)/xacro $(arg model)" />
  <node name="joint_state_publisher" pkg="joint_state_publisher" type="joint_state_publisher" />
  <node name="robot_state_publisher" pkg="robot_state_publisher" type="robot_state_publisher" />
</launch>

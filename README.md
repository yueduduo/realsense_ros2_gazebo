# 说明
本仓库修复了运行D435仿真插件时的 segment fault(段错误 (核心已转储)) bug. 
通过gdb gzserver run 发现原作者在从ros1迁移到ros2后, 没有初始化node_节点指针导致了bug.

2024/8/13

# realsense_ros2_gazebo

Intel RealSense Tracking and Depth cameras simulated models for Gazebo/ROS 2, with URDF macros.

**Work in progress as of June 3, 2022.**

## RealSense T265 ##

![](doc/t265.png)

### Usage ###
```xml
<xacro:include filename="$(find realsense_ros2_gazebo)/xacro/tracker.xacro"/>

<xacro:realsense_T265 sensor_name="camera" parent_link="base_link" rate="30.0">
  <origin rpy="0 0 0" xyz="0 0 0.5"/>
</xacro:realsense_T265>
```

### Publishers ###
* /camera/**fisheye1**/*
* /camera/**fisheye2**/*
* /camera/**gyro**/sample _( accel and gyro are in the same imu message )_
* /camera/**odom**/sample



## RealSense R200 ##

![](doc/r200.png)

### Usage ###
```xml
<xacro:include filename="$(find realsense_ros2_gazebo)/xacro/depthcam.xacro"/>

<xacro:realsense_R200 sensor_name="camera" parent_link="base_link" rate="30.0">
  <origin rpy="0 0 0" xyz="0 0 0.5"/>
</xacro:realsense_R200>
```

### Publishers ###

* /camera/**color**/*
* /camera/**depth**/*
* /camera/**infra1**/*
* /camera/**infra2**/*



## RealSense D435

![](doc/d435.png)

### Usage ###

```xml
<xacro:include filename="$(find realsense_ros2_gazebo)/xacro/depthcam.xacro"/>

<xacro:realsense_d435 sensor_name="d435" parent_link="base_link" rate="10">
  <origin rpy="0 0 0 " xyz="0 0 0.5"/>
</xacro:realsense_d435>
```

### Publishers ###

* /camera/**color**/*
* /camera/**depth**/*
* /camera/**infra1**/*
* /camera/**infra2**/*

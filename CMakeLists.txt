cmake_minimum_required(VERSION 3.15)
project(realsense_ros2_gazebo)

set(CMAKE_BUILD_TYPE "RelWithDebInfo")

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(camera_info_manager REQUIRED)
find_package(diagnostic_updater REQUIRED)
find_package(gazebo_dev REQUIRED)
find_package(gazebo_msgs REQUIRED)
find_package(gazebo_ros REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(image_transport REQUIRED)
find_package(pluginlib REQUIRED) # TODO Probably required
find_package(rclcpp REQUIRED)
find_package(rclcpp_components REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(std_msgs REQUIRED)
find_package(tf REQUIRED)
find_package(tf2_ros REQUIRED)
find_package(Threads REQUIRED)
find_package(urdf REQUIRED)

link_directories(${gazebo_dev_LIBRARY_DIRS})

# RealSense Gazebo plugin
add_library(realsense_gazebo_plugin SHARED
  src/RealSensePlugin.cpp
  src/gazebo_ros_realsense.cpp)
target_include_directories(realsense_gazebo_plugin PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>)
target_link_libraries(realsense_gazebo_plugin PUBLIC
  ${GAZEBO_LIBRARIES}
  Threads::Threads)
ament_target_dependencies(
  realsense_gazebo_plugin
  "camera_info_manager"
  "diagnostic_updater"
  "gazebo_dev"
  "gazebo_msgs"
  "gazebo_ros"
  "geometry_msgs"
  "image_transport"
  "rclcpp"
  "rclcpp_components"
  "sensor_msgs"
  "std_msgs"
  "tf"
  "tf2_ros"
  "urdf"
)
ament_export_dependencies(ament_cmake)
ament_export_dependencies(rclcpp)
ament_export_targets(realsense_gazebo_pluginTargets HAS_LIBRARY_TARGET)

# Install Gazebo plugin library
install(TARGETS realsense_gazebo_plugin
  EXPORT realsense_gazebo_pluginTargets
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
  RUNTIME DESTINATION bin
  INCLUDES DESTINATION include)

# Install header files
install(DIRECTORY include/realsense_gazebo_plugin
  DESTINATION include)
  #FILES_MATCHING PATTERN "*.h" TODO Required?
  #PATTERN ".svn" EXCLUDE TODO Required?

# Install models meshes
install(DIRECTORY meshes
    DESTINATION share/${PROJECT_NAME})

# Install xacro files
install(DIRECTORY xacro
    DESTINATION share/${PROJECT_NAME})

# TODO Must be added (see ROS 2 plugins tutorial)
pluginlib_export_plugin_description_file(realsense_gazebo_plugin realsense_gazebo_plugin.xml)

ament_package()

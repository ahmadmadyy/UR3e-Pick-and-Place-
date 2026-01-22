cmake_minimum_required(VERSION 3.8)
project(moveit2_scripts)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclcpp_action REQUIRED)
find_package(moveit_core REQUIRED)
find_package(moveit_ros_planning REQUIRED)
find_package(moveit_ros_planning_interface REQUIRED)
find_package(interactive_markers REQUIRED)
find_package(geometric_shapes REQUIRED)
find_package(control_msgs REQUIRED)
find_package(moveit_msgs REQUIRED)

# ---------------------------------------------------------
# Executables
# ---------------------------------------------------------
add_executable(joint_space_trajectory src/joint_space_trajectory.cpp)
add_executable(goal_pose_trajectory src/goal_pose_trajectory.cpp)
add_executable(double_motion_trajectory src/double_motion_trajectory.cpp)
add_executable(gripper_control src/gripper_control.cpp)
add_executable(cartesian_trajectory src/cartesian_trajectory.cpp)
add_executable(approach_retreat_trajectory src/approach_retreat_trajectory.cpp)
add_executable(draw_x_cartesian_trajectory src/draw_x_cartesian_trajectory.cpp)
add_executable(kinematics_plugin_trajectory src/kinematics_plugin_trajectory.cpp)
add_executable(pick_and_place_trajectory src/pick_and_place_trajectory.cpp)

# ---------------------------------------------------------
# Dependencies
# ---------------------------------------------------------
foreach(target
  joint_space_trajectory
  goal_pose_trajectory
  double_motion_trajectory
  gripper_control
  approach_retreat_trajectory
  cartesian_trajectory
  draw_x_cartesian_trajectory
  kinematics_plugin_trajectory
  pick_and_place_trajectory
)
  target_include_directories(${target}
    PUBLIC include
  )

  ament_target_dependencies(${target}
    rclcpp
    rclcpp_action
    moveit_core
    moveit_ros_planning
    moveit_ros_planning_interface
    interactive_markers
    control_msgs
    moveit_msgs
  )
endforeach()

# ---------------------------------------------------------
# Install
# ---------------------------------------------------------
install(TARGETS
  joint_space_trajectory
  goal_pose_trajectory
  double_motion_trajectory
  gripper_control
  approach_retreat_trajectory
  cartesian_trajectory
  draw_x_cartesian_trajectory
  kinematics_plugin_trajectory
  pick_and_place_trajectory
  DESTINATION lib/${PROJECT_NAME}
)

install(DIRECTORY
  launch
  DESTINATION share/${PROJECT_NAME}
)

# ---------------------------------------------------------
# Testing
# ---------------------------------------------------------
if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()

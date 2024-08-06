---
layout: page
title: Robotlab - UFactory xArm6
permalink: /robotlab/xarm6
---

UFactory xArm6 is among a series of light-weight multi-DOFs robots with simple programming interface. It has 6 revolute joints and 5kg payload, with a repetitive accuracy of 0.1mm. The official repository contains a rich document about programming it with [python SDK](https://github.com/xArm-Developer/xArm-Python-SDK) or [ROS](https://github.com/xArm-Developer/xarm_ros2). The remote computer can be connected to the robot via a network and a direct cable if low latency is desired.

Basically turn on the power switch on the control box to turn on the robot. The process will start with a beep and after a while raise three consecutive beeps indicating it is ready to use. The control box has firmware and a graphical user interface pre-installed. To use the interface as a teaching pendant, users may either download a client called [ufactory studio](https://www.ufactory.cc/ufactory-studio/) or directly access through a web browser. A label of IP can be found on the robot and one can simply type "192.168.1.xx:18333" in the browser to command the robot.

<div>
<img src="./assets/img/IMG_0684.jpeg" width="432" height="576"/>
</div>

The lab space does not have its native gripper and suction cup kit. However, its toolplate and RS 485 connection should be compatible to lab grippers. There are examples for using external device such as [Robotiq grippers](http://help.ufactory.cc/en/articles/3997200-guide-to-use-the-robotiq-gripper-on-ufactory-xarm). Similar programming should be possible for grippers like OnRobot RG2 or other devices supporting serial communication. 
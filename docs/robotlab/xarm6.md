---
layout: page
title: Robotlab - UFactory xArm6
permalink: /robotlab/xarm6
---

UFactory xArm6 is among a series of light-weight multi-DOFs robots with simple programming interface. It has 6 revolute joints and 5kg payload, with a repetitive accuracy of 0.1mm. The official repository contains a rich document about programming it with [python SDK](https://github.com/xArm-Developer/xArm-Python-SDK) or [ROS](https://github.com/xArm-Developer/xarm_ros2). The remote computer can be connected to the robot via a network and a direct cable if low latency is desired.

<div>
<img src="./assets/img/IMG_0684.jpeg" width="432" height="576"/>
</div>

The lab space does not have its native gripper and suction cup kit. However, its toolplate and RS 485 connection should be compatible to lab grippers. There are examples for using external device such as [Robotiq grippers](http://help.ufactory.cc/en/articles/3997200-guide-to-use-the-robotiq-gripper-on-ufactory-xarm). Similar programming should be possible for grippers like OnRobot RG2 or other devices supporting serial communication. 
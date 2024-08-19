---
layout: page
title: Robotlab - Optitrack
permalink: /robotlab/optitrack
---

The MoCap system has been connected to a computer (the "motive" computer) via a separated network switch. The Motive computer has dual network adapters so it is also connected to the main RobotLab network (currently via WiFi). To activate the optitrack system:

* Plug the power cable of the optitrack network switch;
* Turn on the Motive computer and log in the Windows system;
* Start the Motive application and check if the markers are visible and trackable in the GUI;
* Create named rigid-bodies or tracker sets for parsing the data. Note that Motive can remember created objects.

The data should be streamed if everything goes smoothly. Check options in the datastreaming tab if this was not the case. The official website has a detailed documentation about these options (https://docs.optitrack.com/motive/data-streaming). Basically, Motive is using the second network adapter (default IP should be 192.168.1.37) as a server so any other computers connecting to the RobotLab network can work as a client to read the data through standard socket programming. 

Unsurprisingly, someone has created code libraries to handle the network setup and data parsing. You can choose one of below or search online for others that might integrate best with your program:

* [NatNet](https://optitrack.com/software/natnet-sdk/) the official SDK in C++ for Windows/Ubuntu/Fedora;
* [python-natnet-client](https://github.com/TimSchneider42/python-natnet-client.git) a relatively recent third-party library written in Python;
* [mocap_optitrack](https://github.com/ros-drivers/mocap_optitrack.git) maintained as one of the ROS drivers. Could be useful if you plan to connect the data to other ROS nodes.

The current wireless setup can transmit data at around 100Hz. Some applications might be sensitive to the rate of frame drop and other transportation over the RobotLab network. Consider to use ethernet cables if this is critical to your experiments.
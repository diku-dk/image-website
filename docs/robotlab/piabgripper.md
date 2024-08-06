---
layout: page
title: Robotlab - Piab Vacuum Kit
permalink: /robotlab/piabgripper
---

[Piab](https://www.piab.com) provides vacuum technologies for lifting and moving objects in automation applications. The lab space has received a package of vacuum cups and soft grippers that may suit different payloads and object geometries. The grippers can be connected to robot arms such as [UR5e](./ur5e) and actuated with vacuum ejector (the red aspirator in the picture) or piCOMPACT I/O link (the device in the picture). Note you would need air compressor as in the picture below and pneumatic solenoid valves to control on/off of the grip. Consult the lab manager on how to use them properly.

<div>
<img src="./assets/img/IMG_0685.jpeg" width="576" height="432"/>
<img src="./assets/img/IMG_0686.jpeg" width="576" height="432"/>
</div>

The lab has sufficient gadgets to build circuits to control the air flow and hence the on/off of grip from a computer. As a demonstrated example, you may find a setup in a plastic box using Aruidno, power control and valves to do so. 

<div>
<img src="./assets/img/IMG_0925.jpg" width="576" height="432"/>
</div>

Note that the valves is drive by 12V power so we cannot directly connect them to the output pins of Arduino (some motor control boards might be fine though). The power control here serves as a switch that allows us to use small electric currents to signal on/off of larger currents. 

We can use serial port to communicate with Arduino to trigger the on/off action. On the arduino side, we may simply use a code snippet:

```cpp
const int airvalvePin = 8;
int commandByte;

void setup(){
    Serial.begin(9600);
    pinModel(airvalvePin, OUTPUT);
}

void loop(){
    if(Serial.available() > 0){
        commandByte = Serial.read();

        if(commandByte == 'O' || commandByte == 'o'){
            digitalWrite(airvalvePin, HIGH);
        }
        if(commandByte == 'C' || commandByte == 'c'){
            digitalWrite(airvalvePin, LOW);
        }
    }
}
```

While on the computer side, we can use python to write to the serial port:

```python
import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600)   #check the port identifier on your computer
time.sleep(1)

while True:
    try:
        cmd = input("Input O or C to open or close the valve...")
        if len(cmd) > 0:
            ser.write(str.encode(cmd[0]))
    except KeyboardInterrupt:
        print("Exit the loop and close the serial.")
        break

ser.close()
```

A good practice could be wrap the serial communication into a grip() function. Note that valve-on means closing the gripper or activating the suction since the compressed air is used to create vacuum. You might want to name the command differently if that creates confusion.
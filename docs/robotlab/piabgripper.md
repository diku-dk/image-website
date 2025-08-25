---
layout: page
title: Robotlab - Piab Vacuum Kit
permalink: /robotlab/piabgripper
---
# Version 1
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

# Version 2
The new version of the setup use a 6-channel piCOMPACTx10 and is actuated by the digital output of the robot arm UR5e.
The input to the pump is compressed air which pressure is controlledy by a FESTO (8046299) proportional-pressure regulator mappint an electrical input form 0-10 V to pressure 0-6 Bar (0-87 psi).
This setup is suitable to control robot, regulator and pump from the control box of the UR5e. The regulator is controlled by an analog output and the pump by a digital output.


The following code first enables the input pressure from the regulator and then cyclicly switches the pump ON and OFF for a defined amount of cycles, with an interval of 2 seconds. The standard digital output pin decides the direction of the air flow.

```python
import rtde_io
import rtde_receive
import time

IP="ROBOT_IP"
_io = rtde_io.RTDEIOInterface(IP)
_r = rtde_receive.RTDEReceiveInterface(IP)
# proportional reguulator fully open
_io.setAnalogOutputVoltage(0,1) # Analog outoput 0,  10V (voltage is controlled with a float 0 to 1)


def to_psi(V):
    return (V - 4/5) * 53.0657 # Adjusted for the pump's voltage to pressure relationship

def regulator_to_psi(V):
    return V/10*87 # Adjusted for the regulator's voltage to pressure relationship


pressure=[]
voltage=[]

def wait_and_log(seconds):
    counter=0
    step=0.01
    while counter<seconds: 
        voltage.append(_r.getStandardAnalogInput0()) #read voltage
        pressure.append(to_psi(_r.getStandardAnalogInput0())) #convert to pressure
        time.sleep(step)
        counter+=step

def print_pin_state(pin):
    # Get the state of the pin
    state = _r.getDigitalOutState(pin)
    if state:
        print(f"Pin {pin} is HIGH")
    else:
        print(f"Pin {pin} is LOW")


#Chose the pin of the standard digital output
mode="suck"
if mode=="blow":
    pin=0
elif mode=="suck":
    pin=1
else:
    print("Invalid mode. Use 'blow' or 'suck'.")

seconds=2
counter=0
while counter<10:# ten on off cycles
    _io.setStandardDigitalOut(pin, True) #start

    wait_and_log(seconds)

    _io.setStandardDigitalOut(pin, False)#stop

    wait_and_log(seconds)
    counter+=1
```


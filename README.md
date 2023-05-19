# webpage-controlled-bot
Raspberry Pi Pico robot controlled by a web application with the help of requests.

[See it for yourself](https://youtu.be/ovlnHXRR9XI)

This repository is for the modified version of my older robot [repository](https://github.com/timotei42/bluetooth_robot).Now, instead of using Bluetooth to send commands, I use requests. The robot can be controlled via a webapp.

I'll go over:
  - the components used
  - the set values 
  - what i use to communicate with the robot

 ## The Components
 The components used are as follows:
  - a Raspberry Pi Pico W
  - 2 SG 90 servos ([microservos,for ease of use](http://www.ee.ic.ac.uk/pcheung/teaching/DE1_EE/stores/sg90_datasheet.pdf))
 ## Set Values in the Code
 They are as follows
 - The PWM frequency for the microservos is 50 Hz.
  - The STEP variable is to determine how fast the servo schanges position. The higher it is the faster the servo will move. I set it to 50 for smooth movement. It also runs a lower risk of the robot losing balance, with the base being 0.5 kg
- max_wait is the numbers of attempts the Pi will make to connect to the wifi. If the connection still fails, it wll throw a connection error. 

## The Remote
The robot is controlled by a webapp made in react, using Typescript. I tried to keep it as minimal as possible. The four buttons under the "Simple Movements" heading move the servos back and forth and the two buttons under the "Combined Movements" are combinations of the simple movements. The requirements for the page are ```react``` for the buttons and ```axios``` for sending requests.The buttons themselves are react components.
The dialogue only takes place over the local network.

## C implementation of robot code 
(coming soon)

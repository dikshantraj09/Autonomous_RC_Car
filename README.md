# Autonomous_RC_Car
Made a diy Autonomous RC Car using ROS, Raspberry Pi-4,Arduino and L298n Motor driver, RP-LIDAR for Laser Scan Data
![alt text](https://lh3.googleusercontent.com/ygYSRw36hOCKKH4Lk4oOrR2HaGkdY2ZuQ602AKA42sG8EUZHb7hV3Ep5kBDc2HipGqUMnzeBPcauVIJP7mrwfGovMjKOUDWmJE0hmHUIcljiQ5mY3ZeV_KEDp4pD4u2ETWpPPy4c0pAY_88a1jvYbkOrImVSGyL1R6Umc4v9Rk3pU0bqtKHlekr_7pC4Nf5duo7lQD08hQ3GtBSH_jG62cTlr0D6uBgI3d8aCjfriTWkH0qnPG2e46vWDuxlatPvQehVbRzrTLIcC_UMiaA_ilD64iAhaW7UbZVjudeDnsaleJjucJkk-H_ovjxuDjWIVo_Jv5RRxHXmqq5WXZW7IPWQIPNs4Msqz066cmLK5AebeMQ9aTvPb_xcaSAByZcxzqPUS3fvRrAxQOKFtnT3f_6fmtsXmQ22-hx0y3XwdFJ-4e7BPvRU5Ji6wkRZ9rVUs9TYHF_OcBNpwvb4G7eXGOGMhPGodU4k98pvVYGmfECnxhDyxaBhVo6LG7YKWr4gBK8wumo5CAqatYBIE4pPkztPQuvlaBb6Su4tiHH0cZ4pmms6X0HCe7bzt9Z1cH_vUKpruaOzctwSvdTzLZt-uVlU6XtFzG5372BBhwGEctE9LFpJLvBAa9Ay_HMKOLXhuftb_gNJL_v0ukcUm1apcfZ7G2KtuQBzdBFQz6Q2WHe2lp1Ochq35Xb3BDH8w-kgN9X9OaacdKCi0ROodEjAg3Auyw=w1343-h1007-no?authuser=0)
## Autonomous Operation Demo
![alt](https://media.giphy.com/media/ZHOvBsc81Ag0K6fCMH/giphy.gif)
## Prerequisites
1. Raspbian OS on Raspberry Pi4
2. ROS Melodic Installed
3. Arduino IDE
4. Python 2.7 and 3.7 installed
5. RP-LIDAR SD

## STEPS FOR TELE-OPERATION
1. run `roscore`
2. export current IP : `export ROS_IP= Current IP`
3. export current Master : `export ROS_MASTER_URI= http://current_ip:11311`
4. run rosserial : `rosrun rosserial_python serial_node.py`
5. run python file to publish Command Velocity : file in `/steer_bot/src/drive_servo.py`
6. run joy_node : `rorun joy joy_node`

![alt text](./13.jpeg "Title")
![alt text](./12.jpeg "Title")
# Circuit Simulation
![alt text](./11.jpeg "Title")

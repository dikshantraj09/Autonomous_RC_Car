#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy


def callback(data):
    twist = Twist()
    # if data.buttons[4] == 1:
    #     twist.angular.x = 35
    # else:
    #     twist.angular.x = 130
    if data.axes[3] < 0:
        twist.angular.x = 90+50*data.axes[3]
    else:
        twist.angular.x = 90+40*data.axes[3]
    if data.buttons[7] == 1:
        twist.linear.x = 255
    elif data.buttons[6] == 1:
        twist.linear.x = -255
    else:
        twist.linear.x = 0
    #twist.linear.x = 255*data.axes[4]
    pub.publish(twist)


def start():
    # publishing to "turtle1/cmd_vel" to control turtle1
    global pub
    rospy.init_node("rc_car")
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    # subscribed to joystick inputs on topic "joy"
    rospy.Subscriber("joy", Joy, callback)
    # starts the node

    rospy.spin()


if __name__ == '__main__':
    start()

#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy


def callback(data):
    # print("sub")
    twist = Twist()
    twist.angular.x = 90+100*data.angular.z
    if (data.linear.x > 0):
        twist.linear.x = 255
    elif (data.linear.x < 0):
        twist.linear.x = -255
    pub.publish(twist)


def start():
    # publishing to "turtle1/cmd_vel" to control turtle1
    global pub
    rospy.init_node("rc_car")
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    # subscribed to joystick inputs on topic "joy"
    rospy.Subscriber(
        "/rpi_car/ackermann_steering_controller/cmd_vel", Twist, callback)
    # starts the node

    rospy.spin()


if __name__ == '__main__':
    start()

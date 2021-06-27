#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Imu


def callback(data):
    twist = Twist()
    twist.angular.x = 90+5 * data.linear_acceleration.y
    #twist.angular.z = 4*data.buttons[1]
    # print("got")
    pub.publish(twist)


def start():
    # publishing to "turtle1/cmd_vel" to control turtle1
    global pub
    rospy.init_node("rc_car")
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    # subscribed to joystick inputs on topic "joy"
    rospy.Subscriber("/android/imu", Imu, callback)
    # starts the node

    rospy.spin()


if __name__ == '__main__':
    start()

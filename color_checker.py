#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from ogrebot.msg import robot_vels
from std_msgs.msg import *
import Adafruit_TCS34725
import smbus

state = False

if __name__ == '__main__':
    rospy.init_node('color_checker', anonymous=False)
    color = rospy.Publisher('color', Bool, queue_size=10)
    tcs=Adafruit_TCS34725.TCS34725()
    while not rospy.is_shutdown():
        r,g,b,c = tcs.get_raw_data()
        if (c > 300 and not state):
            color.publish(True)
            state = True
            print('white')
        elif (c < 300 and (state)):
            state = False
            color.publish(False)
            print('black')
        rospy.sleep(.01)

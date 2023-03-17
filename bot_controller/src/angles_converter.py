#!/usr/bin/python3

import rospy
import math
from bot_controller.srv import AnglesConverters, AnglesConvertersResponse

def convert_rad_to_degrees(req):
    res = AnglesConvertersResponse()
    res.base = int(((req.base + (math.pi/2))*180)/math.pi)
    res.shoulder = 180 - int(((req.shoulder + (math.pi/2))*180)/math.pi)
    res.elbow = int(((req.elbow + (math.pi/2))*180)/math.pi)
    res.gripper = int(((-req.gripper)*180)/math.pi)
    return res


def convert_degrees_to_rad(req):
    res = AnglesConvertersResponse()
    res.base = ((req.base * math.pi) - ((math.pi/2)*180))/180
    res.shoulder = (((180 - req.shoulder)* math.pi) - ((math.pi/2)*180))/180
    res.elbow = ((req.elbow * math.pi) - ((math.pi/2)*180))/180
    res.gripper = -((math.pi/2)*req.gripper)/180
    return res

if __name__ == '__main__':
    rospy.init_node('angles_converter')
    rad_to_degrees = rospy.Service('rad_to_degrees', AnglesConverters, convert_rad_to_degrees)
    degrees_to_rad = rospy.Service('degrees_to_rad', AnglesConverters, convert_degrees_to_rad)
    rospy.spin()
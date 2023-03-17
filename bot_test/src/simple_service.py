#!/usr/bin/python3

from bot_test.srv import AddTwoInts, AddTwoIntsResponse
import rospy


def add_two_ints(req):
    rospy.loginfo('Ready to sum %d and %d', req.a, req.b)
    return AddTwoIntsResponse(req.a + req.b)

if __name__ == "__main__":
    rospy.init_node('simple_service')
    service = rospy.Service('add_two_ints', AddTwoInts, add_two_ints)
    rospy.loginfo("Ready to add two ints.")
    rospy.spin()
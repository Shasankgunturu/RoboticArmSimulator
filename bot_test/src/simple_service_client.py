#!/usr/bin/python3

import rospy
from bot_test.srv import AddTwoInts
import sys

if __name__=="__main__":
    if len(sys.argv) == 3: #name and 2 other args
        a = int(sys.argv[1])
        b = int(sys.argv[2])
    else:
        print("dumbass")
        sys.exit(-1)

    print("Requesting sum of", a, b)
    # rospy.wait_for_message('add_two_ints', Int64)
    add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts) #name and type of service
    response = add_two_ints(a, b)
    print("service response", response)
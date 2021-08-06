#!/usr/bin/env python
# license removed for brevity

import sys
import rospy

from vs.srv import AddTwoint
from vs.srv import AddTwointRequest
from vs.srv import AddTwointResponse

def add_two_int_client(x,y):
    rospy.wait_for_service('add_two_int')
    try:
        add_two_int = rospy.ServiceProxy('add_two_int', AddTwoint)
        resp = add_two_int(x,y)
        return resp.sum
    except rospy.ServiceException, e:
        print "service call failed: %s" %e

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print usage()
        sys.exit(1)
    print ("Requesting %s + %s "%(x,y))
    print("%s + %s = %s"%(x, y, add_two_int_client(x, y)))

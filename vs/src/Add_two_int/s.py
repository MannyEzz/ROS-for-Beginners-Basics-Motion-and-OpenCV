#!/usr/bin/env python
# license removed for brevity

import rospy
from vs.srv import weq
from vs.srv import weqResponse
from vs.srv import weqRequest
import time

def call_back(req):
    print("returning %s * %s = %s"%(req.a,req.b,(req.a*req.b)))
    time.sleep(5)
    sum_response = weqResponse(req.a*req.b)
    return sum_response


def server():
    rospy.init_node("server")
    rospy.Service('multi',weq,call_back)
    print("ready to multiply")
    rospy.spin()


if __name__ == "__main__":
    try:
        server()
    except:
        pass
import sys, os
import numpy as np
import cv2
import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import Float64, String
from cv_bridge import CvBridge

cap = cv2.VideoCapture(0, cv2.CAP_V4L2)

rospy.init_node("pi_cam_pub", anonymous=True)
image_pub = rospy.Publisher("/cam_pub", Image, queue_size=1)
#image_8UC4 = rospy.Publisher("/8UC4", Image, queue_size=1)
bridge = CvBridge()

counter = 0
while not rospy.is_shutdown():
	if counter % 2 != 0:
		counter += 1
	else:
		counter = 1
	ret, image = cap.read()
	image_pub.publish(bridge.cv2_to_imgmsg(image,"bgr8"))
#	image_8UC4.publish(bridge.cv2_to_imgmsg(image,"rgb8"))

cap.release()
cv2.destoryAllWindows()

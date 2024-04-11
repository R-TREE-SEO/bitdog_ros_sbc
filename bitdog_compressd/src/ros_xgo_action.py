#!/usr/bin/python3

import random
import time
import json 
import xgolib
import rospy
from std_msgs.msg import Float64, String, Int8
import sys,os
import subprocess
#sudo chmod a+rw /dev/ttyS0

subprocess.call([("sudo chmod a+rw /dev/ttyAMA0")],shell = True)


class xgo:
	def __init__(self):
		self.action = rospy.Subscriber('/xgo', Int8,self.action, queue_size = 1)
		self.line = rospy.Subscriber('/line', String, self.line, queue_size = 1)
		self.xgo = xgolib.XGO('/dev/ttyAMA0')
		self.ls = ["xgo.stop", "xgo.move_y", "xgo.forward", "xgo.back", "xgo.left", "xgo.right", "xgo.turnleft", "xgo.turnright"]
		
	def action(self, label):
		print(label.data)
		if type(label.data) == int:
			data = label.data
			self.xgo.action(data)
	def line(self, data):
		line = data.data
		if line == self.ls[2]:
			self.xgo.forward(10)
			#time.sleep(1.2)
			#self.xgo.stop()
		elif line == self.ls[0]:
			self.xgo.stop()
			self.xgo.turnleft(1)
			self.xgo.turnright(1)
			self.xgo.turnleft(0)
			self.xgo.turnright(0)
		elif line == self.ls[3]:
			self.xgo.back(10)
		elif line == self.ls[4]:
			self.xgo.left(10)
		elif line == self.ls[5]:
			self.xgo.right(10)
		elif line == self.ls[6]:
			self.xgo.turnright(20)
			#self.xgo.action(4)
		elif line == self.ls[7]:
			self.xgo.turnleft(20)
			#self.xgo.action(5)

	def main(self):
		rospy.spin()
		
if __name__ == '__main__':
	rospy.init_node('xgo')
	node = xgo()
	node.main()
		



'''
[xgo move command]
    xgo.move_x 
    xgo.move_y 
    xgo.turn   
    xgo.forward
    xgo.back
    xgo.left
    xgo.right
    xgo.turnleft
    xgo.turnright

[xgo action command]
xgo.action(1) = sit
xgo.action(2) = stand
xgo.action(3) = crawl
xgo.action(4) = turn left
xgo.action(5) = turn right
xgo.action(6) = push up
xgo.action(7) = warigari FB
xgo.action(8) = warigari RL
xgo.action(9) = warigari RL2
xgo.action(10) = warigati and twist
xgo.action(11) = pee
xgo.action(12) = see uppeer
xgo.action(13) = arm shake
xgo.action(14) = stretching
xgo.action(15) = wave
xgo.action(16) = warigari dance
xgo.action(17) = sit and warigari dance
xgo.action(18) = ???
xgo.action(19) = hand shake

1
Lie down
2
Stand up
3
Crawl
4
Turn around
6
Squat
7
Turn roll
8
Turn pitch
9
Turn yaw
10
3 axis motion
11
Take a pee
12
Sit down
13
Wave hand
14
Give a stretch
15
Wave body
16
Wave side
17
Pray
18
Looking for food
19
Handshake

'''





#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def move():
    #Starts new node
    rospy.init_node('turtle_circle', anonymous =True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size = 10)
    vel_msg = Twist()
    while not rospy.is_shutdown():

        #Configuring Speed, both linear and angular
        #Linear Velocity
        vel_msg.linear.x=10
        vel_msg.linear.y=0
        vel_msg.linear.z=0
        #Angular Velocity
        vel_msg.angular.x=0
        vel_msg.angular.y=0
        vel_msg.angular.z=5#2D space
        velocity_publisher.publish(vel_msg)

if __name__ == "__main__":
    try:
        move()
    except rospy.ROSInterruptException: pass

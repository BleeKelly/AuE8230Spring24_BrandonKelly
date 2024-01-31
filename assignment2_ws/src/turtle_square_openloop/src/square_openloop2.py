#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import math

#Create Square Function
def square():
   #Defines Variables
    line_speed = 0.2
    turn_speed = 0.2
    distance_forward = 2
    turn_angle = math.pi

    #Node Setup   
    rospy.init_node('turtle_square_openloop',anonymous = True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size = 10)
    vel_msg = Twist()
    while not rospy.is_shutdown():
        #Draw First Line
        vel_msg.linear.x = line_speed
        vel_msg.linear.y = 0 
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0 
        vel_msg.angular.y = 0 
        vel_msg.angular.z = 0 
        current_distance = 0 
        
        t0=rospy.Time.now().to_sec()

        while(current_distance < distance_forward and ):
            velocity_publisher.publish(vel_msg)
            t1 = rospy.Time.now().to_sec()
            current_distance=line_speed*(t1-t0)
            print(vel_msg)
        vel_msg.linear.x = 0 
        velocity_publisher.publish(vel_msg)
    #Complete First Turn 

    #Draw Second Line
    #Complete Second Turn
    #Draw Third Line 
    #Complete Third Turn
    #Draw Fourth Line
    #Complete Fourth Turn
if __name__ == "__main__":
    try:
	    square()
    except rospy.ROSInterruptException: pass

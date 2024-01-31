#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import math
#Defines Variables
line_speed = 0.2
turn_speed = 0.2
distance_forward = 2
turn_angle = (math.pi/2)
#Create move and rotate functions

def mov():
    # Creates new node
    rospy.init_node('turtle_square_openloop', anonymous =True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    vel_msg = Twist()
    #Forward Movement
    vel_msg.linear.x=line_speed
    vel_msg.linear.y=0
    vel_msg.linear.z=0
    #Halt Rotational Movement
    vel_msg.angular.x=0
    vel_msg.angular.z=0 
    vel_msg.angular.z=0 
    #Publish Velocity 
    t0 = rospy.Time.now().to_sec()
    current_distance = 0 
    while(current_distance < distance_forward and not rospy.is_shutdown()):
        #print(current_distance)
        print(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_distance = line_speed * (t1-t0)
        velocity_publisher.publish(vel_msg)
    vel_msg.linear.x=0#Stops the turtle
    velocity_publisher.publish(vel_msg)

def rot():
    rospy.init_node('turtle_square_openloop',anonymous = True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size = 10)
    vel_msg = Twist()
    #Halt Forward Movement
    vel_msg.linear.x = 0 
    vel_msg.linear.y = 0 
    vel_msg.linear.z = 0 
    #Rotational Movement
    vel_msg.angular.x = 0 
    vel_msg.angular.y = 0 
    vel_msg.angular.z = turn_speed
    #Publish Velocity
    current_angle = 0 
    t0 = rospy.Time.now().to_sec()
    while (current_angle < turn_angle and not rospy.is_shutdown()):
        t1 = rospy.Time.now().to_sec()
        current_angle = turn_speed * (t1-t0)
        velocity_publisher.publish(vel_msg)
    vel_msg.angular.z = 0 
    velocity_publisher.publish(vel_msg)

#Create Square Function
def square():
    print("Square Step1")   
    while not rospy.is_shutdown():
        print("Square2")
    #Draw First Line 
        mov()
        print("square3")
    #Complete First Turn 
        rot()
    #Draw Second Line
        mov()
    #Complete Second Turn
        rot()
    #Draw Third Line 
        mov()
    #Complete Third Turn
        rot()
    #Draw Fourth Line
        mov()
    #Complete Fourth Turn
        rot()
if __name__ == "__main__":
    try:
        square()
    except rospy.ROSInterruptException:pass

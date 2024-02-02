# Assignment 2
## turtle_circle
This code makes the turtlesim turtle do circles. 

![turtle_circle](https://github.com/BleeKelly/AuE8230Spring24_BrandonKelly/assets/150833244/8dce209e-9183-407e-a01d-0e6dd244ede2)

### Installation
To install this package first clone the repo. Then go to your Catkin workspace src folder and run the command 

```
catkin_make_pkg turtle_circle geometry_msgs rospy
```
This will create a package workspace with the correct dependencies. You can then `cd` into the src folder and make directories for launch and script files using the command `mkdir launch scripts`.
At this point, you will want to create symbolic links to the git repo you cloned to do this run the following commands(with the correct path for your setup)

```
ln -s git_dir/assignment2_ws/turtle_circle/scripts/circle.py /package_path/scripts/circle.py
```
```
ln -s git_dir/assignment2_ws/turtle_circle/launch/circle.launch /package_path/launch/circle.launch
```
At this point, return to the top-level directory of your workspace. I typically will run `catkin_make` to be safe and then `source devel/setup.bash` At this point you can launch the package using the command 

```
roslaunch turtle_circle circle.launch
```

## turle_square_openloop
This code makes the turtlesim turtle draw a 2-unit square at a speed of 0.2 unit linearly and 0.2 radian/sec on turns
![turtle_square](https://github.com/BleeKelly/AuE8230Spring24_BrandonKelly/assets/150833244/c83d58be-1d7a-4622-84b8-83f935b30ab9)

### Installation
To install this package first clone the repo. Then go to your Catkin workspace src folder and run the command 

```
catkin_make_pkg turtle_square_openloop geometry_msgs rospy
```
This will create a package workspace with the correct dependencies. You can then `cd` into the src folder and make directories for launch and script files using the command `mkdir launch scripts`.
At this point, you will want to create symbolic links to the git repo you cloned to do this run the following commands(with the correct path for your setup)

```
ln -s git_dir/assignment2_ws/turtle_square_openloop/scripts/square_openloop.py /package_path/scripts/square_openloop.py
```
```
ln -s git_dir/assignment2_ws/turtle_square_openloop/launch/square_openloop.launch /package_path/launch/square_openloop.launch
```
At this point, return to the top-level directory of your workspace. I typically will run `catkin_make` to be safe and then `source devel/setup.bash` At this point you can launch the package using the command 

```
roslaunch turtle_circle circle.launch
```


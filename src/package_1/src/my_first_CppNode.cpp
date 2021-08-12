#include <ros/ros.h>

int main (int argc, char **argv)
{
	ros::init(argc, argv, "MyroscppNode");
	ros::NodeHandle nh;
	ROS_INFO("node initiated");
	ros::Rate rate(10);

	while (ros::ok())
	{
		ROS_INFO("node Run");
		rate.sleep();
	}
}

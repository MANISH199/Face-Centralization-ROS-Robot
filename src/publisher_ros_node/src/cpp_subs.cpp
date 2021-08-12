# include <ros/ros.h>
# include <std_msgs/String.h>
void fun_call(const std_msgs::String msg)
{
	ROS_INFO("subcribed data: %s " , msg.data.c_str());
}
int main (int argc, char **argv)
{
        ros::init(argc, argv, "cpp_subs_node");
        ros::NodeHandle nh;
        //ros::Publisher pub = nh.advertise<std_msgs::String>("/publisher_node_topic", 10);
	ros::Subscriber sub = nh.subscribe("/publisher_node_topic",1000,fun_call);
	ros::spin();
}


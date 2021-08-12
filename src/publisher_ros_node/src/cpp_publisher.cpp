# include <ros/ros.h>
# include <std_msgs/String.h>
int main (int argc, char **argv)
{
	ros::init(argc, argv, "cpp_publisher_node");
	ros::NodeHandle nh;
	ros::Publisher pub = nh.advertise<std_msgs::String>("/publisher_node_topic", 10);
	ros::Rate rate(.2);

	std_msgs::String store ;
	store.data = "a";
	while(ros::ok())
	{
		std_msgs::String msg;
		if (store.data == "a")
		{
			store.data = "b";
		}
		else if (store.data == "b")
		{
			store.data = "c";
		}
		else if (store.data == "c")
		{
			store.data = "a";
		}
		msg.data =store.data;
		pub.publish(msg);
		rate.sleep();
	}

}

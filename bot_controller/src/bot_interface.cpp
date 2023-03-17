#include "bot_controller/bot_interface.h"
#include <std_msgs/Int16MultiArray.h>
#include <bot_controller/AnglesConverter.h"

BotInterface::BotInterface(ros::NodeHandle& nh) : nh_(nh), pnh_("-"), pos_(4,0), vel_(4,0), eff_(4,0), cmd_(4,0),  names_("joint_1", "joint_2", "joint_3", "joint_5") {
    hardware_pub_ = pnh_.advertise<std_msgs::UInt16MultiArray>("/arduino/arm_actuate", 1000);
    hardware_srv_ = pnh_.serviceClient<bot_controller::AnglesConverter>("/rad_to_degrees")
    
}
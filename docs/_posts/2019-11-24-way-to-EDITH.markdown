---
layout: post
title:  "Way to EDITH"
date:   2019-11-24 08:00:00 +0530
categories: drones
---
Many curious questions left at the end of this week. What is JDERobot exactly? How exactly to use the ICE Framework? Where is it being used in JDERobot? 


### The COOL part!

![Drone](https://media2.govtech.com/images/940*630/DroneFeature1.jpg)

After merging of the pull request, I wanted to solve some other exercise, [follow_road](https://github.com/JdeRobot/RoboticsAcademy/tree/master/exercises/follow_road). Seeing unknown terms like mavros and PX4, my curious mind decided to read about it before working on solving the problem. So, here is what I read:

Unmanned robotic vehicles remotely or autonomously controlled are called drones. Since my birth(or till heard the word 'drone'), I considered only autonomous flying robots as a drone, but almost all vehicles, be it aerial, underwater or ground are considered drones.

**Please Note that I will be using the word Drone for unmanned aerial vehicles, inspite of telling the difference in the first sentence.**

Acurate and quick control are major concerns while controlling an aerial drone. Therefore, control of these drones require special software and hardware for appropriate control.

In a nutshell, the "brain" of the drone is called an autopilot. It consists of flight stack software running on the drone controller hardware. The drone controller hardware is given commands from another software called the Ground Control Station.

![Something just like this](https://raw.githubusercontent.com/MishkaRogachev/JAGCS/master/ui.png)

[Pixhawk](https://pixhawk.org/) is one such open source hardware project that provides autopilot hardware designs. Pixhawk supports flight stacks such as [PX4](https://px4.io/) or [Ardupilot](http://ardupilot.org/), that run on the OS [NuttX](https://nuttx.org/).

[MAVLink](https://en.wikipedia.org/wiki/MAVLink), Micro Air Vehicle is one of those protocols used for communicating with aerial drones, from a ground control station. Apart from commands, orientation of vehicle, GPS location and speed can be communicated to the drone as well.

[QGroundControl](http://qgroundcontrol.com/) is an example of a Ground Control Station that utilises MAVLink protocol, that runs on almost all platforms, be it Windows, Android or MacOS.

Loads of definitions! But, these are the practical aspects that are currently in use. Have to read about the basics as well in order to learn better about them.

Just for everyone's information, the title of this blog is inspired from the movie SpiderMan: Far from Home, in which Tony Stark(Iron Man) developed a drone based project called EDITH. It was really fun reading about the autopilot systems as I was continously inspired by the thought of making such fiction come into life, hence the title. 

[EDITH](../assets/edith.gif)

### Loads of Questions!

Another task I had this week, was to read about the Ice framework. JDERobot uses the ICE framework behind some of its applications, so this was a great thing to read about.

The journey started with this [research-paper](https://gsyc.urjc.es/jmplaza/papers/waf2016-roscompatibility.pdf) written by 2 great people. It was fun reading the paper, as I could understand it quite well. The paper involved the translation of existing JDERobot components to ROS based implementation. On to Ice,

[Ice by ZeroC](https://zeroc.com/products/ice) is an [RPC](https://en.wikipedia.org/wiki/Remote_procedure_call)(Remote Procedure Call) based framework. What makes Ice useful are it's object oriented client-server based applications. These client-server applications can be written in different languages, a lot of different languages, C++, C#, Java, Javascript, Python and more(as written on the official website).

After this amount of theory, lets get practical now!

![Practical](../assets/practical.jpg)


Getting practical started with looking at the documentation and some example codes of the project. But as everyone knows, only reading about implementation is whole lot different than using it in practical designs. Therefore, getting an overview was enough for now, the implementation will be learned with time.

![Quote for Learning](https://spiritualcleansing.org/wp-content/uploads/2015/04/Tell-me-and-I-forget-teach-me-and-I-may-remember-involve-me-and-I-learn..jpg)

Hence, I thought the best use case of this learning would be to see where and how is it being used in JDERobot. Quite a lot of searching the repository left me more curious, as I have still not figured out where Ice is being used! Hence, the task for next week would be more reading and doubt clearance.

### References

[DOCS PX4](https://docs.px4.io/v1.9.0/en/getting_started/px4_basic_concepts.html)

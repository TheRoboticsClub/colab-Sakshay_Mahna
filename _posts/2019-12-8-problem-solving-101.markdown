---
layout: post
title:  "Problem Solving 101"
date:   2019-12-08 8:00:00 +0530
categories: productivity
---
The cons of not following a step by step approach and taking on everything all at once!


### Address to a previous question

In one of my previous blogs, particularly [this one](https://theroboticsclub.github.io/colab-Sakshay_Mahna/2019-11-23-way-to-edith/), I referred to a question that I did not understand what exactly was JDERobot? Well, José Sir explained to me what it was, and I forgot to mention the answer in my previous blog, [this one](https://theroboticsclub.github.io/colab-Sakshay_Mahna/2019-12-02-os-upgrade/). So, here we are answering it!

![JDERobot](https://i.ytimg.com/vi/R-0AEXS3Wj0/maxresdefault.jpg)

In simple words, JDERobot is a robotics-toolkit to help develop advanced robotics applications. Previously, JDERobot used [ICE framework by ZeroC](https://zeroc.com/products/ice). But, keeping in mind the development of ROS. JDERobot shifted to using ROS as its main framework. ROS provides almost all the drivers that any robotics application requires. If any driver is not available, the JDERobot developers develop and use it as per their convenience(#Engineering Stuff). But, Robotics Academy is the main project of JDERobot, helping people practice and learn programming robots. 

![Robotics Academy](https://jderobot.github.io/assets/images/projects/robotics-academy-action.jpg)

### Task for this week

Let's get back to this week's work. To put it straight, I was **not able** to complete this week's task. But, made some amount of progress which I can share on the blog. This week's task was to implement the VFF(Virtual Force Field) algorithm on the [obstacle_avoidance exercise](https://jderobot.github.io/RoboticsAcademy/portfolio/obstacle_avoidance/).

![Failure](http://1zl13gzmcsu3l9yq032yyf51-wpengine.netdna-ssl.com/wp-content/uploads/2017/12/Henry-Ford-2.jpg)

### How not to solve problems

Engineers are problem solvers. The best profession in the world(according to me). This week's task had quite a lot of problems to deal with. So let's get onto them. The first problem, the exercise mentioned on the webpage and actual file do not match! However, the launch file of the problem on the webpage is available in the program files of the application. This was easy to deal with, just implement the user interface of the given exercise on the another launch file. But, this comes with an additional problem, the target waypoints to follow are according to the exercise that I do not want to run, hence I have to adjust the waypoints as well. No problem, will deal with it **later**.

Second problem; the user interface has a little problem. The vectors that represent the direction of car, obstacle direction and target direction are a bit mismatched! After thorough checking and working through the exercise, I found that the X and Y directions of the vectors are mismatched. This causes a lot of confusion while debugging the error. No problem, found a simple way around that can be permanently fixed, **later**.

Third problem, the implementation is itself. The implementation is not as simple as it looked in the research paper of the algorithm. After getting done with the above problems, I can get done with this problem **later**.

Well, this is not how we should solve our problems. Keep everything to **later** and then come back realising nothing is solved and everything is left to **later**. We should always follow a systematic approach, solving all the problems one by one.(Reference: The book [Problem Solving 101](https://drive.google.com/file/d/0B1UQmV-A_nboeXlpTHYyb1NUcG9sVjZsLUFzRi1odTdXVEdj/view?usp=sharing) The book is on my personal drive!)

![Problem Solving 101](https://images-na.ssl-images-amazon.com/images/I/51Ijf3bqMhL._SX314_BO1,204,203,200_.jpg)

From next week onwards, I would try my best to implement the algorithm and get all the problems solved and not put everything to **later**.

### A personal thing to share

I usually do not like putting personal thing over the blog posts. But, this one thing was really tempting to put on! [The Construct](https://twitter.com/_TheConstruct_), an organization that teaches ROS, [awarded me](https://twitter.com/_TheConstruct_/status/1202738313867730944) with a really cool ROS Developer T-shirt, on successfully solving the ROS Challenge of the Week. One more source of motivation, to keep working hard and love Robotics!

![ROS Developer](https://vangogh.teespring.com/v3/image/t4znMRjs25w0vaExHwmMuXvN8UA/560/560.jpg)

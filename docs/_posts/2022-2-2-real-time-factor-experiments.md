---
layout: post
title:  "Real Time Factor Experiments"
date:   2022-02-02 10:30:00 +0530
categories: rtf
---
The RTF (Real Time Factor) plays a crucial role in determining the performance of the network. According to qualitative experiments (visually observing behavior), the NARX network is able to complete a difficult curve in Montmelo Circuit when the RTF is reduced. In this blog post, we study the effects of changing Real Time Update Rate on NARX network quantitatively for Simple Circuit.

Following are some of the graphs. The X axis shows the Real Time Update Rate set in Gazebo and the Y axis shows the corresponding quantity under study.

## Real Time Factor

![Real Time Factor](../assets/2022-2-2-real-time-factor-experiments/real_time_factor.png)

*Comparision of Real Time Factor*

## Position Deviation (MAE)

![MAE](../assets/2022-2-2-real-time-factor-experiments/position_deviation_mae.png)

*Comparision of Position Deviation (MAE)*

## Lap Seconds

![Lap Seconds](../assets/2022-2-2-real-time-factor-experiments/lap_seconds.png)

*Comparision of Lap Seconds*

## Average Speed

![Average Speed](../assets/2022-2-2-real-time-factor-experiments/average_speed.png)

*Comparision of Average Speed*

## Frame Rate

![Frame Rate](../assets/2022-2-2-real-time-factor-experiments/frame_rate.png)

*Comparision of Frame Rate*

## Mean Iteration Time

![Mean Iteration Time](../assets/2022-2-2-real-time-factor-experiments/mean_brain_iteration_time.png)

*Comparision of Mean Iteration Time*

## Mean Inference Time

![Mean Inference Time](../assets/2022-2-2-real-time-factor-experiments/mean_inference_time.png)

*Comparision of Mean Inference Time*

## Mean ROS Iteration Time

![ROS Iteration Time](../assets/2022-2-2-real-time-factor-experiments/mean_ros_iteration_time.png)

*Comparision of Mean ROS Iteration Time*

## Observations

1. The RTF graph is similar for 1000 and 500 Real Time Update Rate. The change takes place for smaller values of 100 and 50.

2. The Mean Iteration Time, Mean Inference Time and Mean ROS Iteration Time show an increasing trend with the reduction of the Real Time Update Rate. A similar trend can be observed for the Lap Time. A decreasing trend is observed for Position Deviation.

3. The Frame Rates for all the different Real Time Update Rates are quite low.

## Conclusions

The main objective of conducting these experiments was to determine the capabilities of my computer. From the RTF graph, it is clearly visible that the computer is not able to achieve the desired performance with 1000 and 500 Real Time Update Rates. The best performance is given by 100 and 50. The other graphs also point out a similar conclusion. Hence, intuitively, 100 should be the most optimal value for conducting experiments as this value allows the simulator to run well and algorithm that is running on it.

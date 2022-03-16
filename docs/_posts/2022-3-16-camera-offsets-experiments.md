---
layout: post
title:  "Camera Offset Experiments"
date:   2022-3-16 10:30:00 +0530
categories: sdf
---
Generaly, Neural Network based algorithms should be more robust compared to hard coded algorithms. A similar case should be expected for our Visual Control algorithm as well. In this post, we study the performance of the brains by changing the camera position.

# Camera Offset

The images obtained by different camera positions are:

Original                   |  Left                    |  Right                    |  Rotate Up                    |  Rotate Down                    |
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:
![](../assets/2022-3-16-camera-offsets-experiments/simple-first.png) | ![](../assets/2022-3-16-camera-offsets-experiments/left-first.png) | ![](../assets/2022-3-16-camera-offsets-experiments/right-first.png) | ![](../assets/2022-3-16-camera-offsets-experiments/up-first.png) | ![](../assets/2022-3-16-camera-offsets-experiments/down-first.png)

# PilotNet

Following are the graphs

## Position Deviation Error

![Error](../assets/2022-3-16-camera-offsets-experiments/pilotnet-err.png)

*Comparision of Position Deviation Error*

## Position Deviation (MAE)

![MAE](../assets/2022-3-16-camera-offsets-experiments/pilotnet-mae.png)

*Comparision of Position Deviation (MAE)*

## Percentage Completed

![MAE](../assets/2022-3-16-camera-offsets-experiments/pilotnet-percentage.png)

*Comparision of Percentage Completed*

## Lap Seconds

![Lap Seconds](../assets/2022-3-16-camera-offsets-experiments/pilotnet-seconds.png)

*Comparision of Lap Seconds*

## Average Speed

![Average Speed](../assets/2022-3-16-camera-offsets-experiments/pilotnet-speed.png)

*Comparision of Average Speed*

# Deepest LSTM Tiny PilotNet

Following are the graphs

## Position Deviation Error

![Error](../assets/2022-3-16-camera-offsets-experiments/lstm-err.png)

*Comparision of Position Deviation Error*

## Position Deviation (MAE)

![MAE](../assets/2022-3-16-camera-offsets-experiments/lstm-mae.png)

*Comparision of Position Deviation (MAE)*

## Percentage Completed

![MAE](../assets/2022-3-16-camera-offsets-experiments/lstm-percentage.png)

*Comparision of Percentage Completed*

## Lap Seconds

![Lap Seconds](../assets/2022-3-16-camera-offsets-experiments/lstm-seconds.png)

*Comparision of Lap Seconds*

## Average Speed

![Average Speed](../assets/2022-3-16-camera-offsets-experiments/lstm-speed.png)

*Comparision of Average Speed*

# Explicit Method

Following are the graphs

## Position Deviation Error

![Error](../assets/2022-3-16-camera-offsets-experiments/explicit-err.png)

*Comparision of Position Deviation Error*

## Position Deviation (MAE)

![MAE](../assets/2022-3-16-camera-offsets-experiments/explicit-mae.png)

*Comparision of Position Deviation (MAE)*

## Percentage Completed

![MAE](../assets/2022-3-16-camera-offsets-experiments/explicit-percentage.png)

*Comparision of Percentage Completed*

## Lap Seconds

![Lap Seconds](../assets/2022-3-16-camera-offsets-experiments/explicit-seconds.png)

*Comparision of Lap Seconds*

## Average Speed

![Average Speed](../assets/2022-3-16-camera-offsets-experiments/explicit-speed.png)

*Comparision of Average Speed*

# Observations

1. Car having the camera rotated up, never completes the circuit.

2. For the Deep Learning brains, the rotate up and rotate down, both of them do not complete the circuit. However, the rotate down completes the lap for Explicit Brain.

3. The Right and Left camera offsets are able to complete the circuits, but, have a higher error compared to the original camera position. 

# Conclusions

It was expected for the PilotNet and DeepestLSTM networks to perform well for the Left, Right and Rotated Down camera offsets. For Left and Right, this was well observed, but for Rotate Down the brains did not perform the same. This may be due to the croping that is done before processing the image. Due to that, a particular field of view of the image may be blocked that is helpful for the network to work.

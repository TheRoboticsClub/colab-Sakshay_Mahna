---
layout: post
title:  "Deep Learning Studio"
date:   2022-01-21 13:30:00 +0530
categories: deep-learning
---
Hello Engineers! It's been a long time since I have written any post on this blog. I wish to start it again, let's see how it goes! Currently, I am working on a different project: Deep Learning Studio. In this project, the aim is to research and study different Neural Network based control mechanisms (obviously on Robots). Therefore, the next blogs will be on the same.

**PS** This rejuvenation of this blog was inspired by the latest weekly meeting of this project. Seeing Sergio's (member of the Deep Learning Studio project) PhD [blog](https://roboticslaburjc.github.io/2019-phd-sergio-paniego/), it was interesting to see how all the research related to the project can be compiled in an easy to read format, and additionally provides some accountability to present more readable results.

## Summary
The work done on the project till now is summarised, so it is easier to follow up from the next blog. The problem statement we are working on is: Make an automatic F1 Car follow a red line around the circuit, using a CNN based control. Currently, our aim is to study the advantage/disadvantage of memory on Neural Networks for control. In total, we have 5 different circuits that the car is tested on: The Simple Circuit, The Many Curves Circuit, The Montmelo Circuit, The Montreal Circuit and The Nurburgring Circuit. Of these, The Montemelo Circuit is the toughest.

Till now, we have 2 baseline implementations: Explicit and PilotNet. Explicit is a hard code based strategy, where we code a red color filter, and tune PID controller to make the car go round the circuit. The PilotNet is a CNN based strategy, which has been trained on images collected from running the Explicit Brain around the circuits. The data for training has primarily been collected from two set of circuits, The Simple Circuit and The Many Curves Circuit.

To improve over the baselines using memory based networks, our group has been working on 4 approaches, Explicit Memory, LSTM, Conv3D LSTM and NARX. Explicit Memory approach is being covered by Utkarsh and LSTM and Conv3D LSTM are being covered by Sergio. I am currently working on the NARX network approach.

This is it for a brief introduction to the current state of the project. From next post onwards, we will compile the results and study conducted for each week (or 2 weeks).
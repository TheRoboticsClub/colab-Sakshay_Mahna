FROM jderobot/ubuntu:ros-melodic
WORKDIR ./
COPY . ./

RUN apt-get update
RUN apt-get install vim -y
RUN apt-get install xvfb -y
RUN Xvfb :0 -screen 0 1024x768x16 &> xvfb.log  &
RUN DISPLAY=:0
RUN export DISPLAY

RUN pip install websocket_server

EXPOSE 2303
EXPOSE 1905


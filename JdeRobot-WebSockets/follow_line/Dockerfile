FROM python:2.7
WORKDIR ./
COPY . ./
RUN pip install websocket_server
EXPOSE 2303
EXPOSE 1905
CMD ls
CMD python ./host.py


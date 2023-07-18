FROM ubuntu:20.04

WORKDIR /home/shreejam/sgx-demo

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN pip install flask
RUN pip install pyopenssl

COPY sqlite.py ./
COPY templates ./templates
COPY app.py ./
COPY patients.db ./

CMD python3 app.py

#docker build -t app .
#docker run -it -p 5000:5000 app
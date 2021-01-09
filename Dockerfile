FROM ubuntu:bionic-20201119

#create the environment
RUN apt-get update
RUN apt-get -y install python3-pip
RUN apt-get -y install htop

RUN mkdir -p /header_extractor

# install requirements first
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools
COPY ./requirements.txt /header_extractor/requirements.txt
RUN pip3 install -r /header_extractor/requirements.txt

# Copy code (mounted in development)
COPY ./ /header_extractor/

WORKDIR /header_extractor
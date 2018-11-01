FROM continuumio/miniconda3

#########################################
# Generate Poetry!
# 
# docker build -t vanessa/40-avocados .
# docker run vanessa/40-avocados
#########################################

LABEL maintainer vsochat@stanford.edu
LABEL VERSION 0.0.1

RUN apt-get update && apt-get install -y git
RUN /opt/conda/bin/pip install --upgrade pip && \
    /opt/conda/bin/pip install pyaml==17.12.1

RUN mkdir /code
ADD . /code

ENTRYPOINT ["/opt/conda/bin/python", "/code/writePoetry.py"]

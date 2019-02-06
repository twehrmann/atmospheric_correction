FROM ubuntu:18.04
LABEL Description="SIAC image" Version="1.0"
ENV DEBIAN_FRONTEND=noninteractive
ENV LANG C.UTF-8

MAINTAINER Thilo Wehrmann <thilo.wehrmann@eoss.cloud>

RUN sed -i 's|http://us.|http://|g' /etc/apt/sources.list
RUN apt-get update && apt-get install software-properties-common -y

RUN apt-get update && apt-get install -y ssh python python-dev python3.6 python3.6-dev python-pip python3-pip virtualenv libssl-dev libpq-dev git build-essential libfontconfig1 libfontconfig1-dev
RUN apt-get update && apt-get install -y gdal-bin libgdal-dev libgnutls28-dev libspatialindex-dev
RUN pip install setuptools pip --upgrade --force-reinstall

# OS block
RUN apt-get install git curl -y

RUN apt-get install apt-transport-https ca-certificates curl software-properties-common -y
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable " && apt-get update && apt-cache policy docker-ce && apt-get install -y docker-ce

RUN apt-get install -y grep sed dpkg && \
    TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o "/v.*\"" | sed 's:^..\(.*\).$:\1:'` && \
    curl -L "https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb" > tini.deb && \
    dpkg -i tini.deb &&  rm tini.deb &&  apt-get clean

RUN pip install --upgrade pip



RUN apt-get install -y gdal-bin python-gdal python3-gdal
RUN python3 -m pip install numpy

# manual installation of ...
RUN python3 -m pip install pycurl


#RUN pip install https://github.com/multiply-org/atmospheric_correction/archive/master.zip
ADD . /tmp/SIAC
WORKDIR /tmp/SIAC/

RUN python3 -m pip install -r requirements.txt
RUN python3 setup.py install

ENTRYPOINT [ "/usr/bin/tini", "--" ]

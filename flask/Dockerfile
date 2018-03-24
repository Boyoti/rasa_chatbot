#Dockerfile for flask containerization
FROM centos:latest
MAINTAINER Brian Hopkins "brianhh1230@gmail.com"
RUN yum update -y && yum clean all
RUN yum -y install epel-release https://centos7.iuscommunity.org/ius-release.rpm && yum clean all
RUN \
  yum -y install python36u python36u-pip build-essentials python36u-devel && \
  yum clean all

# Set the locale
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

COPY . /app
WORKDIR /app
RUN pip3.6 install -r requirements.txt
ENTRYPOINT ["python3.6"]
CMD ["app.py"]

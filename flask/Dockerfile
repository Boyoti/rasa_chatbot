#Dockerfile for flask containerization
FROM centos:latest
MAINTAINER Brian Hopkins "brianhh1230@gmail.com"
RUN yum update -y && yum clean all
RUN yum -y install epel-release && yum clean all
RUN \
  yum -y install python python-pip build-essentials python-devel && \
  yum clean all

# Set the locale
RUN localedef -i en_US -f UTF-8 en_US.UTF-8


COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]

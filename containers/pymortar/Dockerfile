FROM jupyter/scipy-notebook

USER root

# install dependencies
RUN apt-get update
RUN pip install --upgrade pip
RUN pip install numpy pytz pandas grpcio pymortar protobuf googleapis-common-protos pyarrow
RUN pip install --upgrade numpy
#RUN apt-get install 

ADD analytics /home/jovyan/
ENV MORTAR_API_ADDRESS api.mortardata.org:9001

# execute
ADD run.sh /opt/run.sh
ENTRYPOINT /opt/run.sh

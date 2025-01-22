FROM ubuntu:24.04

RUN apt update && apt install -y python3-pip python3-venv
#	&& python3 -

SHELL ["/bin/bash"]

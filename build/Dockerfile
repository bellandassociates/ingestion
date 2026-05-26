FROM python:latest

WORKDIR /workdir
RUN apt-get upgrade && apt-get update && apt-get install -y vim

COPY ./build/requirements.txt .
RUN pip install -r requirements.txt

CMD ["/bin/bash"]

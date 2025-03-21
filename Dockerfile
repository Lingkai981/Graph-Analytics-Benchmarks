FROM ubuntu

RUN apt-get update && apt-get install -y \
    g++

WORKDIR /artifacts

COPY . /artifacts

CMD ["echo", "hello"]

FROM ubuntu:20.04

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && \
    apt-get install -y \
    g++ \
    make \
    cmake \
    git \
    curl \
    zip \
    unzip \
    tar \
    ninja-build \
    python3-jinja2 \
    pkg-config \
    gcc \
    clang \
    && rm -rf /var/lib/apt/lists/*

# RUN git clone https://github.com/emscripten-core/emsdk.git
# # Download and install the latest SDK tools.
# RUN cd ./emsdk
# RUN chmod +x ./emsdk
# RUN ./emsdk install latest
# RUN chmod +x ./emsdk_env.sh
# RUN source ./emsdk_env.sh
WORKDIR /workspace
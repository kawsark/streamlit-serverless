# syntax=docker/dockerfile:1.4
FROM python:3.11-slim

ARG USERNAME=ec2-user
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Create the user
RUN groupadd --gid $USER_GID $USERNAME
RUN useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

WORKDIR /app

# Install pre-reqs
#RUN apk update && apk add cmake libstdc++ g++
RUN apt update -y && apt install cmake g++ gcc curl unzip -y

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# # Install AWS CLI
# RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
# RUN unzip awscliv2.zip
# RUN ./aws/install
# RUN aws --version

# Copy files
COPY photoai-streamlit.py /app/
COPY requirements.txt /app/
COPY photoailib /app

RUN pip3 install -r requirements.txt

RUN chown $USERNAME:$USERNAME /app

USER $USER

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "photoai-streamlit.py", "--server.port=8501", "--server.address=0.0.0.0"]

#!/bin/bash

echo "Installing Docker..."

sudo apt update

sudo apt install -y docker.io

sudo systemctl enable docker
sudo systemctl start docker

sudo usermod -aG docker ubuntu
sudo usermod -aG docker jenkins

docker --version

echo "Docker Installed Successfully"
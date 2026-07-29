#!/bin/bash

echo "Installing Java..."

sudo apt update
sudo apt install -y fontconfig openjdk-21-jre

java -version

echo "Java Installed Successfully"
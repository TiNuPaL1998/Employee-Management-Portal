#!/bin/bash

echo "Installing AWS CLI..."

cd /tmp

curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"

sudo apt install -y unzip

unzip -o awscliv2.zip

sudo ./aws/install --update

aws --version

echo "AWS CLI Installed Successfully"
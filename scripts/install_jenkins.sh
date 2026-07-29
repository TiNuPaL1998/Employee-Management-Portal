#!/bin/bash

echo "Installing Jenkins..."

sudo wget -O /usr/share/keyrings/jenkins-keyring.asc \
https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key

echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]" \
https://pkg.jenkins.io/debian-stable binary/ | \
sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null

sudo apt update

sudo apt install -y jenkins

sudo systemctl enable jenkins
sudo systemctl start jenkins

sudo systemctl status jenkins --no-pager

echo "Jenkins Installed Successfully"
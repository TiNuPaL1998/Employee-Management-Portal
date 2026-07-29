#!/bin/bash

set -e

echo "========================================="
echo " Starting DevOps Server Bootstrap"
echo "========================================="

chmod +x *.sh

./install_java.sh
./install_git.sh
./install_docker.sh
./install_awscli.sh
./install_jenkins.sh

echo ""
echo "========================================="
echo " Bootstrap Completed Successfully"
echo "========================================="
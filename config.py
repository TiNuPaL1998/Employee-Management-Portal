"""
Project Configuration
---------------------
This file contains all configurable values used by deploy.py.
Update these values if your project structure changes.
"""

import os

# -----------------------------
# Project Information
# -----------------------------
PROJECT_NAME = "Employee-Management-Portal"

# Root directory of the project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Flask application entry point
APP_FILE = "app.py"

# Virtual Environment
VENV_NAME = "venv"

# Requirements file
REQUIREMENTS_FILE = "requirements.txt"

# -----------------------------
# Linux Paths
# -----------------------------
PROJECT_PATH = "/home/ubuntu/Employee-Management-Portal"

NGINX_CONFIG_SOURCE = "scripts/employee-management.conf"
NGINX_CONFIG_DESTINATION = "/etc/nginx/sites-available/employee-management"

GUNICORN_SERVICE_SOURCE = "scripts/gunicorn.service"
GUNICORN_SERVICE_DESTINATION = "/etc/systemd/system/gunicorn.service"

# -----------------------------
# Services
# -----------------------------
NGINX_SERVICE = "nginx"
GUNICORN_SERVICE = "gunicorn"

# -----------------------------
# Packages
# -----------------------------
SYSTEM_PACKAGES = [
    "git",
    "python3",
    "python3-pip",
    "python3-venv",
    "nginx",
    "curl",
    "unzip"
]

# -----------------------------
# AWS CLI
# -----------------------------
AWS_DOWNLOAD_URL = "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip"

# -----------------------------
# Health Check
# -----------------------------
APPLICATION_URL = "http://localhost"

# -----------------------------
# Log File
# -----------------------------
LOG_FILE = "deploy.log"
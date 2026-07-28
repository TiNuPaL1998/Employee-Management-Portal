"""
Utility functions for Deployment Automation
"""
from deployment import utils
import subprocess
import logging
import sys
from datetime import datetime

import config

# ----------------------------------------------------
# Configure Logging
# ----------------------------------------------------
logging.basicConfig(
    filename=config.LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# ----------------------------------------------------
# Console Output
# ----------------------------------------------------
def info(message):
    print(f"[INFO] {message}")


def success(message):
    print(f"[SUCCESS] {message}")


def warning(message):
    print(f"[WARNING] {message}")


def error(message):
    print(f"[ERROR] {message}")


# ----------------------------------------------------
# Logging
# ----------------------------------------------------
def log(message):
    logging.info(message)


# ----------------------------------------------------
# Execute Shell Commands
# ----------------------------------------------------
def run_command(command):
    """
    Runs a shell command.

    Example:
        run_command(["python", "--version"])
    """

    info("Running: " + " ".join(command))

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True
        )

        if result.stdout.strip():
            print(result.stdout)

        return True

    except subprocess.CalledProcessError as e:

        error(e.stderr)

        log(e.stderr)

        return False


# ----------------------------------------------------
# Ask User
# ----------------------------------------------------
def confirm(message):

    choice = input(f"{message} (y/n): ")

    return choice.lower() == "y"
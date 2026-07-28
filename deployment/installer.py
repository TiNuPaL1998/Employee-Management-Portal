"""
Installer Module
"""

from deployment import utils
import config


def setup():

    utils.info("Updating package list...")

    utils.run_command(["sudo", "apt", "update"])

    utils.info("Installing required packages...")

    command = [
        "sudo",
        "apt",
        "install",
        "-y",
    ] + config.SYSTEM_PACKAGES

    utils.run_command(command)

    utils.success("System packages installed successfully.")
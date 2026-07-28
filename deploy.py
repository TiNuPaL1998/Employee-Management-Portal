"""
Deployment Automation Tool
Author: Tinu

Usage:
    python deploy.py setup
    python deploy.py deploy
    python deploy.py status
    python deploy.py health
    python deploy.py aws
"""
from deployment import utils
import sys
from deployment import installer


def setup():

    utils.info("Starting setup...")

    utils.run_command(["python3", "--version"])

    utils.success("Setup completed.")


def deploy():
    utils.info("Deploying application...")


def status():
    utils.info("Checking system status...")


def health():
    utils.info("Checking application health...")


def aws():
    utils.info("Performing AWS CLI operations...")

def help_menu():
    utils.info("\nAvailable Commands:\n")
    utils.info("  setup    - Prepare server")
    utils.info("  deploy   - Deploy application")
    utils.info("  status   - Check server status")
    utils.info("  health   - Health check")
    utils.info("  aws      - AWS CLI operations")


def main():
    if len(sys.argv) < 2:
        help_menu()
        return

    command = sys.argv[1].lower()

    commands = {
        "setup": setup,
        "deploy": deploy,
        "status": status,
        "health": health,
        "aws": aws,
    }

    if command in commands:
        commands[command]()
    else:
        print(f"❌ Unknown command: {command}")
        help_menu()


if __name__ == "__main__":
    main()
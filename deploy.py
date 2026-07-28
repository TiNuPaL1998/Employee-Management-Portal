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


def setup():

    utils.info("Starting setup...")

    utils.run_command(["python", "--version"])

    utils.success("Setup completed.")


def deploy():
    print("📦 Deploying application...")


def status():
    print("📊 Checking system status...")


def health():
    print("❤️ Checking application health...")


def aws():
    print("☁️ AWS CLI Operations...")


def help_menu():
    print("\nAvailable Commands:\n")
    print("  setup    - Prepare server")
    print("  deploy   - Deploy application")
    print("  status   - Check server status")
    print("  health   - Health check")
    print("  aws      - AWS CLI operations")


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
import os
import subprocess
import sys

def install_requirements():
    """Устанавливает зависимости"""
    print("📦 Устанавливаю зависимости...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def start_bot():
    """Запускает бота"""
    print("🚀 Запускаю бота...")
    os.execvp(sys.executable, [sys.executable, "balance_analyzer.py"])

if __name__ == "__main__":
    install_requirements()
    start_bot()

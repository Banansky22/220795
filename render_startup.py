import os
import sys

if __name__ == "__main__":
    # Просто запускаем основной файл
    os.execvp(sys.executable, [sys.executable, "balance_analyzer.py"])

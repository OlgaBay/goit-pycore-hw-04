from pathlib import Path
from colorama import Fore, Style
import sys

# виводить в терміналі список всіх піддиректорій та файлів у вказаній директорії
def show_directory(directory, level = 0):
    directory = Path(directory)
    # відступ для візуального відображення рівня вкладеності
    indent = " " * ((level + 1) * 2)

    if not directory.exists():
        print("Директорії не існує")
        return
    if not directory.is_dir():
        print("Це не директорія")
        return
    
    try:   
        if level == 0:
            print(Fore.YELLOW + f"📦 {directory.name}" + Style.RESET_ALL)
        for item in directory.iterdir():
            if item.is_dir():
                print(Fore.LIGHTBLUE_EX + f"{indent} 📂 {item.name}" + Style.RESET_ALL)
                show_directory(item, level + 1)    
            else:
                print(Fore.LIGHTGREEN_EX + f"{indent} 📄 {item.name}" + Style.RESET_ALL)

    except PermissionError:
        print("Немає доступу до директорії")

if len(sys.argv) > 1:
    show_directory(sys.argv[1])
else: 
    print("Вкажіть шлях до директорії")
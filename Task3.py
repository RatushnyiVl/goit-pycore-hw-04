from colorama import Fore, Style
import sys
from pathlib import Path

main_path = Path(sys.argv[1])
print(f'{Fore.RED}{Style.BRIGHT} {main_path.name}/')

def read_folder(path, indent=1):
    spacing = "   " * indent
    try:
        for el in path.iterdir():
            if el.is_dir(): # folder
                print(spacing, Fore.BLUE,Style.BRIGHT, el.name, '/', sep='')
                read_folder(el, indent + 1) # nested folder
            else: #file
                print(spacing, Fore.GREEN, Style.BRIGHT, el.name, sep='')
    except PermissionError:
        print(f'{spacing}{Fore.RED}No permission to: {el}{Style.RESET_ALL}')
    except FileNotFoundError:
        print(f'{spacing}{Fore.RED}No such a directory{Style.RESET_ALL}')
    except Exception as e:
        print(f'{spacing}{Fore.RED}Error occurred: {e}{Style.RESET_ALL}')

read_folder(main_path)

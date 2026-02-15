from pathlib import Path
from colorama import Fore

# path = '../test_dir'
path = input('Enter path: ')

def print_files(path_str: str, tab=0):
    directory = Path(path_str)

    if not directory.exists():
        print(Fore.RED, f'{tab * " "}{directory} does not exist')
        return

    if directory.is_file():
        print(Fore.RED, f'{tab * " "}{directory} is a file')
        return

    def print_directory(directory2: Path, tab=0):
        print(Fore.YELLOW, f'{tab * "  "}{directory2.name}/')
        for file in directory2.iterdir():
            if file.is_dir():
                print_directory(file, tab + 1)
                continue
            print(Fore.BLUE, f'{(tab + 1) * "  "}{file.name}')

    print_directory(directory)

print_files(path)
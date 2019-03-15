from pathlib import Path

def get_path():
    p = Path('.')
    dir_list = [x for x in p.iterdir() if x.is_dir()]
    print(dir_list)
    p = Path('~/abc')

if __name__ == '__main__':
    get_path()


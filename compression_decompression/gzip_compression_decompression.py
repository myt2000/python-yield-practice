import gzip
import shutil

if __name__ == "__main__":
    content = b"Lots of content here"
    with open('D:/demo/sort_seq.py', 'rb') as f_in:
        with gzip.open('D:/demo/sort_seq.py.gz', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

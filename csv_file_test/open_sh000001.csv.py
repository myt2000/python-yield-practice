import csv

def get_sh_csv():
    with open('D:/new_tdx/vipdoc/sz/pythondata/sz000001.csv') as f:
        # reader = csv.DictReader(f)
        spamreader = csv.reader(f)
        for row in spamreader:
            print(', '.join(row))

if __name__ == "__main__":
    get_sh_csv()
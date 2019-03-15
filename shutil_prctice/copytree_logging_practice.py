from shutil import copytree
import logging

def _logpath(path, names):
    logging.info('Working in %s', path)
    return []   # nothing will be ignored

if __name__ == "__main__":
    source = '/home/scrapy/source_code'
    destination = '/home/scrapy/destination_code'
    copytree(source, destination, ignore=_logpath)
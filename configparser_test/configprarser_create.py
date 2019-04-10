import configparser

def create_ini():
    config = configparser.ConfigParser()
    config['DEFAULT'] = {'ServerAliveInterval': '45',
                          'Compression': 'yes',
                          'CompressionLevel': '9'}
    config['bitbucket.org'] = {}
    config['bitbucket.org']['User'] = 'hg'
    config['topsecret.server.com'] = {}
    topsecret = config['topsecret.server.com']
    topsecret['Port'] = '50022'
    topsecret['ForwardX11'] = 'no'
    config['DEFAULT']['ForwardX11'] = 'yes'
    with open('./example.ini', 'w') as configfile:
        config.write(configfile)

if __name__ == "__main__":
    create_ini()
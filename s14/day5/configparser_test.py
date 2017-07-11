import configparser
__author__ = "Steven Lee"

config = configparser.ConfigParser()
config["DEFAULT"] = {'ServerAliveInterval': '45', 'Compression': 'yes', 'CompressionLevel': '9'}
config['DEFAULT']['ForwardX11'] = 'yes'

config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'stevenlee'

config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Host Port'] = '50022'  # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here

with open('example.ini', 'w') as configfile:
    config.write(configfile)

config = configparser.ConfigParser()
print(config.sections())
print(config.read('example.ini'))
print(config.sections())
print('bitbucket.org' in config)  # print True
print('bytebucket.org' in config)  # print False
print(config['bitbucket.org']['User'])  # print stevenlee
print(config['DEFAULT']['Compression'])  # print yes

topsecret = config['topsecret.server.com']
print(topsecret['ForwardX11'])
print(topsecret['Host Port'])

for key in config['bitbucket.org']:  # 默认(DEFAULT)配置会加载
    print(key)

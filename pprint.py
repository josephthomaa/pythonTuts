import pprint

stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
stuff.insert(0, stuff)
#from urllib.request import urlopen
#with urlopen('https://pypi.org/pypi/sampleproject/json') as resp:
#	project_info = json.load(resp)['info']
pprint.pprint(stuff)	
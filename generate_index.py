''' Python script to generate a stub README.md files from a plugin.json file '''
import json
import argparse
import os
import sys
import configparser
from collections import OrderedDict

parser = argparse.ArgumentParser(description = 'Generate README.md index of all plugins')
parser.add_argument("-f", "--force", help = 'will automatically overwrite existing README', action='store_true')

args = parser.parse_args()

os.path.realpath(__file__)


basedir=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'plugins')
outputfile = os.path.join(basedir, 'README.md')

if not args.force and os.path.isfile(outputfile):
	print("Cowardly refusing to overwrite an existing README. Remove or re-run with -f.")
	sys.exit(0)

#channels = glob.glob(os.path.join(basedir,"*"))
channels = os.walk(basedir).next()[1]

template = '# Binary Ninja Plugins\n\n'

config = configparser.ConfigParser()
config.readfp(open(os.path.join(basedir, '..', '.gitmodules')))
submodules={}

for section in config.items()[1:]:
	sectionname = section[0].split('"')[1]
	submodules[sectionname] = config.get(section[0], 'url')

for channel in ['official', 'community']: #because otherwise it's alphabetical
	index = os.path.join(basedir,channel+".json")
	if not args.force and os.path.isfile(index):
		print("Cowardly refusing to overwrite an existing index. Remove or re-run with -f.")
		sys.exit(0)

	plugins = []

	if channel.startswith('.'):
		continue

	template += "## {}\n\n".format(channel.title())

	template += '''| PluginName | Author | License | Description |
|------------|--------|---------|-------------|
'''

	for plugin in os.walk(os.path.join(basedir,channel)).next()[1]:
		try:
			url = submodules[os.path.join('plugins', channel, plugin)]
                        if url.endswith('.git'):
                            url = url[:-4]
		except:
                    url = 'https://github.com/Vector35/binaryninja-plugins/tree/master/plugins/{channel}/{plugin}'.format(channel = channel, plugin = plugin)
		data = json.load(open(os.path.join(basedir,channel,plugin,"plugin.json")), object_pairs_hook=OrderedDict)['plugin']
                data['url'] = url
		plugins.append(data)
		template += '|[{name}]({url})|{author}|[{license}]({channel}/{plugin}/LICENSE)|{description}|\n'.format(name = data['name'], channel = channel,
			url = url, plugin = plugin, author = data['author'],
			license = data['license']['name'], description = data['description'])
	template += "\n\n"
	print("Writing {outputfile}".format(outputfile=index))
	open(index, 'w').write(json.dumps(plugins))

print("Writing {outputfile}".format(outputfile=outputfile))
open(outputfile, 'w').write(template)

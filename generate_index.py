''' Python script to generate a stub README.md files from a plugin.json file '''
import json
import argparse
import os
import sys

parser = argparse.ArgumentParser(description = 'Generate README.md index of all plugins')
parser.add_argument("-f", "--force", help = 'will automatically overwrite existing README', action='store_true')

args = parser.parse_args()

os.path.realpath(__file__)


basedir=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'plugins')
outputfile = os.path.join(basedir, 'README.md')

if not args.force and os.path.isfile(outputfile):
	print("Cowardly refusing to overwrite an existing index.")
	sys.exit(0)

#channels = glob.glob(os.path.join(basedir,"*"))
channels = os.walk(basedir).next()[1]

template = '# Binary Ninja Plugins\n\n'

for channel in ['core', 'community']: #because otherwise it's alphabetical
	if channel.startswith('.'):
		continue

	template += "## {}\n\n".format(channel.title())

	template += '''| PluginName | Author | License | Description |
|------------|--------|---------|-------------|
'''

	for plugin in os.walk(os.path.join(basedir,channel)).next()[1]:
		data = json.load(open(os.path.join(basedir,channel,plugin,"plugin.json")))['plugin']
		template += '|[{name}](plugins/{channel}/{plugin})|{author}|[{license}](plugins/{channel}/{plugin}/LICENSE)|{description}|\n'.format(name = data['name'], channel = channel,
					plugin = plugin, author = data['author'],
					license = data['license']['name'], description = data['description'])
	template += "\n\n"

open(outputfile, 'w').write(template)

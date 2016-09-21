# Binary Ninja Plugins

Repository to track Binary Ninja Plugins, Themes, and other related tools

## Plugins

Binary Ninja plugins are available in different channels. Currently, there are two channels:

 - [Official](plugins/official): The official channel includes plugins written directly by [Vector 35](https://vector35.com/) or written by a third-party and verified by Vector 35. We have at least done our best to ensure they use the current plugin writing best-practices and provide useful functionality.

 - [Community](plugins/community): The community channel includes plugins written by third-parties that are not verified for quality, safety, or efficacy.  

 - [Combined](plugins/): A combined list of all plugins.

A [sample plugin](plugins/official/sample_plugin/) is available to demonstrate the required format for plugins.

### Installing Plugins

To install plugins, you can either clone this repository, or clone the specific plugin you are interested in and

### Contributing Plugins

To add your plugin to this repository, please first make sure that it parses properly using the [generate_index.py](generate_index.py) and then issue a pull request adding your plugin as a submodule, or file a new [issue](/../../issues/new).

## License

Note that content contained in the root of this repository itself is Copyright 2016, Vector 35 LLC and [available](LICENSE) under an MIT license, but that each individual plugin may be released under a different license.
